#Works like a  charm, opens up in foreground

import os
import time
import datetime
import subprocess

List_Parent_FLP_Folder = [
    r"C:\Users\Kfoen\Documents\Image-Line\FL Studio\Projects\FL 21 - projects\2024\CONSUME AFTER DARK"
    #r"C:\Users\Kfoen\Documents\Image-Line\FL Studio\Projects\FL 20 - projects\K2\2023",
    #r"C:\Users\Kfoen\Documents\Image-Line\FL Studio\Projects\FL 20 - projects\K2\2022"
]

Single_flp_Project_Path = r"C:\Users\Kfoen\Documents\Image-Line\FL Studio\Projects\FL 20 - projects\K2\New Kev\black butterfly.flp"
FL_Studio_Path = r"C:\Program Files\Image-Line\FL Studio 21"
Output_Folder_Path = r"C:\Users\Kfoen\Music\DropHere"
Processor_Type = "FL64.exe"


def get_file_paths(directory_paths):
    file_paths = []
    for directory_path in directory_paths:
        for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                file_paths.append(os.path.join(directory_path, filename))
    return file_paths

file_paths = get_file_paths(List_Parent_FLP_Folder)

today = datetime.date.today()
today_str = today.strftime("%d-%m-%Y")

for file_path in file_paths:
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%d-%m-%Y")
    if modified_time == today_str:
        Export_FLP_to_MP3 = f'cd {FL_Studio_Path} & {Processor_Type} /R /Emp3 "{file_path}" /O"{Output_Folder_Path}"'
        subprocess.call(Export_FLP_to_MP3, shell=True)

print("All modified FLP projects have been exported to: 💣",Output_Folder_Path )