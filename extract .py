import os
import zipfile

# set the parent directory where the subdirectories are located
parent_directory = "C:/Users/username/Desktop/extracted_files"

# iterate over each subdirectory in the parent directory
for subdir_name in os.listdir(parent_directory):
    subdir_path = os.path.join(parent_directory, subdir_name)
    if os.path.isdir(subdir_path):
        # create a new output subdirectory with the same name as the input subdirectory
        output_subdir_path = os.path.join(subdir_path, 'extracted_files')
        os.makedirs(output_subdir_path, exist_ok=True)

        # iterate over each ASiC-E file in the subdirectory
        for filename in os.listdir(subdir_path):
            if filename.endswith('.asice'):
                with zipfile.ZipFile(os.path.join(subdir_path, filename)) as zf:
                    for member in zf.infolist():
                        # check if the member file is a PDF or DOCX file
                        if member.filename.endswith('.pdf') or member.filename.endswith('.docx'):
                            # extract the file to the output directory
                            zf.extract(member, output_subdir_path)
