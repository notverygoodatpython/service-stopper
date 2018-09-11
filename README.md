# service-stopper
This program uses a basic python script plus tkinter to call on Windows batch scripts to stop/start and then display the status of a service. In this case it starts/stops the Adobe Acrobat Update service: a placeholder for whatever you want. 
# Installation Instructions
You can use the standalone or the python prerequisite version.
The standalone is much slower to load.
## Standalone
Just follow this link: https://mega.nz/#!TfIhWIbC

And use this key: !YN-9xQgL0aiZ1mW8HKIVDY2cK0pXB_yWUl9lp1TuMvI

Then download nircmd (http://www.nirsoft.net/utils/nircmd.html) (download links are at the very bottom of that page) and copy nircmd and nircmdc to your windows directory (C:/Windows)

Extract, and enjoy! (use the exe)
## Python Prerequisite
You must have installed Python 3 (https://www.python.org/downloads/) and nircmd (http://www.nirsoft.net/utils/nircmd.html) (download links are at the very bottom of that page) and copied nircmd and nircmdc to your windows directory (C:/Windows)

Then, just download the files into one folder, and run the .pyw file!

Python is required to run the script and nircmd is required to run the batch scripts at admin level automatically (still needs UAC)
# To customise the script
Simply change the name of the started/stopped/queried service to whatever you want in the two .bat files (use task manager; services tab to find the relavent service)
# Beware
The script CANNOT run on its own, it still requires you to click 'allow' in the UAC prompt. You could use one of the suggestions here: https://www.techgainer.com/disable-uac-prompts-specific-programs-windows/   but I haven't tried any of them so they are unproven (also you would probably need to disable UAC for the entire CMD.exe, which isn't a great idea.)

This whole program most likely won't work on linux or any other os.
# Thanks to:
Nir Sofer: http://www.nirsoft.net/ , whose nircmd utility is essential in allowing the batch scripts to run as admin.

Brent Vollebregt: https://github.com/brentvollebregt , whose auto-py-to-exe allowed me to convert the py files to a standalone exe.

The PyInstaller guys: http://www.pyinstaller.org/ , whose program is the foundation of auto-py-to-exe

Many  thanks!
