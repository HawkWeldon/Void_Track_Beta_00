from PIL import Image
from flark import main
from rearg import rearange 
##################################################################################################################################################
def ant(image_path,output_path,idx,model,):
    df = main(image_path,model)
    mid_points = df.splitlines()
    lenght = len(mid_points)
    mid_points = rearange(mid_points, lenght, idx)
    input_image = Image.open(image_path)
    pixel_map = input_image.load()
    width, height = input_image.size
    wd = int(width/100)
    c = 0 
    Flag = 0
    color = [(255,20,20), (20,255,20), (20,20,255), (255, 255, 255), (34, 67, 19), (255, 255, 255), (56, 88, 199), (3, 46, 200)]
    for i in range(lenght):
        start = mid_points[i].split()
        if (Flag == 1):
            Flag = 0
            c = c + 1
            continue
        if (i < lenght-1):
            if(mid_points[i]==mid_points[i+1]):
                Flag = 1
        for j in range(wd):
            for k in range(wd):
                pixel_map[int(float(start[0]))-j,int(float(start[1]))-k] = color[c]
                pixel_map[int(float(start[0]))+j,int(float(start[1]))+k] = color[c]
                pixel_map[int(float(start[0]))-k,int(float(start[1]))+j] = color[c]
                pixel_map[int(float(start[0]))+k,int(float(start[1]))-j] = color[c]
        c = c + 1
    input_image.save(output_path, format="png")
    return mid_points
##################################################################################################################################################