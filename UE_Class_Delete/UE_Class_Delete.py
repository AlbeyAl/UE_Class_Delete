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


def delete_file(filepath):
    '''Simply deletes a file at the path described in params. '''
    os.remove(filepath)

def open_file(filepath):
    ''' Opens a file using webbrowser.open() to open a file in an external
    program, paying attention to OS.'''
    webbrowser.open(filepath)



