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
from pyranges import read_gtf

from cptac.cancers.source import Source
from cptac.cancers.mssm.mssm import Mssm

class WashuOv(Source):
    def __init__(self, no_internet=False):
        """Initialize WashuOv object.

        Parameters:
        no_internet (bool, optional): If True, skip the index update step. Default is False.
        """
        
        # Set some needed variables, and pass them to the parent Dataset class __init__ function

        self.data_files = {
            "cibersort"             : "CIBERSORT.Output_Abs_OV.txt.gz",
            "CNV"                   : "OV.gene_level.from_seg.filtered.tsv.gz",
            "mapping"               : "gencode.v22.annotation.gtf.gz",
            "miRNA"                : ["OV_precursor_miRNA_combined.tsv.gz","OV_mature_miRNA_combined.tsv.gz","OV_total_miRNA_combined.tsv.gz"], # waiting for data
            # "readme"                : ["README_miRNA","README_CIBERSORT","README_xCell","README_somatic_mutation_WXS","README_gene_expression","README.boxnote","README_ESTIMATE_WashU"],
            "somatic_mutation"      : "OV_prospective.dnp.annotated.exonic.addrecovercases.maf.gz",
            "transcriptomics"       : "OV_tumor_RNA-Seq_Expr_WashU_FPKM.tsv.gz",
            "tumor_purity"          : "CPTAC_pancan_RNA_tumor_purity_ESTIMATE_WashU.tsv.gz",
            "xcell"                 : "OV_xCell.txt.gz",
            "hla_typing": "hla.sample.ct.10152021.sort.tsv.gz"
        }

        #self._readme_files = {}

        self.load_functions = {
            'transcriptomics'   : self.load_transcriptomics,
            'somatic_mutation'  : self.load_somatic_mutation,
            'miRNA'             : self.load_miRNA,
            'xcell'             : self.load_xcell,
            'cibersort'         : self.load_cibersort,
            'CNV'               : self.load_CNV,
            'tumor_purity'      : self.load_tumor_purity,
            #'readme'            : self.load_readme,
            "hla_typing"        : self.load_hla_typing
        }

        # Call the parent class __init__ function
        super().__init__(cancer_type="ov", source='washu', data_files=self.data_files, load_functions=self.load_functions, no_internet=no_internet)

    def load_transcriptomics(self):
        """Load the transcriptomics dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'transcriptomics'
        if df_type not in self._data:
            file_path = self.locate_files(df_type)

            df = pd.read_csv(file_path, sep="\t")
            df = df.rename(columns={"gene_name": "Name","gene_id": "Database_ID"})
            df = df.set_index(["Name", "Database_ID"])
            df = df.sort_index()
            df = df.T
            df.index.name = "Patient_ID"
            #remove label for tumor samples. All samples are tumors 
            df.index = df.index.str.replace(r"-T", "", regex=True) 
            # save df in self._data
            self.save_df(df_type, df)

    def load_somatic_mutation(self):
        """Load the somatic mutation dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'somatic_mutation'
        if df_type not in self._data:
            file_path = self.locate_files(df_type)

            df = pd.read_csv(file_path, sep='\t')    
            # Rename the columns we want to keep to the appropriate names
            df = pd.read_csv(file_path, sep='\t')    
            df['Patient_ID'] = df.loc[:, 'Tumor_Sample_Barcode']
            df = df.rename(columns={
                        "Hugo_Symbol":"Gene",
                        "Gene":"Gene_Database_ID",
                        "Variant_Classification":"Mutation",
                        "HGVSp_Short":"Location"})

            df = df.set_index("Patient_ID")
            df = df[ ['Gene'] + ["Mutation"] + ["Location"] + [ col for col in df.columns if col not in ["Gene","Mutation","Location"] ] ]
            df.index = df.index.str.replace(r"_T", "", regex=True)     
            # save df in self._data
            self.save_df(df_type, df)

    
    def load_xcell(self):
        """Load the xcell dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'xcell'
        if df_type not in self._data:
            file_path = self.locate_files(df_type)

            df = pd.read_csv(file_path, sep = '\t', index_col = 0) 
            df = df.transpose()
            df.columns.name = 'Name'
            df.index.name = 'Patient_ID'
            df.index = df.index.str.replace(r'-T$', '', regex=True) # remove label for tumor samples
            df.index = df.index.str.replace(r'-A$', '.N', regex=True) # change label for normal samples
            # save df in self._data
            self.save_df(df_type, df)

    def load_cibersort(self):
        """Load the cibersort dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'cibersort'
        if df_type not in self._data:
            file_path = self.locate_files(df_type)

            df = pd.read_csv(file_path, sep = '\t', index_col = 0) 
            df.index.name = 'Patient_ID'
            df.columns.name = 'Name'
            df.index = df.index.str.replace(r'-T$', '', regex=True) 
            df.index = df.index.str.replace(r'-A$', '.N', regex=True)
            # save df in self._data
            self.save_df(df_type, df)

    def load_mapping(self):
        """Load the mapping dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the datframe, processes it, and saves it in the _helper_tables attribute.
        """
        df_type = 'mapping'
        if "CNV_gene_ids" not in self._helper_tables:
            file_path = self.locate_files(df_type)

            df = read_gtf(file_path)
            df = df.as_df()
            df = df[["gene_name","gene_id"]]
            df = df.drop_duplicates()
            df = df.rename(columns={"gene_name": "Name","gene_id": "Database_ID"})
            df = df.set_index("Name")
            self._helper_tables["CNV_gene_ids"] = df  

    def load_CNV(self):
        """Load the CNV dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'CNV'
        if df_type not in self._data:
            file_path = self.locate_files(df_type)

            df = pd.read_csv(file_path, sep="\t")
            df = df.rename(columns={"Gene": "Name"})
            df = df.set_index("Name")
            cnv = df

            self.load_mapping()
            gene_ids = self._helper_tables["CNV_gene_ids"]
            df = cnv.join(gene_ids,how = "left") #merge in gene_ids 
            df = df.reset_index()
            df = df.set_index(["Name", "Database_ID"]) #create multi-index
            df = df.T
            df.index.name = 'Patient_ID'
            # save df in self._data
            self.save_df(df_type, df)

    def load_tumor_purity(self):
        """Load the tumor purity dataframe

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'tumor_purity'
        if df_type not in self._data:
            file_path = self.locate_files(df_type)

            df = pd.read_csv(file_path, sep = "\t", na_values = 'NA')
            df.Sample_ID = df.Sample_ID.str.replace(r'-T', '', regex=True) # only tumor samples in file
            df = df.set_index('Sample_ID') 
            df.index.name = 'Patient_ID' 

            # get clinical df (used to slice out cancer specific patient_IDs in tumor_purity file)
            mssmclin = Mssm(filter_type='ov', no_internet=self.no_internet)
            clinical_df = mssmclin.get_df('clinical')               
            patient_ids = clinical_df.index.to_list()
            df = df.loc[df.index.isin(patient_ids)]    

            # save df in self._data
            self.save_df(df_type, df)

    def load_miRNA(self):
        """Load the miRNA dataframe.

        This method first checks if the dataframe is already loaded. If not, 
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'miRNA'
        if df_type not in self._data:
            file_paths = self.locate_files(df_type)

            # This is just an example; the actual loading will depend on your data
            df = pd.concat([pd.read_csv(file_path, sep='\t') for file_path in file_paths])
            df = df.rename(columns={"YourColumnName": "NewColumnName"})
            df = df.set_index("NewColumnName")

            # Further processing here, if necessary

            self.save_df(df_type, df)

    def load_hla_typing(self):
        """Load the hla_typing dataframe.

        This method first checks if the dataframe is already loaded. If not,
        it loads the dataframe, processes it, and saves it in the _data attribute.
        """
        df_type = 'hla_typing'

        if df_type not in self._data:
            # perform initial checks and get file path (defined in source.py, the parent class)
            file_path = self.locate_files(df_type)

            # which cancer_type goes with which cancer in the mssm table
            tumor_codes = {'brca':'BR', 'ccrcc':'CCRCC',
                           'ucec':'UCEC', 'gbm':'GBM', 'hnscc':'HNSCC',
                           'lscc':'LSCC', 'luad':'LUAD', 'pdac':'PDA',
                           'hcc':'HCC', 'coad':'CO', 'ov':'OV'}

            df = pd.read_csv(file_path, sep='\t')
            df = df.loc[df['Cancer'] == tumor_codes[self.cancer_type]]
            df = df.set_index("Sample")
            df.index.name = 'Patient_ID'
            df = df.sort_values(by=["Patient_ID"])

            self.save_df(df_type, df)

        return self._data[df_type]