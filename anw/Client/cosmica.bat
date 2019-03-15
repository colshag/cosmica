@echo off
echo Welcome to Cosmcia!
echo ======================================
echo I will now attempt to update your code 
echo from the git repo play-cosmica on GitHub!
python update.py
echo ======================================
echo Great! Now let's run the launcher!
echo I'm leaving this command prompt active so
echo that if the game crashes you can give a 
echo screenshot of what went wrong. 
echo ======================================
echo Thanks for Playing!
echo Chris/Jeremy/Steve
echo NeuroJump. 2019.
echo ======================================
python launcher.py
PAUSE