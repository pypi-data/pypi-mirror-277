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

# User-directed exceptions
class CptacError(Exception):
    """Base class for all exceptions we'll raise."""
    pass

class NoInternetError(CptacError):
    """No internet."""
    pass

class HttpResponseError(CptacError):
    """There was a problem with an HTTP response."""
    pass

class InvalidParameterError(CptacError):
    """Invalid parameter."""
    pass

class FileError(CptacError):
    """Base class for data-related errors."""
    pass

class DatasetNotInstalledError(FileError):
    """They requested a dataset they haven't installed."""
    pass

class MissingFileError(FileError):
    """A data file was missing."""
    pass

class DownloadFailedError(FileError):
    """A file download failed."""
    pass

class DataError(CptacError):
    """Something was wrong with the data."""
    pass

class ReindexMapError(DataError):
    """Problem reindexing a dataframe."""
    pass

class DropFromSingleIndexError(DataError):
    """They tried to drop a level from a single-level index."""
    pass

class NoDefinitionsError(DataError):
    """They tried to access definitions for a dataset that doesn't provide any."""
    pass

class DataFrameNotIncludedError(DataError):
    """They requested a dataframe that's not included in the dataset."""
    pass


class DataSourceNotFoundError(CptacError):
    """They requested a data source that we don't have."""
    pass

class DataTypeNotInSourceError(CptacError):
    """The source they requested does not have the data type they requested."""
    pass

class PdcDownloadError(CptacError):
    """There was a problem downloading data from the Proteomic Data Commons."""
    pass

# Warnings
class CptacWarning(UserWarning):
    """Base class for all warnings we'll generate."""
    pass

class FailedReindexWarning(CptacWarning):
    """Error reindexing a dataframe."""
    pass

class InsertedNanWarning(CptacWarning):
    """NaNs were inserted during a dataframe join."""
    pass

class DataTypeNotInSourceWarning(CptacWarning):
    """The source they requested does not have the data type they requested. But other sources were found.
    Sometimes a datatype exists for some cancers in a source but not all.
    """
    pass

class DuplicateColumnHeaderWarning(CptacWarning):
    """Due to a requested column multiindex flattening, the column index now has duplicate labels."""
    pass

class FlattenSingleIndexWarning(CptacWarning):
    """They tried to flatten a single-level index. We didn't do anything."""
    pass

class FilledMutationDataWarning(CptacWarning):
    """Mutation data was automatically filled during a dataframe join."""
    pass

class ParameterWarning(CptacWarning):
    """We should warn them about a parameter for some reason."""
    pass

class PublicationEmbargoWarning(CptacWarning):
    """There is a publication embargo on the dataset."""
    pass

class FileNotUpdatedWarning(CptacWarning):
    """A file they wanted to update wasn't updated."""
    pass

class FailedChecksumWarning(CptacWarning):
    """A datafile failed a checksum test."""
    pass

class DatasetAlreadyInstalledWarning(CptacWarning):
    """The dataset was already installed, and they didn't want to redownload it."""
    pass

class StatsWarning(CptacWarning):
    """Statistics-related warnings."""
    pass

class StDevWarning(StatsWarning):
    """Warning about standard deviation."""
    pass

class PvalWarning(StatsWarning):
    """Some warning related to p values."""
    pass

class OldPackageVersionWarning(CptacWarning):
    """They're using an old version of the package."""
    pass

# Developer-directed exceptions
class CptacDevError(Exception):
    """For exceptions that are probably the developer's fault."""
    pass

