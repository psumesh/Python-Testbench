#This file is created by Umesh Prasad
#email   : spumesh@outlook.com


from shutil import rmtree
from os import path, remove, mkdir, chdir, listdir

def Temporary_file_setup():


    if path.isdir('./__pycache__'):
         rmtree('__pycache__')
   
    if path.isdir('./sim_build'):
         rmtree('sim_build')
   
    if path.exists('results.xml'):
         remove('results.xml')

    files_in_dir   = listdir()
    filtered_files = [file for file in files_in_dir if file.endswith('.vcd')]
    for file in filtered_files:
         path_to_file = path.join(file)
         remove(path_to_file) 


def log_directory_setup(f_name = 'unknown_Testfolder'):
    
    if not path.isdir('./Testcases_logs'):
       mkdir('./Testcases_logs')
       chdir('./Testcases_logs')

