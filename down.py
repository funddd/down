import wget
import easygui
import sys
while True:
    if easygui.ccbox(msg = "down",title = "wgetdown",choices = ("new down","close")) == True:
        DATA_URL = easygui.enterbox(msg="URL",title = "new down")
        DATA_PATH = easygui.filesavebox() 
        a = wget.download(DATA_URL, out=DATA_PATH)
        easygui.msgbox("Download complete")
    if easygui.ccbox(msg = "down",title = "wgetdown",choices = ("new down","close")) == False:
        sys.exit(0)
