import wave
import other
import pyaudio
import threading

from datetime import datetime

class AudioRecordHandler():
    
    def __init__(self, name):
        self.frames = []
        self.fs = 44100 # number of frames per second
        self.name = name
        self.chunk = 1024 # chunk size of 1024 samples
        self.channels = 2 #stereo
        self.format = pyaudio.paInt16 #sample format
        self.port = pyaudio.PyAudio() #initialize PyAudio object
        self.port.get_default_host_api_info()
        self.stream = self.port.open(format=self.format, channels=self.channels, rate=self.fs, frames_per_buffer=self.chunk, input=True)

    def start_recording(self, duration):             
        self.duration = duration
        self.thread = threading.Thread(target=self.record_frames)
        self.thread_is_running = True
        self.thread.start()

    def record_frames(self):
        self.start = datetime.now()
        # recording for [duration] time (in seconds)
        while ((datetime.now() - self.start).total_seconds() < self.duration) and (self.thread_is_running):
            self.record_frame()
        self.save_audio()

    def record_frame(self):
        # reading the next sound frame, and append it to frames list
        data = self.stream.read(self.chunk)
        # calculating decibels of this frame
        f=open('db_capture.txt','a')
        f.write(f'[{(datetime.now() - self.start).total_seconds()}]:{other.decibels(data)} db')
        f.close()
        self.frames.append(data)

    def save_audio(self):
        # creating | reseting file for wave sound
        wf = wave.open(self.name + '.wav', 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.port.get_sample_size(self.format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def discard(self):
        # discarding all resources & threads
        if self.thread.is_alive():
            self.thread_is_running = False
        self.stream.start_stream()
        self.stream.close()
        self.port.terminate()

if __name__ == '__main__':
    print('Try main.py...')