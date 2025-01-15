"""
Author: Saba Geppetto
"""
 
import hashlib
import os
 
import tqdm
 
DEFAULT_PATH = r""
 
 
def create_file_hash(file_path: str) -> str:
    """
    create file hash for the given file path if it exists.
 
    :param file_path:
    :return:
    """
    if not os.path.exists(path=file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
 
    with open(file=file_path, mode="rb") as file:
        return hashlib.md5(file.read()).hexdigest()
 
 
def create_hash_table(directory: str) -> dict:
    hash_table = {}
 
    files_to_compare = []
 
    for root, _, files in os.walk(top=directory):
        for file in files:
            # this is stupid, I know, this is for the progress bar.
            files_to_compare.append(os.path.join(root, file))
 
    for file in tqdm.tqdm(iterable=files_to_compare):
        file_hash = create_file_hash(file_path=file)
 
        if file_hash in hash_table:
            hash_table[file_hash].append(file)
 
        else:
            hash_table[file_hash] = [file]
 
    return hash_table
 
 
def process_hash_table(hash_table: dict) -> dict:
    """
    find the duplicate files from the hash table.
 
    :param hash_table:
 
    :return:
    """
    # drop all non duplicate files.
    return {
        k: v for k, v in hash_table.items() if len(v) > 1
    }
 
 
def count_duplicates(processed_hash_table: dict) -> int:
    """
    Count the number of duplicate files.
 
    :param processed_hash_table:
    :return:
    """
    return sum(len(v) - 1 for v in processed_hash_table.values())
 
 
def get_directory_from_user() -> str:
    """
    Get the directory from the user.
 
    :return:
    """
    directory = input("Enter the directory to search for duplicate files: ")
 
    if not os.path.exists(path=directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
 
    return directory
 
 
def main():
    """
    Main function.
 
    :return:
    """
    # ask the user for the directory to search for duplicate files.
    directory = get_directory_from_user()
 
    # create the hash table for the given directory.
    hash_table = create_hash_table(directory=directory)
 
    # process the hash table to find the duplicate files.
    duplicate_files = process_hash_table(hash_table=hash_table)
 
    # count the number of duplicate files.
    num_duplicates = count_duplicates(processed_hash_table=duplicate_files)
 
    print(f"Number of duplicate files: {num_duplicates}")
 
 
if __name__ == "__main__":
    main()
 
