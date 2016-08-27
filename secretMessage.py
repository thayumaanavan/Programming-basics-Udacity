import os

def rename_files():
    file_list=os.listdir("./prank")
    os.chdir("./prank")

    for file_name in file_list:
        print("old name: "+file_name+";New name: "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))

rename_files()