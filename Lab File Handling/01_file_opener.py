import os

file_path = r'C:\Users\lifet\Documents\GitHub\Python-Advanced\Lab File Handling'

if os.path.exists(file_path):
    print('File found')
else:
    print('File not found')
