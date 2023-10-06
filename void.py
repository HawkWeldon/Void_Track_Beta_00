import torch
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_directory, 'model/model.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
from anotate import ant
from vid_frm import form
import V2f
file = open("temp.txt","r+")
file.truncate(0)
file.close()
no_frm = V2f.video()
print ("no of fromes :"+str(no_frm))
idx = 0
while ( 1==1 ):
    print("#"*150)
    image_path = 'D:/I.Research/VoidWrk/Op/Frame%05d.png'%idx
    out_path = 'D:/I.Research/VoidWrk/Anotated/Anotated%05d.png'%idx
    if os.path.isfile(image_path) == False:
            break
    print("given frame:"+str(idx+1))
    inptx = ant(image_path,out_path,idx,model)
    idx = idx + 1
form('D:/I.Research/VoidWrk/Anotated')