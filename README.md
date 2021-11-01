# SeleniumTestScript
 This script uses SeleniumAPI to play an youtube video while recording the desktop screen

# System Information
OS: Windows 11 Home Insider Preview Single Language

Build: 22489.1000

Python version running: 3.9.7

# Prerequisites
You may create a virtual environment if a python you have a python version already installed
* Open Windows terminal
* Create 2 new folders in the current directory (mkdir pyver, mkdir pyproj)
* Install python 3.10 in the pyver\py310
* Create a virtual env in the pyproj folder - C:\Users\dterm\pyver\py310\python -m venv {placeholder for name}
* Activate the env -  {chosen name}\Scripts\activate (if you encounter a 'cannot be loaded error' you may need to run "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted" command )
* Install Python 3.10
* Install pip
* Check versions ` python --version` and `pip --version`

# For the screen record
* `pip install opencv-python pyautogui numpy`

# For audio record
* `pip install pipwin` in order to get a supported wheel for pyaudio
* `piwin install pyaudio`
* also to avoid any headaches to record system sound, set stereo mix as default (Win+R mmsys.cpl and change from the Recording tab)

# For SeleniumAPI
* `pip install selenium`
To ensure the functionality of SeleniumAPI, a driver must also be installed depending on the preffered browser and its version.
In this case I installed a chromedriver from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and added it to PATH.
* `pip install webdriver-manager`

Finally, to run the script, open it in VSCode, run the main.py and follow the instructions given for input.


