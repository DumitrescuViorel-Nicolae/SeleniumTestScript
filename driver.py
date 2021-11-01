import video_record
import audio_record

from os import mkdir
from os.path import exists
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
from os.path import dirname

PATH = dirname(sys.argv[0]) + '\\'

class SeleniumHandler():

    def __init__(self):
        self.driver = self.create_new_driver()
        self.navigate()

    def start_recordings(self, filename, duration):
        if not exists(PATH+filename):
            mkdir(PATH+filename)
        a_recorder = audio_record.AudioRecordHandler(filename+'\\'+filename)
        v_recorder = video_record.VideoRecordHandler(filename+'\\'+filename)
        a_recorder.start_recording(duration)
        v_recorder.start_recording(duration)
        a_recorder.thread.join()
        v_recorder.thread.join()
        a_recorder.discard()
        v_recorder.discard()

    def create_new_driver(self):
        return Chrome(executable_path=PATH+'chromedriver.exe', options=self.create_new_options())

    def navigate(self, site='https://www.youtube.com/'):
        self.driver.get(site)

    def play_video(self):
        # clicking on play button
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, '//button[@class="ytp-play-button ytp-button"]'))).click()
        except:
            pass

    def acceptCookie(self):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button'))).click()
        except:
            pass

    # def maximize_video(self):
    #     #clicking on maximize button
    #     try:
    #         WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[@class="ytp-fullscreen-button ytp-button"]'))).click()
    #     except:
    #         pass

    def create_new_options(self):
        options = ChromeOptions()

        # remove pop-up with: 'browser is controlled by...'
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])

        return options

    def stop(self):
        self.driver.close()


if __name__ == '__main__':
    print('Try main.py...')
