import os
import argparse
import pprint
from collections import defaultdict


def get_file_name_path_size_list(dir_path):
    file_name_path_size_list = list()
    for dir_name, sub_dir_names, file_names in os.walk(dir_path):
        for file_name in file_names:
            file_path = os.path.join(dir_name, file_name)
            file_size = os.path.getsize(file_path)
            file_name_path_size_list.append(((file_name, file_size), file_path))
    return file_name_path_size_list


def merge_duplicates_paths(file_name_path_size_list):
    merged_duplicates_paths_list = defaultdict(list)
    for key, path in file_name_path_size_list:
        merged_duplicates_paths_list[key].append(path)
    return merged_duplicates_paths_list


def get_duplicate_files_list(merged_duplicates_paths_list):
    duplicate_files_list = list()
    for path in merged_duplicates_paths_list.values():
        if len(path) > 1:
            duplicate_files_list.append(path)
    return duplicate_files_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path')
    args = parser.parse_args()
    file_name_path_size_list = get_file_name_path_size_list(args.dir_path)
    merged_duplicates_paths_list = merge_duplicates_paths(file_name_path_size_list)
    duplicate_files_list = get_duplicate_files_list(merged_duplicates_paths_list)
    pprint.pprint(duplicate_files_list)




