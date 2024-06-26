# Log to Trajectory and Extended XYZ Converter

This Python script automates the conversion of Gaussian log files (.log) to both ASE trajectory (.traj) and extended XYZ (.extxyz) formats. The output is organized into two subdirectories within a main `output` directory.

## Directory Structure After Running Script

- `output/`: Main directory for converted files.
  - `traj_files/`: Contains the converted .traj files.
  - `extxyz_files/`: Contains the converted .extxyz files.

## Prerequisites

- Python 3
- Atomic Simulation Environment (ASE) library

Make sure Python and ASE are installed. You can install ASE with pip:

```
pip install ase
```

## How to Use

1. Place your Gaussian .log files in a directory.
2. Run the script using one of the two modes:
   - **File Mode**: To convert a single .log file.
   - **Directory Mode**: To convert all .log files in a specified directory.

### Command Syntax

- For a single file:
  ```
  python main.py -mode file /path/to/your/file.log
  ```

- For a directory:
  ```
  python main.py -mode directory /path/to/your/directory
  ```

### Output

- The script creates an `output` directory in the script's running directory.
- Inside `output`, two subdirectories `traj_files` and `extxyz_files` are created, containing the converted files.

## Notes

- Ensure the provided path is correct and points to either a valid .log file or a directory containing .log files.
- The script does not process files in subdirectories when the directory mode is used.
