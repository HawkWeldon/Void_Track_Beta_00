import cv2
import os
import moviepy.editor as mvp
os.system('cls')
def form(image_folder):
    video_name = 'D:/I.Research/VoidWrk/temp.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 10, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()
    clip=mvp.VideoFileClip("D:/I.Research/VoidWrk/temp.avi");
    clip.write_videofile("D:/I.Research/VoidWrk/Tracked.mp4");
    os.remove("D:/I.Research/VoidWrk/temp.avi")