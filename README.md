Description

This script is designed to extract PDF and DOCX files from ASiC-E files located in a specified directory and its subdirectories. It creates a new output subdirectory with the same name as the input subdirectory for each ASiC-E file and saves the extracted files in the output directory.

Requirements

Python 3.x
The zipfile module

Usage

Save the script to a local directory.
Open the script in a Python IDE or text editor.
Modify the parent_directory variable on line 5 to specify the parent directory where the subdirectories with ASiC-E files are located.
Run the script.
Output
The extracted PDF and DOCX files will be saved in a new subdirectory named extracted_files within each input subdirectory containing ASiC-E files.

Notes

This script only extracts PDF and DOCX files from ASiC-E files. If you need to extract other file types, modify the code accordingly.
This script only works for ASiC-E files. If you need to extract files from other types of archive files, modify the code accordingly.
This script does not handle errors or exceptions related to file extraction. If an error occurs during the extraction process, the script will terminate.
