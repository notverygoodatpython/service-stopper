# service-stopper
This program uses a basic python script plus tkinter to call on Windows batch scripts to stop/start and then display the status of the services. In my case it starts/stops the Adobe Acrobat Update service: a placeholder for whatever you want. 
# Installation Instructions
You can use the standalone or the python prerequisite version.
## Standalone
Just follow this link: https://mega.nz/#!TfIhWIbC

And use this key: !YN-9xQgL0aiZ1mW8HKIVDY2cK0pXB_yWUl9lp1TuMvI

Extract, and enjoy! (use the exe)
## Python Prerequisite
You must have installed Python 3 (https://www.python.org/downloads/) and nircmd (http://www.nirsoft.net/utils/nircmd.html) (download links are at the very bottom of the page).

Then, just download the files into one folder, and run the .pyw file!

Python is required to run the script and nircmd is required to run the batch scripts at admin level automatically (still needs UAC)
# To customise the script
Simply change the name of the started/stopped/queried service to whatever you want (use task manager; services tab to find the relavent service)
# Beware
The script CANNOT run on its own, it still requires you to click 'allow' in the UAC prompt. You could use one of the suggestions here: https://www.techgainer.com/disable-uac-prompts-specific-programs-windows/   but I haven't tried any of them so they are unproven (also you would probably need to disable UAC for the entire CMD.exe, which isn't a gread idea.)

This whole program most likely doesn't work on linux or any other os.
