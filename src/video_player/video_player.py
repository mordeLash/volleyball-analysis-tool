import cv2 
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
class video_player:
    def __init__(self,path,display):
        try:
            self.cap = cv2.VideoCapture(path)
            self.cap_metaData = {}
            self.cap_metaData["fps"] = self.cap.get(cv2.CAP_PROP_FPS)
            self.cap_metaData["frame count"] = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.cap_metaData["frame height"] = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.cap_metaData["frame width"] = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.display = display
            self.cur_frame = 0
        except Exception as e:
            print(f"Error: Error loading video: {str(e)}")
    


    def seek_frame(self,frame_number):
        if(frame_number<self.cap_metaData["frame count"]):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
            self.cur_frame=frame_number
            self.capload_frame_to_screen()

    def load_frame_to_screen(self):
        ret, frame = self.cap.read()
        if not ret:
            print(f"Error: Error loading video: Error reading frame")
            return
        screen_frame = self.frame_to_image(frame)
        self.display.setPixmap = screen_frame

    def frame_to_image(frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        image = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        #TODO scale image
        return QPixmap.fromImage(image)

    
        



        