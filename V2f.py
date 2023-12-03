import cv2
import os
def video():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    vid_path = os.path.join(current_directory, 'vid/vid.mp4')
    vid = cv2.VideoCapture(vid_path)
    success,image = vid.read()
    c = 0
    while success:
      os.system('cls')
      cv2.imwrite('D:/I.Research/VoidWrk/Op/Frame%05d.png' % c, image)
      success,image = vid.read()
      c = c + 1
    os.system('cls')
    print('Break down done')
    return c