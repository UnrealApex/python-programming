import random
import os

def random_file(file_path):
    file_write = open(file_path, "a+")
    file_read = open(file_path, "r")
    for i in range(100):
        file_write.write(f" {str(random.randint(0, 100))}  ")
    print(file_read.read())
    open(file_path).close()

random_file(os.path.expanduser('~') + "\\src\\python-programming\\lab-12\\test.txt")
