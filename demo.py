"""
** Python Delete File

- Delete a File
    - To delete a file, you must import the OS module, and run its os.remove() function
 """
import os
# os.remove("myfile.txt")

# Check if file Exist
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

# Delete Folder
os.rmdir("folder")