import os 
import shutil 


def matching():
#creating an array list of all the static ID's
    id_list = ['00P4000000c0ea8EAA', '00P4000000c0eZAEAY', '00P4000000c0eZKEAY', '00P4000000c0eZtEAI', '00P4000000c0eZyEAI']

#opening a file to write in
    matching_file = open('matching_file.txt', 'w')

#using a nested for loop to loop through the filenames in the directory while also looping through the file names in the list
#if the filename is the same as one of the ones in the static list then move it
    for files in os.listdir("C:/Users/rjbri/OneDrive/Python/Intern/id_files"):
        for f in id_list:
            if f in files:
                matching_file.write(files+'\n')
                #creating a source join and joinging the mathcing files into the source to be moved into the destination
                src = os.path.join("C:/Users/rjbri/OneDrive/Python/Intern/id_files", f)
                dest = os.path.join("C:/Users/rjbri/OneDrive/Python/Intern/matching_folder", f)
                shutil.move(src, dest)

 #closing file            
    matching_file.close()

def change_filetype():
    #iterating over all the files in the directory
    directory_path = "C:/Users/rjbri/OneDrive/Python/Intern/matching_folder"
    file_types = ['PDF', 'JPG', 'PNG', 'MSG', 'XLS', 'DOCX', 'XLSX', 'JPEG', 'CSV', 'SNOTE', 'TIF', 'PPTX']

    # Iterating over all the files in the directory
    for files in os.listdir(directory_path):
        # Joining a full file path to make it usable
        path = os.path.join(directory_path, files)
        if os.path.isfile(path):  # Checking that the path is a file
            try:  # Attempting to open and read a file
                with open(path, 'r', encoding='utf-8', errors='ignore') as file:  # Reading a file as file and encoding it to utf-8 and making sure to ignore errors while decoding
                    first_line = file.readline().strip() #stripping the white spaces from the line
                    for extension in file_types: #checking every extension from the file in the file types list
                        if extension in first_line:
                            name, _ = os.path.splitext(files)#splitting the name and the old extension  
                            new_name = name + '.' + extension.lower()#creating a new name with new extension
                            new_path = os.path.join(directory_path, new_name)#joining a new path
                            file.close() #closing file so it does not iterate over an open one
                            break
                    else:
                        continue  # If no extension was found, skip renaming
                    os.rename(path, new_path)
            except Exception as e:#blockign catches and printing an error if one of the files is not readable
                print(f"Error reading {files}: {e}")
   
def main():
    matching()
    change_filetype()

main()

                    
""" new_name = name + '.'+ extensions
                            new_path = os.path.join(directory, new_name)
                            file.close()
                            os.rename(path, new_path) """ 