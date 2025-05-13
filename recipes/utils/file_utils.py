# (C) Copyright IBM Corp. 2024.
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import os
import requests
from humanfriendly import format_size
import pandas as pd
import glob
from urllib.parse import unquote

# from typing import List, Optional

## Reads parquet files in a folder into a pandas dataframe
def read_parquet_files_as_df(parquet_dir: str)  -> pd.DataFrame:
    """
    Reads all parquet files from a directory and combines them into a single pandas DataFrame.

    Args:
        parquet_dir (str): Path to the directory containing parquet files.

    Returns:
        pandas.DataFrame: A concatenated DataFrame containing data from all parquet files.
                         Returns an empty DataFrame if no files are found or all files are empty.

    Example usage:
        df = read_parquet_files_as_df('data/parquet_files/')
    """
    parquet_files = glob.glob(os.path.join(parquet_dir, '*.parquet'))
    if not parquet_files:
        print(f"No parquet files found in {parquet_dir}")
        return pd.DataFrame()

    # read each parquet file into a DataFrame and store in a list
    dfs: list[pd.DataFrame] = []
    for file in parquet_files:
        try:
            df: pd.DataFrame = pd.read_parquet(file)
            if not df.empty:
                dfs.append(df)
        except Exception as e:
            print(f"Error reading {file}: {str(e)}")

    # Concatenate all DataFrames into a single DataFrame
    if dfs:
        data_df: pd.DataFrame = pd.concat(dfs, ignore_index=True)
        print(f"Successfully read {len(dfs)} parquet files with {len(data_df)} total rows")
        return data_df
    else:
        print("No data found in parquet files")
        return pd.DataFrame()  # return empty df
# ------------
