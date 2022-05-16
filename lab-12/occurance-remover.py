import os

def occurance_remover(file_path, removal_string):
    occurances = open(file_path, "r").read().count(removal_string)
    # Read in the file
    with open(file_path, "r") as file:
      filedata = file.read()

    # Remove the string given from the file
    filedata = filedata.replace(removal_string, "")

    # Write the contents to the file without the removal strings
    with open(file_path, 'w') as file:
      file.write(filedata)
    file.close()
    print(f"Removed {occurances} {'occurances' if (occurances != 1) else 'occurance'} of {removal_string} from {os.path.basename(file_path)}")
    
occurance_remover(os.path.expanduser('~') + "\\src\\python-programming\\lab-12\\test.txt", "foo")
