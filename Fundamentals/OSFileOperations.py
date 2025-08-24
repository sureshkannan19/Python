import os
import shutil

#  Below command starting with ~ points USERHOME, hence output is C:\Users\SureshBabu/PycharmProjects/PythonProject/resources
folder_original = os.path.expanduser("~/PycharmProjects/PythonProject/resources")
folder_destination = os.path.expanduser("~/PycharmProjects/PythonProject/resources_replica")

for file in os.scandir(folder_original):
    if os.path.isfile(file):
        print("File:", file)
    elif os.path.isdir(file):
        print("Directory:", file)

if not os.path.isdir(folder_destination):
    print("Directory does not exist:", folder_destination)
    os.makedirs(folder_destination)

# moving only file's from one location to another
# os.path.join returns valid path(folder or file)
for file in os.scandir(folder_original):
    original_file_path = os.path.join(folder_original, file.name)
    destination_file_path = os.path.join(folder_destination, file.name)

    if not os.path.exists(destination_file_path):
        print("File does not exist:", destination_file_path, "creating file now...")
        # os.rename(original_file_path, destination_file_path)

        # both destination folder or file path is accepted
        shutil.move(original_file_path, folder_destination)
        print("File created successfully.")