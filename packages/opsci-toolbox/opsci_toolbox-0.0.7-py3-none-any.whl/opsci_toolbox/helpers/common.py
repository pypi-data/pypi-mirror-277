import os
import pandas as pd
import pickle
import glob
import requests
import json
from tqdm import tqdm
import shutil
import zipfile
import random
from collections import Counter
import gspread
from google.auth import exceptions
import pyarrow.parquet as pq
from datetime import datetime
import hashlib
import ast
import subprocess

####################################################################################################
# FILE LOADERS
####################################################################################################

def load_file(path: str, delimiter: str = ";", decimal: str = ".")  -> pd.DataFrame:
    """
    Load a file into a Pandas DataFrame based on the file extension.

    Parameters:
    path (str): The file path to load.
    delimiter (str, optional): The delimiter used in CSV/TSV files. Default is ";".
    decimal (str, optional): The character used for decimal points in CSV/TSV files. Default is ".".

    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.

    Raises:
    ValueError: If the file extension is not supported.
    """
    extension = os.path.splitext(os.path.basename(path))[1]
    if extension == ".parquet":
        df = load_parquet(path)
    elif extension == ".pickle":
        df = load_pickle(path)
    elif extension == ".json":
        df = load_json(path)
    elif extension == ".jsonl":
        df = load_jsonl(path)
    elif extension == ".csv":
        df = load_csv(path, delimiter = delimiter, decimal =decimal)
    elif extension == ".tsv":
        df = load_csv(path, delimiter = "\t", decimal =decimal)
    else :
        print("Check your input file. Extension isn't supported : .parquet, .pickle, .json, .jsonl, .csv, .tsv")
    return df

def load_parquet(path: str) -> pd.DataFrame:
    """
    Load a parquet file into a DataFrame.
    
    Parameters:
    path (str): The file path to the parquet file.
    
    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    
    Raises:
    Exception: If there is an error reading the parquet file.
    """
    try:
        table = pq.read_table(path)
        df = table.to_pandas()
    except Exception as e:
        pass
        print(e)
    return df

def load_pickle(path: str) -> pd.DataFrame:
    """
    Load a pickle file into a DataFrame.
    
    Parameters:
    path (str): The file path to the pickle file.
    
    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    return pd.read_pickle(path)


def load_json(path: str) -> pd.DataFrame:
    """
    Load a JSON file into a DataFrame.
    
    Parameters:
    path (str): The file path to the JSON file.
    
    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    
    Raises:
    Exception: If there is an error reading the JSON file.
    """
    df = pd.DataFrame()
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        df = pd.json_normalize(data)
    except Exception as e:
        print(f"Error reading the JSON file: {e}")
        raise
    return df

def load_jsonl(path: str) -> pd.DataFrame:
    """
    Load a JSON Lines (jsonl) file into a DataFrame.
    
    Parameters:
    path (str): The file path to the jsonl file.
    
    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    
    Raises:
    Exception: If there is an error reading the jsonl file.
    """
    df = pd.DataFrame()
    try:
        data = []
        with open(path, 'r') as json_file:
            for line in tqdm(json_file, desc="Loading JSON Lines"):
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as line_error:
                    print(f"Error decoding line: {line_error}")
            
        df = pd.json_normalize(data)
    except Exception as e:
        print(f"Error reading the jsonl file: {e}")
        raise
    return df


def load_csv(path: str, delimiter: str = ";", decimal: str = ".") -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.
    
    Parameters:
    path (str): The file path to the CSV file.
    delimiter (str, optional): The delimiter used in the CSV file. Default is ";".
    decimal (str, optional): The character used for decimal points in the CSV file. Default is ".".
    
    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    
    Raises:
    Exception: If there is an error reading the CSV file.
    """
    df = pd.DataFrame()
    try:
        df = pd.read_csv(path, delimiter=delimiter, encoding="utf-8", decimal=decimal)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        raise
    return df

def read_txt_to_list(file_path: str) -> list[str]:
    """
    Read a text file line by line and append to a Python list.
    
    Parameters:
    file_path (str): The file path to the text file.
    
    Returns:
    list[str]: A list of lines read from the text file.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    Exception: If any other error occurs during file reading.
    """
    
    # Initialize an empty list to store the lines
    lines = []

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line and append it to the list
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    return lines

def read_json(path: str) -> dict:
    """
    Read a JSON file and return a dictionary.
    
    Parameters:
    path (str): The file path to the JSON file.
    
    Returns:
    dict: The data read from the JSON file as a dictionary.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    Exception: If there is an error reading the JSON file.
    """
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data

def read_txt_file(file_path: str) -> str:
    """
    Read the content of a text file and return it as a string.
    
    Parameters:
    file_path (str): The file path to the text file.
    
    Returns:
    str: The content of the text file as a string.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    Exception: If there is an error reading the text file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        raise
    return content

def read_jsonl(path: str) -> list[dict]:
    """
    Load a JSON Lines (jsonl) file into a list of dictionaries.
    
    Parameters:
    path (str): The file path to the jsonl file.
    
    Returns:
    list[dict]: A list of dictionaries containing the data read from the JSON Lines file.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    Exception: If there is an error reading the jsonl file.
    """
    json_data = []
    try:
        with open(path, 'r') as json_file:
            for line in tqdm(json_file, desc="Reading JSON Lines"):
                try:
                    json_data.append(json.loads(line))
                except Exception as e:
                    print(f"Error decoding line: {e}")
                    raise
    except FileNotFoundError:
        print(f"File not found: {path}")
        raise
    return json_data


#########################################################################################
# FILE WRITERS
#########################################################################################


def write_pickle(data: pd.DataFrame, path: str, filename: str) -> str:
    """
    Write a DataFrame into a pickle file.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to be written to the pickle file.
    path (str): The directory where the pickle file will be saved.
    filename (str): The name of the pickle file (without the extension).
    
    Returns:
    str: The full path to the saved pickle file.
    """
    file_path = os.path.join(path, filename + '.pickle')
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)
    return file_path


def write_list_to_txt(input_list: list, path: str, name: str) -> str:
    """
    Write a list to a text file, with each item on a new line.

    Parameters:
    - input_list (list): The list to be written to the text file.
    - path (str): The directory path where the text file will be saved.
    - name (str): The name of the text file (without the extension).

    Returns:
    str: The full path to the saved text file.
    """
    file_path = os.path.join(path, name + '.txt')
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')
    return file_path

def write_jsonl(data: list[dict], path: str, name: str) -> str:
    """
    Write data to a JSON Lines (jsonl) file. Each dictionary in the list represents a single JSON object.

    Parameters:
    - data (list[dict]): The list of dictionaries to be written to the JSON Lines file.
    - path (str): The directory path where the JSON Lines file will be saved.
    - name (str): The name of the JSON Lines file (without the extension).

    Returns:
    str: The full path to the saved JSON Lines file.
    """
    file_path = os.path.join(path, name + '.jsonl')
    with open(file_path, 'w') as file:
        for entry in data:
            json.dump(entry, file)
            file.write('\n')
    return file_path


def write_json(json_dict: dict, path: str, name: str) -> str:
    """
    Write a dictionary to a JSON file.

    Parameters:
    - json_dict (dict): The dictionary to be written to the JSON file.
    - path (str): The directory path where the JSON file will be saved.
    - name (str): The name of the JSON file (without the extension).

    Returns:
    str: The full path to the saved JSON file.
    """
    file_path = os.path.join(path, name + '.json')
    with open(file_path, 'w') as outfile:
        json.dump(json_dict, outfile)
    return file_path


def write_dataframe_to_json(df: pd.DataFrame, path: str, name: str, orient: str = 'records') -> str:
    """
    Write a DataFrame to a JSON file.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be written to the JSON file.
    - path (str): The directory path where the JSON file will be saved.
    - name (str): The name of the JSON file (without the extension).
    - orient (str, optional): The format of the JSON file. Default is 'records'.

    Returns:
    str: The full path to the saved JSON file.
    """
    file_path = os.path.join(path, name + ".json")
    df.to_json(file_path, orient=orient, lines=True)
    return file_path
    
    
def save_dataframe_excel(df: pd.DataFrame, path: str, name: str, sheet_name: str) -> str:
    """
    Write a DataFrame to an Excel file.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be written to the Excel file.
    - path (str): The directory path where the Excel file will be saved.
    - name (str): The name of the Excel file (without the extension).
    - sheet_name (str): The name of the Excel sheet.

    Returns:
    str: The full path to the saved Excel file.
    """
    file_path = os.path.join(path, f"{name}.xlsx")
    df.to_excel(file_path, sheet_name=sheet_name, index=False)
    print(file_path, "- File created")
    return file_path

def add_dataframe_to_excel(df: pd.DataFrame, existing_file_path: str, new_sheet_name: str) -> None:
    """
    Adds a DataFrame to an existing Excel file as a new sheet.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be added.
    - existing_file_path (str): Path to the existing Excel file.
    - new_sheet_name (str): Name of the new sheet in the Excel file.

    Returns:
    - None
    """
    # Read existing Excel file into a dictionary of DataFrames
    excel_file = pd.read_excel(existing_file_path, sheet_name=None)

    # Add the new DataFrame to the dictionary with the specified sheet name
    excel_file[new_sheet_name] = df

    # Write the updated dictionary of DataFrames back to the Excel file
    with pd.ExcelWriter(existing_file_path, engine='xlsxwriter') as writer:
        for sheet_name, df in excel_file.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

def save_dataframe_csv(df: pd.DataFrame, path: str, name: str) -> str:
    """
    Save a DataFrame to a CSV file within a specified directory.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be saved.
    - path (str): The directory where the CSV file will be saved.
    - name (str): The desired name for the CSV file (without extension).

    Returns:
    str: The full path to the saved CSV file.
    """
    file_path = os.path.join(path, f"{name}.csv")
    df.to_csv(
        file_path,
        sep=";",
        encoding="utf-8",
        index=False,
        decimal=",",
    )
    print("File saved:", file_path)
    return file_path

def write_txt_file(data: str, path: str, name: str) -> str:
    """
    Write a string to a text file.

    Parameters:
    - data (str): The string to be written to the text file.
    - path (str): The directory path where the text file will be saved.
    - name (str): The name of the text file (without the extension).

    Returns:
    str: The full path to the saved text file.
    """
    file_path = os.path.join(path, name + '.txt')
    with open(file_path, "w") as file:
        file.write(data)
    return file_path

def split_df_into_chunks(df: pd.DataFrame, path: str, name: str, chunk_size: int = 10000) -> list[str]:
    """
    Split a DataFrame into multiple pickle files with a specified chunk size.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be split.
    - path (str): The directory path where the pickle files will be saved.
    - name (str): The base name for the pickle files.
    - chunk_size (int, optional): The size of each chunk. Default is 10000.

    Returns:
    list[str]: A list of file paths to the saved pickle files.
    """
    num_chunks = -(-len(df) // chunk_size)  # Calculate the number of chunks using ceil division

    file_paths = []

    # create smaller datasets of chunk_size each
    for i in range(num_chunks):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        chunk = df.iloc[start:end]
        filename = f"{name}_{i}"  # Adjust the filename format as needed
        file_path = write_pickle(chunk, path, filename)
        file_paths.append(file_path)

    return file_paths

###################################################################################################
# FOLDERS / FILES HELPERS
###################################################################################################

def create_dir(path: str) -> str:
    """
    Create a local directory if it doesn't exist.

    Parameters:
    - path (str): The directory path to be created.

    Returns:
    str: The path of the created directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(path, "- directory created")
    return path


def list_files_in_dir(path: str, filetype: str = '*.json') -> list[str]:
    """
    List files of a specific format in a directory.

    Parameters:
    - path (str): The directory path to search for files.
    - filetype (str, optional): The file type pattern to search for. Default is '*.json'.

    Returns:
    list[str]: A list of file paths matching the specified file type pattern.
    """
    pattern = os.path.join(path, filetype)
    files = glob.glob(pattern)
    return files


def list_subdirectories(root_directory: str) -> list[str]:
    """
    List subdirectories in a root directory.

    Parameters:
    - root_directory (str): The root directory path.

    Returns:
    list[str]: A list of subdirectory names.
    """
    subdirectories = []
    for entry in os.scandir(root_directory):
        if entry.is_dir():
            subdirectories.append(entry.name)
    return subdirectories


def list_recursive_subdirectories(root_directory: str) -> list[str]:
    """
    List recursively all subdirectories from a root directory.

    Parameters:
    - root_directory (str): The root directory path.

    Returns:
    list[str]: A list of subdirectory paths.
    """
    subdirectories = []
    for root, dirs, files in os.walk(root_directory):
        subdirectories.extend([os.path.join(root, d) for d in dirs])
    return subdirectories


def list_files_in_subdirectories(path: str, filetype: str = '*.json') -> list[str]:
    """
    Walk through subdirectories of a root directory to list files of a specific format.

    Parameters:
    - path (str): The root directory path.
    - filetype (str, optional): The file type pattern to search for. Default is '*.json'.

    Returns:
    list[str]: A list of file paths matching the specified file type pattern in subdirectories.
    """
    files = []

    # Check if the directory exists
    if not os.path.exists(path):
        print(f"The directory '{path}' does not exist.")
        return files

    # Use glob to get all files in the directory and its subdirectories
    pattern = os.path.join(path, '**', filetype)
    files = glob.glob(pattern, recursive=True)

    return files

def copy_file(source_path: str, destination_path: str, new_filename: str = '') -> str:
    """
    Copy a file from a source path to a destination path.

    Parameters:
    - source_path (str): The path of the source file.
    - destination_path (str): The path of the destination directory.
    - new_filename (str, optional): The new filename. If not provided, the original filename is used.

    Returns:
    str: The path of the copied file.
    """
    if new_filename:
        file_path = os.path.join(destination_path, new_filename)
    else:
        filename = os.path.basename(source_path)
        file_path = os.path.join(destination_path, filename)
    
    shutil.copy(source_path, file_path)
    return file_path

def remove_file(file_path: str) -> None:
    """
    Remove a single file.

    Parameters:
    - file_path (str): The path of the file to be removed.

    Returns:
    None
    """
    try:
        os.remove(file_path)
        print(f"File {file_path} removed successfully.")
    except OSError as e:
        print(f"Error removing file {file_path}: {e}")
        
def remove_folder(folder_path: str) -> None:
    """
    Remove a folder and all its contents.

    Parameters:
    - folder_path (str): The path of the folder to be removed.

    Returns:
    None
    """
    try:
        shutil.rmtree(folder_path)
        print(f"Folder {folder_path} and its contents removed successfully.")
    except OSError as e:
        print(f"Error removing folder {folder_path}: {e}")
           
        
def get_file_size(file_path: str) -> tuple[int, str]:
    """
    Get the size of a single file in a readable format (KB, MB, GB).

    Parameters:
    - file_path (str): The path of the file.

    Returns:
    tuple[int, str]: A tuple containing the size of the file in bytes and its formatted size.
    If the file is not found, returns None.
    """
    try:
        size = os.path.getsize(file_path)

        # Define the units and their respective sizes
        units = ['B', 'KB', 'MB', 'GB']
        size_in_units = size
        unit_index = 0

        # Convert size to appropriate unit
        while size_in_units > 1024 and unit_index < len(units) - 1:
            size_in_units /= 1024
            unit_index += 1

        # Format the result
        formatted_size = "{:.2f} {}".format(size_in_units, units[unit_index])
        print(formatted_size)
        return size, formatted_size
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def get_folder_size(folder_path: str) -> tuple[int, str]:
    """
    Get the size of all files contained in a folder in a readable format (KB, MB, GB).

    Parameters:
    - folder_path (str): The path of the folder.

    Returns:
    tuple[int, str]: A tuple containing the total size of all files in bytes and its formatted size.
    If the folder is not found, returns None.
    """
    total_size = 0

    try:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)

        # Define the units and their respective sizes
        units = ['B', 'KB', 'MB', 'GB']
        size_in_units = total_size
        unit_index = 0

        # Convert size to appropriate unit
        while size_in_units > 1024 and unit_index < len(units) - 1:
            size_in_units /= 1024
            unit_index += 1

        # Format the result
        formatted_size = "{:.2f} {}".format(size_in_units, units[unit_index])

        return total_size, formatted_size
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
        return None

def file_creation_date(file_path: str) -> datetime:
    """
    Return the last update timestamp of a file.

    Parameters:
    - file_path (str): The path of the file.

    Returns:
    datetime: The last update timestamp as a datetime object.
    If the file does not exist, returns None.
    """
    # Check if the file exists
    if os.path.exists(file_path):
        # Get the last modified timestamp
        last_update_timestamp = os.path.getmtime(file_path)
        # Convert the timestamp to a datetime object
        last_update_date = datetime.fromtimestamp(last_update_timestamp)
        return last_update_date
    else:
        return None
    
############################################################################
# LISTS HELPERS
############################################################################
    
    
def transform_to_n_items_list(lst: list, n: int) -> list[list]:
    """
    Transform a list into a list of n-items sublists.

    Parameters:
    - lst (list): The input list to be transformed.
    - n (int): The number of items in each sublist.

    Returns:
    list[list]: A list of n-items sublists.
    """
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def unduplicate_list(lst: list) -> list:
    """ 
    Remove duplicate elements from a list.

    Parameters:
    - lst (list): The input list with possible duplicate elements.

    Returns:
    list: A list with duplicate elements removed.
    """
    return list(set(lst))


def sort_list(lst: list, reverse: bool = False) -> list:
    """
    Sort the list in ascending or descending order.

    Parameters:
    - lst (list): The input list.
    - reverse (bool): If True, sort the list in descending order. 
                     If False (default), sort the list in ascending order.

    Returns:
    list: A new list sorted based on the specified order.
    """
    return sorted(lst, reverse=reverse)


def map_list(lst: list, function: callable) -> list:
    """
    Apply a function to each element of the list.

    Parameters:
    - lst (list): The input list.
    - function (callable): The function to apply to each element.

    Returns:
    list: A new list with the function applied to each element.
    """
    return [function(element) for element in lst]


def flatten_list(lst: list) -> list:
    """
    Flatten a nested list into a single list.

    Parameters:
    - lst (list): The input nested list.

    Returns:
    list: A new list with all nested elements flattened.
    """
    flattened_list = []

    def flatten_recursive(sublist):
        for element in sublist:
            if isinstance(element, list):
                flatten_recursive(element)
            else:
                flattened_list.append(element)

    flatten_recursive(lst)
    return flattened_list


def find_occurrences(lst: list, element) -> int:
    """
    Find the occurrences of a specific element in the list.

    Parameters:
    - lst (list): The input list.
    - element: The element to find occurrences of.

    Returns:
    int: The number of occurrences of the specified element in the list.
    """
    return lst.count(element)


def is_subset(subset: list, superset: list) -> bool:
    """
    Check if one list is a subset of another.

    Parameters:
    - subset (list): The potential subset list.
    - superset (list): The superset list.

    Returns:
    bool: True if the subset is a subset of the superset, False otherwise.
    """
    return all(element in superset for element in subset)

def common_elements(list1: list, list2: list) -> list:
    """
    Find the common elements between two lists.

    Parameters:
    - list1 (list): The first list.
    - list2 (list): The second list.

    Returns:
    list: A new list containing the common elements between list1 and list2.
    """
    return list(set(list1) & set(list2))


def shuffle_list(lst: list) -> list:
    """
    Shuffle the elements of the list randomly.

    Parameters:
    - lst (list): The input list.

    Returns:
    list: A new list with the elements shuffled randomly.
    """
    shuffled_list = lst.copy()
    random.shuffle(shuffled_list)
    return shuffled_list


def sample_list(lst: list, sample_size) -> list:
    """
    Sample a list based on an integer or a float representing the sample size.

    Parameters:
    - lst (list): The input list.
    - sample_size (int or float): If an integer, the number of elements to keep.
                                 If a float, the percentage of elements to keep.

    Returns:
    list: A new list containing the sampled elements.

    Raises:
    - ValueError: If the sample size is invalid (negative integer or float outside [0, 1]).
    - TypeError: If the sample size is neither an integer nor a float.
    """
    if isinstance(sample_size, int):
        if sample_size < 0:
            raise ValueError("Sample size must be a non-negative integer.")
        return random.sample(lst, min(sample_size, len(lst)))
    elif isinstance(sample_size, float):
        if not 0 <= sample_size <= 1:
            raise ValueError("Sample size must be a float between 0 and 1.")
        sample_size = int(sample_size * len(lst))
        return random.sample(lst, sample_size)
    else:
        raise TypeError("Sample size must be an integer or a float.")

def count_elements(lst: list) -> dict:
    """
    Count the occurrences of each element in the list.

    Parameters:
    - lst (list): The input list.

    Returns:
    dict: A dictionary where keys are unique elements from the list, and values are their counts.
    """
    return dict(Counter(lst))

def scale_list(lst: list, min_val: float = 1, max_val: float = 5) -> list:
    """
    Scale the values of a list to a specified range.

    Parameters:
    - lst (list): The input list of values to be scaled.
    - min_val (float): The minimum value of the output range (default is 1).
    - max_val (float): The maximum value of the output range (default is 5).

    Returns:
    - list: A new list with values scaled to the specified range.
    """
    min_w = min(lst)
    max_w = max(lst)
    scaled_w = []
    for x in lst:
        try:
            scaled_value = (x - min_w) / (max_w - min_w) * (max_val - min_val) + min_val
        except ZeroDivisionError:
            scaled_value = min_val
        scaled_w.append(scaled_value)
    return scaled_w


def df_scale_column(df: pd.DataFrame, col_to_scale: str, col_out: str, min_val: float, max_val: float) -> pd.DataFrame:
    """
    Scale values in a DataFrame column to a specified range.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - col_to_scale (str): The name of the column to be scaled.
    - col_out (str): The name of the new column to store scaled values.
    - min_val (float): The minimum value of the output range.
    - max_val (float): The maximum value of the output range.

    Returns:
    - pd.DataFrame: The DataFrame with a new column containing scaled values.
    """
    min_freq = df[col_to_scale].min()
    max_freq = df[col_to_scale].max()
    df[col_out] = df[col_to_scale].apply(lambda x: ((x - min_freq) / (max_freq - min_freq)) * (max_val - min_val) + min_val)
    return df

############################################################################
# ZIP HELPERS
############################################################################      
    
def zip_file(source_file_path: str, zip_file_path: str, name: str) -> str:
    """
    Zip a single file.

    Parameters:
    - source_file_path (str): Path to the file to be zipped.
    - zip_file_path (str): Path for the resulting zip file.
    - name (str): Name for the resulting zip file (without extension).

    Returns:
    str: Path to the resulting zip file.
    """
    file_path = os.path.join(zip_file_path, f"{name}.zip")
 
    with zipfile.ZipFile(file_path, 'w') as zip_file:
        # The second argument to `arcname` is used to set the name of the file inside the zip
        zip_file.write(source_file_path, arcname=os.path.basename(source_file_path))

    return file_path
    
def zip_folder(source_folder_path: str, zip_file_path: str, name: str) -> str:
    """
    Zip an entire folder.

    Parameters:
    - source_folder_path (str): Path to the folder to be zipped.
    - zip_file_path (str): Path for the resulting zip file.
    - name (str): Name for the resulting zip file (without extension).

    Returns:
    str: Path to the resulting zip file.
    """
    file_path = os.path.join(zip_file_path, f"{name}.zip")
    
    with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for foldername, subfolders, filenames in os.walk(source_folder_path):
            for filename in filenames:
                fpath = os.path.join(foldername, filename)
                arcname = os.path.relpath(fpath, source_folder_path)
                zip_file.write(fpath, arcname=arcname)
                
    return file_path

def unzip_file(zip_file_path: str, destination_path: str) -> None:
    """
    Unzip a zip file.

    Parameters:
    - zip_file_path (str): Path to the zip file to be unzipped.
    - destination_path (str): Path where the contents of the zip file will be extracted.

    Returns:
    None
    """
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(destination_path)
    

############################################################################
# Google Spreadsheets HELPERS
############################################################################   


def create_google_spreadsheet_client(credentials: str):
    """
    Create a Gspread client to interact with Google Sheets.

    Parameters:
    - credentials (str): Path to the JSON file containing Google Service Account credentials.

    Returns:
    gspread.Client: A client object for interacting with Google Sheets.
    """
    return gspread.service_account(filename=credentials)

def read_google_spreadsheet(client: gspread.Client, sheet_id: str, worksheet_name: str) -> pd.DataFrame:
    """
    Read data from a Google spreadsheet and return it as a DataFrame.

    Parameters:
    - client (gspread.Client): A Gspread client object authenticated with Google Sheets API.
    - sheet_id (str): The ID of the Google spreadsheet.
    - worksheet_name (str): The name of the worksheet within the spreadsheet.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the specified worksheet.
    """
    try:
        # Open the Google Spreadsheet by ID
        sheet = client.open_by_key(sheet_id)
        
        # Select a specific worksheet by name
        worksheet = sheet.worksheet(worksheet_name)
        
        # Get all values from the worksheet
        df = pd.DataFrame(worksheet.get_all_records())
        
        return df
    except exceptions.GoogleAuthError as e:
        print(f"Authentication error: {e}")
    except gspread.exceptions.APIError as e:
        print(f"API error: {e}")
    except gspread.exceptions.WorksheetNotFound as e:
        print(f"Worksheet not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def list_google_worksheets(client: gspread.Client, sheet_id: str) -> list:
    """
    Return a list of worksheet names for a spreadsheet ID.

    Parameters:
    - client (gspread.Client): A Gspread client object authenticated with Google Sheets API.
    - sheet_id (str): The ID of the Google spreadsheet.

    Returns:
    list: A list of worksheet names.
    """
    sheet = client.open_by_key(sheet_id)
    worksheet_obj = sheet.worksheets()
    worksheet_list = [sheet.title for sheet in worksheet_obj]
    return worksheet_list
    
def get_spreadsheet_permissions(client: gspread.Client, sheet_id: str) -> pd.DataFrame:
    """
    Return a DataFrame with the list of user email and type that can access the document.

    Parameters:
    - client (gspread.Client): A Gspread client object authenticated with Google Sheets API.
    - sheet_id (str): The ID of the Google spreadsheet.

    Returns:
    pd.DataFrame: A DataFrame containing the list of user email addresses and their access types.
    """
    sheet = client.open_by_key(sheet_id)
    permissions = sheet.list_permissions()
    user_list = [(user.get("emailAddress"), user.get("type")) for user in permissions if user.get("emailAddress") is not None]
    df = pd.DataFrame(user_list, columns=['email', 'type'])
    return df


def create_google_spreadsheet(client: gspread.Client, df: pd.DataFrame, filename: str, worksheet_name: str = "Sheet1") -> gspread.Spreadsheet:
    """
    Create a new Google spreadsheet and load a DataFrame into it.

    Parameters:
    - client (gspread.Client): A Gspread client object authenticated with Google Sheets API.
    - df (pd.DataFrame): The DataFrame to be loaded into the spreadsheet.
    - filename (str): The desired filename for the new spreadsheet.
    - worksheet_name (str, optional): The name of the worksheet within the spreadsheet. Defaults to "Sheet1".

    Returns:
    gspread.Spreadsheet: The created spreadsheet object.
    """
    spreadsheet = client.create(filename)
    worksheet = spreadsheet.sheet1
    if worksheet_name != "Sheet1":
        worksheet.update_title(worksheet_name)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    return spreadsheet

def share_google_spreadsheet(spreadsheet: gspread.Spreadsheet, email: str, user_type: str = "user", user_role: str = "writer", notify: bool = False, email_message: str = None, with_link: bool = False) -> gspread.Spreadsheet:
    """
    Share a spreadsheet with a user.

    Parameters:
    - spreadsheet (gspread.Spreadsheet): The Google spreadsheet object to be shared.
    - email (str): The email address of the user with whom the spreadsheet will be shared.
    - user_type (str, optional): The permission type for the user. Defaults to "user".
    - user_role (str, optional): The role assigned to the user. Defaults to "writer".
    - notify (bool, optional): Whether to notify the user about the sharing. Defaults to False.
    - email_message (str, optional): The message to include in the notification email.
    - with_link (bool, optional): Whether to include a link to the shared document in the notification email. Defaults to False.

    Returns:
    gspread.Spreadsheet: The updated spreadsheet object.
    """
    spreadsheet.share(email, perm_type=user_type, role=user_role, notify=notify, email_message=email_message, with_link=with_link)
    return spreadsheet

def generate_short_id(variables: dict) -> tuple[str, str]:
    """
    Generate an 8-character ID using a dictionary as input.

    Parameters:
    - variables (dict): A dictionary containing the variables to be serialized.

    Returns:
    tuple: A tuple containing the generated short ID and the serialized variables.
    """
    # Serialize variables into JSON string
    serialized_variables = json.dumps(variables, sort_keys=True)
    # Generate a hash of the serialized variables
    hash_value = hashlib.sha256(serialized_variables.encode()).hexdigest()
    # Take the first 8 characters of the hash as the short ID
    short_id = hash_value[:8]
    return short_id, serialized_variables

def df_transform_column_as_list(column: pd.Series) -> pd.Series:
    def transform(cell):
        if isinstance(cell, str):
            # Check if it's a list formatted as string, and convert to list
            if cell == "nan":
                values = []
            else:
                try:
                    values = ast.literal_eval(cell)
                except Exception as e:
                    # If it's a single URL as string, make it a list
                    values = [cell]
        elif isinstance(cell, (int, float, bool)):
            # Convert single value to list
            values = [cell]
        elif isinstance(cell, list):
            # If it's already a list, use it as is
            values = cell
        elif cell is None:
            values=[]
        else:
            values=[cell]
        return values

    return column.apply(transform)


def top_rows_per_category(df: pd.DataFrame, 
                          col_to_sort: str, 
                          col_to_gb: str, 
                          cols_to_keep: list[str], 
                          top_rows: int) -> pd.DataFrame:
    """
    Select top rows for each category in a dataframe
    """
    df_gb = (df.sort_values(by=col_to_sort, ascending=False)
                 .groupby(col_to_gb)
                 .apply(lambda group: group.head(top_rows))
                 .reset_index(drop=True)
                )[cols_to_keep]
    return df_gb

def format_number(number: int) -> str:
    """
    Function to format a number in K, M or B
    """
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return f"{number / 1000:.1f}K"
    elif number < 1000000000:
        return f"{number / 1000000:.1f}M"
    else:
        return f"{number / 1000000000:.1f}B"



def unrar_file(rar_file_path : str, output_dir : str) -> None:
    """
    Extracts a .rar file to the specified output directory using the unrar command.
    
    Parameters:
    rar_file_path (str): The path to the .rar file.
    output_dir (str): The directory where the contents should be extracted.
    
    Returns:
    None
    """
    try:
        # Ensure the output directory exists
        subprocess.run(['mkdir', '-p', output_dir], check=True)
        
        # Run the unrar command
        result = subprocess.run(['unrar', 'x', '-y', rar_file_path, output_dir], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the extraction was successful
        if result.returncode != 0:
            print(f"Extraction failed. Error: {result.stderr}")
            
    except Exception as e:
        print(f"An error occurred: {e}")