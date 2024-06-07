#   Copyright 2018 Samuel Payne sam_payne@byu.edu
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import pandas as pd
import os
from pyranges import read_gtf
from cptac.cancers.source import Source

class BroadHnscc(Source):
    def __init__(self, no_internet=False):
        """
        Initialize the BroadHnscc class by setting up required parameters and
        calling the parent's __init__ function.

        Parameters:
        no_internet (bool, optional): If set to True, skips the index update step which requires an internet connection.
        This is useful in situations with spotty internet connections.
        """

        # Define necessary files and loading functions
        self.data_files = {
            "transcriptomics" : "HNSCC.rsem_transcripts_tpm.txt.gz",
            "mapping" : ["sample_descriptions.tsv.gz", "gencode.v34.GRCh38.genes.collapsed_only.gtf.gz"]
        }
        
        self.load_functions = {
            'transcriptomics' : self.load_transcriptomics,
        }
        
        # Call the parent class constructor
        super().__init__(cancer_type="hnscc", source='broad', data_files=self.data_files, load_functions=self.load_functions, no_internet=no_internet)

    def load_mapping(self):
        """
        Load the mapping files and process them accordingly.

        This method locates the mapping files in the specified directory, reads the files,
        and processes the data to create a dictionary for broad keys and broad gene names.
        These dictionaries are then stored in the _helper_tables attribute for later use.
        """

        if not self._helper_tables:
            file_path_list = self.locate_files('mapping')
            for file_path in file_path_list:
                file_name = file_path.split('/')[-1] # Get the filename
                
                if file_name == "sample_descriptions.tsv.gz":
                    # Load, filter and transform the sample description data
                    broad_key = pd.read_csv(file_path, sep="\t")
                    broad_key = broad_key.loc[broad_key['cohort'] == "HNSCC"] #get only HNSCC keys
                    broad_key = broad_key[["sample_id","GDC_id","tissue_type"]]
                    broad_key = broad_key.set_index("sample_id")#set broad id as index
                    #add tumor type identification to end
                    broad_key["Patient_ID"] = broad_key["GDC_id"] + broad_key["tissue_type"] 
                    #change so tumor samples have nothing on end of id and .N for normal samples
                    broad_key.Patient_ID = broad_key.Patient_ID.str.replace(r"Tumor", "", regex=True)
                    broad_key.Patient_ID = broad_key.Patient_ID.str.replace(r"Normal", ".N", regex=True)
                    #covert df to dictionary
                    broad_dict = broad_key.to_dict()["Patient_ID"]
                    self._helper_tables["broad_key"] = broad_dict
                    
                elif file_name == "gencode.v34.GRCh38.genes.collapsed_only.gtf.gz":
                    # Load and transform the gene names data
                    broad_gene_names = read_gtf(file_path)
                    broad_gene_names = broad_gene_names.as_df()
                    broad_gene_names = broad_gene_names[["gene_name","gene_id"]]
                    broad_gene_names = broad_gene_names.rename(columns= {"gene_name":"Name"}) #change name to merge 
                    broad_gene_names = broad_gene_names.set_index("gene_id")
                    broad_gene_names = broad_gene_names.drop_duplicates()
                    self._helper_tables["broad_gene_names"] = broad_gene_names
        
    def load_transcriptomics(self):
        """
        Load transcriptomics data, process it and store it in the _data attribute.

        This method first checks if the transcriptomics data is already loaded.
        If not, it locates the transcriptomics file, reads the data, and processes it.
        It joins the data with gene names and renames the columns with CPTAC IDs.
        The processed dataframe is then saved into the _data attribute.
        """

        if 'transcriptomics' not in self._data:
            # Load initial transcriptomic data
            file_path = self.locate_files('transcriptomics')
            
            df = pd.read_csv(file_path, sep="\t")
            df = df.set_index(["transcript_id","gene_id"])
            
            # Add gene names to transcriptomic data
            self.load_mapping()
            broad_gene_names = self._helper_tables["broad_gene_names"]
            broad_dict = self._helper_tables["broad_key"]        
            df = broad_gene_names.join(df, how = "left") #merge in gene names keep transcripts that have a gene name
            df = df.reset_index()
            df = df.rename(columns= {"transcript_id": "Transcript_ID","gene_id":"Database_ID"})
            df = df.set_index(["Name","Transcript_ID","Database_ID"])
            df = df.rename(columns = broad_dict)# rename columns with CPTAC IDs
            df = df.sort_index() 
            df = df.T
            df.index.name = "Patient_ID"
            # Save transcriptomic data in self._data
            self.save_df('transcriptomics', df)