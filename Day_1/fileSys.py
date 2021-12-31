# read contents of file at any locations
import os
print(os.getcwd())
# \\ for connecting the path
file=open(r'e:\\Git_Repos\\Python\\Day_1\\test.txt')
print(file.read())
file.close()

