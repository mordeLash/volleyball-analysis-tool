import sys
from PyQt5.QtWidgets import ( # type: ignore
    QApplication, QMainWindow, QWidget, QPushButton,
    QSlider, QVBoxLayout, QLabel, QFileDialog
)
from PyQt5.QtCore import Qt # type: ignore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Volleyball Analysis GUI")
        self.resize(800, 600)  # Initial window size; window is resizable by default

        # Central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Load Video button
        self.load_video_button = QPushButton("Load Video")
        self.load_video_button.clicked.connect(self.load_video)
        self.layout.addWidget(self.load_video_button)

        # Label to show video load status
        self.video_status_label = QLabel("No video loaded")
        self.layout.addWidget(self.video_status_label)

        # Slider for video navigation (hidden until a video is loaded)
        self.video_slider = QSlider(Qt.Horizontal)
        self.video_slider.setMinimum(0)
        self.video_slider.setMaximum(100)  # Placeholder range
        self.video_slider.setValue(0)
        self.video_slider.hide()  # Hidden until video is loaded
        self.layout.addWidget(self.video_slider)
        

        # Play/Pause button (hidden until a video is loaded)
        self.play_pause_button = QPushButton("Play")
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        self.play_pause_button.hide()  # Hidden until video is loaded
        self.layout.addWidget(self.play_pause_button)

        # State variable to track play/pause state
        self.is_playing = False

    def load_video(self):
        """Opens a file dialog to load a video and updates the GUI."""
        video_file, _ = QFileDialog.getOpenFileName(
            self, "Open Video File", "", "Video Files (*.mp4 *.mov *.avi *.*)"
        )
        if video_file:
            # Update status label and show slider and play/pause button
            self.video_status_label.setText(f"Video Loaded: {video_file}")
            self.video_slider.show()
            self.play_pause_button.show()

            # (Optional) Set slider range based on video duration here
            self.video_slider.setMinimum(0)
            self.video_slider.setMaximum(100)
            self.video_slider.setValue(0)

            # Reset play/pause button state
            self.is_playing = False
            self.play_pause_button.setText("Play")

    def toggle_play_pause(self):
        """Toggles between play and pause states."""
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.play_pause_button.setText("Pause")
            # Insert video playback code here if needed
        else:
            self.play_pause_button.setText("Play")
            # Insert code to pause the video here

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
