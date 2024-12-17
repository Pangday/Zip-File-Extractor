import zipfile
import os
import shutil

def unzip_all_folders(source_folder):
    # Loop through all files in the source folder
    for item in os.listdir(source_folder):
        if item.endswith(".zip"):  # Check if the file is a zip file
            file_path = os.path.join(source_folder, item)
            folder_name = os.path.splitext(item)[0]  # Get the zip file name without extension
            extract_folder = os.path.join(source_folder, folder_name)

            # Create the directory if it doesn't exist
            os.makedirs(extract_folder, exist_ok=True)

            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all contents into the respective unzip folder
                zip_ref.extractall(extract_folder)
            print(f"Extracted: {item} into {extract_folder}")

def copy_pcf_pdf_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Walk through the source folder to find .pcf and .pdf files
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.pcf') or file.endswith('.pdf'):  # Check for .pcf or .pdf
                file_path = os.path.join(root, file)
                # Copy the file to the target folder
                shutil.copy(file_path, destination_folder)
                print(f"Copied: {file} to {destination_folder}")

# Example usage:
source_folder = r'C:\Users\ZIYING.PANG\OneDrive - Seatrium Ltd\Production Engineering & Scheduling\unzip_folders'  # Replace with your folder path
destination_folder = r'C:\Users\ZIYING.PANG\OneDrive - Seatrium Ltd\Production Engineering & Scheduling\process_pcf'  # Replace with your desired destination folder

# First, unzip all the folders
unzip_all_folders(source_folder)

# Then, copy the .pcf and .pdf files to the new folder
copy_pcf_pdf_files(source_folder, destination_folder)
