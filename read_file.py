import pandas as pd
import os
import shutil

file = 'Train.xlsx'
data = pd.read_excel(file)


imgs=[]
for i in range(0,data.shape[0]):
    I=data['Pics'].iloc[i].split("\\")[-1]
    imgs.append(I)

data['Images']=imgs

Folders=list(data['Folders'].unique())

root_dir=os.getcwd()

Train_dir=os.path.join(root_dir,"Train")

os.chdir(Train_dir)

for folder in Folders:
    try:
        os.makedirs(folder)
    except OSError:
        pass

    for i in range(0,data.shape[0]):
        if data.iloc[i]['Folders']==folder:
            shutil.copy(os.path.join(Train_dir,data["Images"][i]),os.path.join(Train_dir,folder))