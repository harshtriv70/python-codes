# write a python program to print the content of a directory using the os module 
import os

def print_directory_contents(path): 
    # Check if the given path is a directory
    if os.path.isdir(path):
        # List all the files and directories in the given path              
        contents = os.listdir(path)              
        print(f"Contents of '{path}':")              
        for item in contents:
            print(item)              
    else:
        print(f"The path '{path}' is not a valid directory.")              

# Example usage
directory_path = '/Users/HARSH TRIVEDI/Documents'  # Replace with your directory path
print_directory_contents(directory_path)              
