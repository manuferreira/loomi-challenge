# Loomi Challenge

- <b>How to setup the environment - for Windows 10?</b><br>
  1. Install Python 3.12.1: go to https://www.python.org/downloads/
  2. Install VSCode: go to https://code.visualstudio.com/
  3. Install Chrome: go to https://www.google.com/chrome/
  4. Install WebDriver (Chromedriver) for Chrome (be aware to choose between the Chromedriver Win64 or win32 version): https://googlechromelabs.github.io/chrome-for-testing/ <br>
     I used the https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip version, remember to add the chromedriver to your environment variable PATH
  5. Install the Selenium package for Python: go to https://pypi.org/project/selenium/
     In this case, you will have to execute the following command on PowerShell: <code>pip install selenium</code> remember to add python to your environment variable PATH

- <b>How the folders are organized?</b>
  - pages: I had to put the files inside this one page because of some import errors, this will be fixed later on and the files will be put in their respective folders.
  - resources
  - config

- <b>How to run a test?</b>
  - The tests are located inside the files that start with <b>test_</b> example: <b>test_login.py</b> you have to run the __main__ method inside these files and all the tests related to that file will be run.



