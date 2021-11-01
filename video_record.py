import cv2
import pyautogui
import threading
import numpy as np

class VideoRecordHandler():

    def __init__(self, name, framerate=20):
        self.name = name
        self.framerate = framerate
        self.size = pyautogui.size()  # gets the current screen rez

        self.codec = cv2.VideoWriter_fourcc(*'mp4v')
        self.record = cv2.VideoWriter(
            f"{self.name}.mp4", self.codec, self.framerate, (self.size))

    def record_frame(self):
        frame = np.array(pyautogui.screenshot())
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.record.write(frame)

    def record_frames(self):
        for i in range(int(self.duration * self.framerate)):
            self.record_frame()

    def start_recording(self, duration=60):
        self.duration = duration
        self.thread = threading.Thread(target=self.record_frames)
        self.thread_is_running = True
        self.thread.start()

    def discard(self):
        if self.thread.is_alive():
            self.thread_is_running = False
        self.record.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Try main.py...')
