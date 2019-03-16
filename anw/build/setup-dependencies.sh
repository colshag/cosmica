echo ================================================
echo Welcome to the Cosmica Dependency Installer
echo I will be attempting to install various python 
echo dependencies using the python pip installer
echo ================================================
echo I am leaving this command window open for your 
echo information, close the window manually when complete.
echo ================================================
echo Chris Lewis.
echo NeuroJump. 2019.
echo ================================================
sudo apt install python-pip python-qt4
pip install panda3d==1.10.2
pip install gitpython
pip install twisted service_identity
echo ================================================
echo downloading cosmica from play-cosmica git repository....
echo ....This will take a minute or two depending on your
echo ....Internet speed
cp getCosmica.py ~
python ~\getCosmica.py
cp cosmica.desktop /usr/share/applications
read -p "Press enter to exit"
