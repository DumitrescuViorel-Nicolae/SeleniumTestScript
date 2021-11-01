from driver import SeleniumHandler


def goto(driver: SeleniumHandler):
    url = None
    filename = None
    duration = None
    while True:
        print('Enter: url, filename, duration:')
        try:
            url = input('    Youtube link to be tested: ')
            filename = input('    Filename for the current test: ')
            duration = int(input('    Duration: '))

            print('Navigating...')
            driver.navigate(url)
            driver.acceptCookie()
            driver.start_recordings(filename, duration)
            driver.play_video()
            driver.stop()
            return
        except:
            if input('Something went wrong! Do you wanna exit (y/n)? :').lower() == 'y':
                return


def interact():
    print('Starting...')
    driver = SeleniumHandler()
    while True:
        try:
            choise = int(
                input('Select option:\n    1 - go to\n    2 - exit\n'))
            if choise not in range(1, 3):
                print('Your choise must be 1 or 2!')
            else:
                if choise == 1:
                    goto(driver)
                elif choise == 2:
                    break
                else:
                    continue
        except:
            if input('Something went wrong! Do you wanna exit (y/n)? :').lower() == 'y':
                break

# def concatenate():
#     subprocess.run(["C:/proiect/ffmpeg","-y", "-i","out.mp4", "-i", "audio.wav", "-map", "0:v", "-map", "1:a", "-c", "copy", "output.mp4"],creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == '__main__':
    interact()
