from pypresence import Presence
from time import time

"""
How to work with bot?
First of all you need create application on Discord developers.
Next step choose your created application and write the name 
that will be displayed in the status.

"""

RPC = Presence("APPLICATIONS_ID") # Aplication ID you can get on General Information your bot
"""
# If you want to create the buttons on your status, just uncomment this constructions.

btns = [
    {
        "label": "", # button name
        "url": "" # button url
    {
        "label": "",
        "url": ""
    }
]
"""

RPC.connect()

'''
About Rich Presence you can read on Discord developers -> Application -> Rich Presence
There you will see what is responsible for what.
'''

RPC.update(
    state="", #str state
    details="", #str details
    start=time(),
    #buttons=btns, #uncomment it if you want to create the buttons on your applications.
    large_image="", #image which you upload on your appliсation, specify the name
    small_image="",
    large_text="", #the text that will be displayed when you hover over the icon
    small_text=""
)

input("Write something to quit the program: ")