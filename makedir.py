import shutil

import os
#shutil.move(src = 'G:\source\pics' , dst ='G:\destination\ ' )

def create_folder() :
    driver = input('''SSD (C) ,WORK (I), ENTERTAINMENT (H), STUDIES (G), LOCAL DISK(D) . Enter the extension .
    Select the letter : ''')
    path1 = driver+':'
    def new_folder (path) :
        dir = input('Want to create a folder here ? [y/n] : ')
        if dir == 'y' :
            nam = input('Enter the name of the folder : ')
            os.mkdir(os.path.join(path,nam))
        else :
            file = list(os.listdir(path))
            if file == [] :
                print('No folders in this directory')
            else :
                for i in file :
                    print(i)
                ext = input('Select the directory in which the folder must be created : ')
                new_path = os.path.join(path, ext)
                new_folder(new_path)
    new_folder(path1)

create_folder()