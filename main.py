import os
import sys
from ase.io import read, write

def ensure_directories_exist():
    base_output_directory = os.path.join(os.getcwd(), 'output')
    traj_directory = os.path.join(base_output_directory, 'traj_files')
    extxyz_directory = os.path.join(base_output_directory, 'extxyz_files')
    
    os.makedirs(traj_directory, exist_ok=True)
    os.makedirs(extxyz_directory, exist_ok=True)
    
    return traj_directory, extxyz_directory

def process_file(file_path, traj_directory, extxyz_directory):
    if file_path.endswith('.log'):
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        traj_file_path = os.path.join(traj_directory, base_name + '.traj')
        extxyz_file_path = os.path.join(extxyz_directory, base_name + '.extxyz')

        structures = read(file_path, index=':')
        write(traj_file_path, structures)
        write(extxyz_file_path, structures)
        print(f"Processed: {file_path}\n  -> {traj_file_path}\n  -> {extxyz_file_path}")

def process_directory(directory_path, traj_directory, extxyz_directory):
    for filename in os.listdir(directory_path):
        if filename.endswith('.log'):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path, traj_directory, extxyz_directory)

if __name__ == "__main__":
    if len(sys.argv) < 4 or sys.argv[1] != '-mode':
        print("Usage: python main.py -mode [file|directory] /path/to/log_file_or_directory")
    else:
        mode = sys.argv[2]
        path = sys.argv[3]  # Correctly assign the path from the arguments
        traj_directory, extxyz_directory = ensure_directories_exist()

        if mode == 'file':
            if os.path.isfile(path):
                process_file(path, traj_directory, extxyz_directory)
            else:
                print(f"The specified path does not point to a file: {path}")
        elif mode == 'directory':
            if os.path.isdir(path):
                process_directory(path, traj_directory, extxyz_directory)
            else:
                print(f"The specified path does not point to a directory: {path}")
        else:
            print("Invalid mode. Use 'file' for processing a single file or 'directory' for processing all files in a directory.")

