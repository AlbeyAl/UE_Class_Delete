import os
from shutil import rmtree
import webbrowser

def find_directory(name, source):
    ''' Finds and returns first directory found in source by name. '''
    for dirpath, dirnames, filenames in os.walk(source):
        for dirname in dirnames:
            if dirname == name:
                dirname = os.path.join(dirpath, dirname)
                return dirname

def find_file(name, extension, source):
    ''' Finds and returns first file found in source by name and extension. '''
    for dirpath, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename == name + extension:
                filename = os.path.join (dirpath, filename)
                return filename

def delete_directory(filepath):
    ''' Deletes a folder and the directory tree following it. '''
    os.rmdir(filepath)

def delete_file(filepath):
    '''Simply deletes a file at the path described in params. '''
    os.remove(filepath)

def open_file(filepath):
    ''' Opens a file using webbrowser.open() to open a file in an external
    program, paying attention to OS.'''
    webbrowser.open(filepath)

def display_error(text):
    print("Error: " + text)

def delete_class():
    # grab the class name to delete
    classname = input("Please enter the name of the class you're trying to delete: ")

    # clear console
    os.system('cls')
    print("Attempting to find and delete " + classname + " class...")

    fileCPPpath = find_file(classname, ".cpp", projectdir)
    fileHpath = find_file(classname, ".h", projectdir)
    binariespath = find_directory("Binaries", projectdir)

    error = False;

    if fileCPPpath != None:
        delete_file(fileCPPpath)
    else:
        display_error("Class .cpp file not found.")
        print(fileCPPpath)
        error = True

    if fileHpath != None:
        delete_file(fileHpath)
    else:
        display_error("Class .h file not found.")
        error = True

#'''    if binariespath != None:
#        delete_file(binariespath)
#    else:
#        display_error("Binaries folder not found.")
#        error = True

    if error == True:
        display_error("Failed to delete class. Please check file and directory spelling.")
    else:
        print("Class deleted successfully!")
    
    print("")
    i = input("Type 1 to continue deleting, or nothing to stop deleting classes: ")

    if i == 1:
        os.system('cls')
        delete_class()

    os.system('cls')

projectname = input("Please enter the name of your project: ")

# grab the directory of the project
projectdir = find_directory(projectname, input("Please enter the path to your projects folder for Unreal Engine: "))

delete_class()

open_file(os.path.join(projectdir, projectname + ".uproject"))
open_file(os.path.join(projectdir, projectname + ".sln"))


