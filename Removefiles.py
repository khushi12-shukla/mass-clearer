from importlib.machinery import PathFinder
import time
import os
import shutil

def main():

    deleted_folders_count = 0
    deleted_files_count = 0

    path= input("want to clear information of 30 days prior? you are in the best place just type the path of the folder over here")
    days=30

    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                deleted_folders_count += 1

                break
            else:

                for folder in folders:

                    folder_path = os.path.join(root_folder,folder)

                    if seconds >=get_file_or_folder_age(folder_path):

                        remove_folder(folder_path)
                        deleted_folders_count += 1 
                
                for file in files:

                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1
        else:

            if seconds >= get_file_or_folder_age(path):

                remove_file(path)
                deleted_files_count += 1
    else:

        print(f'"{path}" is not found. Please check if you have written it incorrectly')
        deleted_files_count += 1

print(f"The number of useless folders deleted are {deleted_folders_count}")
print(f"The number of useless files deleted are {deleted_files_count}")

def remove_folder(path):

    if not shutil.rmtree(path):

        print(f"{path} is removed successfully")
    
    else:

        print(f"We are not able to delete the"+ path)

def remove_file(path):

    if not os.remove(path):

        print(f"{path} is discarded for ever")
    else:

        print("Sorry, but we are not able to delete"+path)

def get_file_or_folder_age(path):

    ctime=os.stat(path).st_ctime

    return ctime

if __name__ == '__main__':
    main()