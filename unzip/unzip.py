import zipfile



zip_file_path = input("What is the path to your zipfile?: ")
zip_file_to = input ("Where do you wanna have your zipfile? :")

zip_file = zipfile.ZipFile(zip_file_path, 'r')
zip_file.extractall(zip_file_to)
zip_file.close()