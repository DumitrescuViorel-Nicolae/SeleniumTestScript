import math
import audioop

# https://stackoverflow.com/questions/25868428/pyaudio-how-to-check-volume


def decibels(data) -> int:

    rms = audioop.rms(data, 2)
    if rms > 0:
        return int(20 * math.log10(rms))
    else:
        return 0


if __name__ == '_main_':
    print('Try main.py...')
