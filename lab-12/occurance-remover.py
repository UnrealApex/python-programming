# TODO: make sure that program does not overwrite file contents
import os
def occurance_remover(file_path, removal_string):
    target_file = open(file_path, "r+")
    occurances = target_file.read().count(removal_string)
    if removal_string in target_file.read():
       removal_string = removal_string.replace(removal_string, "")
    target_file.close()
    print(f"Removed {occurances} of {removal_string} from {os.path.basename(file_path)}")

    
occurance_remover(r"C:\Users\s158658\src\python-programming\lab-12\test.txt", "foo")
