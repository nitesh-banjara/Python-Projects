""" r = open any file to read 
w = open file to write 
a = open for writing and adding at the end of the fire if it exist 
r+ = read and overwrite and pointer at start 
w+ = read and overwrite trumcate 
a+ = read and append from end"""

# f = open("hi.txt","r")


# line0 =f.read()
# line2 =f.read()
# print(line0)
# print(line2)

# f.close

# f = open("hi.txt","w")

# f.write("Hey this is the mmost handsome guy ")

# f = open("hi.txt","a")

# f.write("\n He is not that good bro ")

# with open("hi.txt","r") as f:
#     data = f.read()

# with open("hi.txt","w") as f:
#     data = f.write("My name is Nitesh Banjara ")

import os
os.remove("aaa.txt")# to remove any file 
