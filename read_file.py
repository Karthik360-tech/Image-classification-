import pandas as pd
import os
import shutil

file = 'G:/NKV Study/Project_1.xlsx'
data = pd.read_excel(file)
pics = []
for i in range(4) :
    pics.append(data['Pics'][i].split(","))
print(pics)

folders = []
for i in range(4) :
    folders.append(data['Folders'][i].split(","))

print(folders)

count = 0
d = {} #Empty dictionary to add values into

for i in pics :
    for j in i :
        d[count] = str(j)
    count+=1
print(d)
Folders=list(data['Folders'].unique())
os.chdir("G:\\destination\\new1")
for folder in Folders:
    os.mkdir(folder)
    for i in range(0,data.shape[0]):
        if data.iloc[i]['Folder']==folder:
            shutil.move(os.path.join())