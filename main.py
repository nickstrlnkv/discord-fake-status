from pypresence import Presence
from time import time

"""
How to work with bot?
First of all you need create application on Discord developers.
Next step choose your created application and write the name 
that will be displayed in the status

"""

RPC = Presence("APPLICATIONS_ID") # Aplication ID you can get on General Information your bot
"""
# If you want create the buttons on your status, just uncomment this constructions

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
RPC.update(
    state="Singleplayer",
    details="At the: hla_trainstation1",
    start=time(),
    #buttons=btns,
    large_image="half-life512", #image which you upload on your appliсation, specify the name
    small_image="half-life512",
    large_text="Half-Life: Alyx", #the text that will be displayed when you hover over the icon
    small_text="Half-Life: Alyx"
)

input("Write something to quit the program: ")