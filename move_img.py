import shutil

import os

root_dir = 'G:/NKV Study/Github/Image-classification-/Images'
imgs = list(os.listdir(root_dir))

#moving files
#shutil.move(src = 'G:\source\pics' , dst ='G:\destination\ ' )

#copying images
for i in imgs :
    shutil.copy(src = 'G:/NKV Study/Github/Image-classification-/Images'+'//' + i , dst ='G:/NKV Study/Github/Image-classification-/Train/'  )