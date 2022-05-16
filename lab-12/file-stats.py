import os
def stats(file_path):
    file = open(file_path, "r")
    file_data = file.read()
    file_characters = len(file_data)
    file_lines = int(sum(1 for line in file_data) / 10)
    file_words = len(file_data.split())

stats(os.path.expanduser('~') + "\\src\\python-programming\\lab-12\\test.txt")
