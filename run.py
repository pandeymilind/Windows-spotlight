import os
from datetime import datetime
import subprocess, sys




now = datetime.now()
string=now.strftime("%Y%m%d%H%M%S")

def copy_image(Username,path):

        try:
                copy_and_past= subprocess.Popen(["powershell.exe", f'Copy-Item -Path "C:\\Users\\{Username}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets" -Destination "{path}\\Assets{string}" -Recurse'], stdout=sys.stdout)
                copy_and_past.communicate()
        except:
          print("An exception occurred")
def convert(path):
        dir_set= subprocess.Popen(["powershell.exe", f'Set-Location -Path {path}\\Assets{string}'+'; Dir | rename-item -newname  { $_.Name +".png" }'], stdout=sys.stdout)
        dir_set.communicate()
        return f"Assets{string}"