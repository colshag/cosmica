@echo off
echo ================================================
echo Welcome to the Cosmica Dependency Installer
echo I will be attempting to install various python 
echo dependencies using the python pip installer
echo.
echo I am leaving this command window open for your 
echo information, close the window manually when complete.
echo.
echo If you are getting "no pip" messages, reinstall python
echo make sure to enable the "Add python.exe to Path" option!
echo ================================================
echo Chris Lewis.
echo NeuroJump. 2019.
echo ================================================
c:\Python27\Scripts\pip install panda3d==1.10.2
c:\Python27\Scripts\pip install gitpython
c:\Python27\Scripts\pip install Twisted-18.9.0-cp27-cp27m-win_amd64.whl
c:\Python27\Scripts\pip install PyQt4-4.11.4-cp27-cp27m-win_amd64.whl
echo ================================================
echo downloading cosmica from play-cosmica git repository....
echo ....This will take a minute or two depending on your
echo ....Internet speed
c:\Python27\python getCosmica.py
PAUSE