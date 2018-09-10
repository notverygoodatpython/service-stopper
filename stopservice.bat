net stop qupdate
timeout 2
net stop qengine
timeout 1
sc query qupdate
sc query qengine
pause