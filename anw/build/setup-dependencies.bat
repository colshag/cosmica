@echo off
echo ================================================
echo Welcome to the Cosmica Dependency Installer
echo I will be attempting to install various python 
echo dependencies using the python pip installer
echo.
echo I am leaving this command window open for your 
echo information, close the window manually when complete.
echo.
echo When git installs just press Next to all the questions :)
echo ================================================
echo Chris Lewis.
echo NeuroJump. 2019.
echo ================================================
echo First we have to install Python, there is a pause while this is done now...
msiexec /i "python-2.7.16.amd64.msi" /quiet /norestart Include_pip=1 Include_test=0 PrependPath=1 ADDLOCAL=ALL
echo.
echo Now we install Panda3d, gitPython, Twisted, PyQt4, and Zope...
c:\Python27\Scripts\pip install panda3d==1.10.2
c:\Python27\Scripts\pip install gitpython
c:\Python27\Scripts\pip install Twisted-18.9.0-cp27-cp27m-win_amd64.whl
c:\Python27\Scripts\pip install PyQt4-4.11.4-cp27-cp27m-win_amd64.whl
c:\Python27\Scripts\pip install zope.interface-4.6.0-cp27-cp27m-win_amd64.whl
echo ================================================
echo downloading cosmica from play-cosmica git repository....
"C:\Program Files\Git\bin\git.exe" clone http://github.com/colshag/play-cosmica.git
PAUSE