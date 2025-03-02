import cv2 
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import time

"""class to play videos using open-cv"""
class VideoPlayer():
    def __init__(self,path,display):
        try:
            self.cap = cv2.VideoCapture(path)
            self.cap_metaData = {}
            self.cap_metaData["fps"] = self.cap.get(cv2.CAP_PROP_FPS)
            self.cap_metaData["frame count"] = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.cap_metaData["frame height"] = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.cap_metaData["frame width"] = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.display = display
            self.current_frame = 0
            self.delay_time = 1/self.cap_metaData["fps"] 
            self.playing = False
        except Exception as e:
            print(f"Error: Error loading video: {str(e)}")
    

    def play(self):
        """play video frame after frame at the video frame rate"""
        self.playing = True
        while self.current_frame < self.cap_metaData["frame count"] and self.playing:
            frame_start_time = time.time()
            self.current_frame+=1
            self.seek_frame(self.current_frame)
            frame_end_time = time.time()
            frame_load_time = frame_end_time-frame_start_time
            if(frame_load_time<self.delay_time):
                time.sleep(self.delay_time-frame_load_time)
            else:
                print("Error: play time is not real time")


    def pause(self):
        self.playing=False

    def seek_frame(self,frame_number):
        """display specific frame from video"""
        if(frame_number<self.cap_metaData["frame count"]):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
            self.cur_frame=frame_number
            self.load_frame_to_screen()

    def load_frame_to_screen(self):
        """load current frame from video to screen"""
        ret, frame = self.cap.read()
        if not ret:
            print(f"Error: Error loading video: Error reading frame")
            return
        screen_frame = self.frame_to_image(frame)
        self.display.setPixmap = screen_frame

    def frame_to_image(frame):
        """convert open-cv frame to image"""
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        image = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        #TODO scale image
        return QPixmap.fromImage(image)

    
        



        