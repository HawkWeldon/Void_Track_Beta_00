import cv2
import os
def video(current_directory):
    vid_path = os.path.join(current_directory, 'vid/vid.mp4')
    vid = cv2.VideoCapture(vid_path)
    success,image = vid.read()
    c = 0
    while success:
      os.system('cls')
      half_path = str('Op/Frame%05d.png' % c)
      cv2.imwrite(os.path.join(current_directory, half_path), image)
      success,image = vid.read()
      c = c + 1
    os.system('cls')
    print('Break down done')
    return c