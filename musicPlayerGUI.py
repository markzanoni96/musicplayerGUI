"""
1/3/2023  Program: videoStoreGUI.py

GUI-based version of the Video Store application from chapter 2.
NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

ALSO NOTE: you MUST install the pygame package by running: pup install pygame
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from pygame import mixer
from tkinter import PhotoImage

# other imports can go here

class musicPlayerGUI(EasyFrame):
	

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Music Player GUI", background = "black", resizable = False)
		self.addLabel(text = "Python Music Player", row = 0, column = 0, columnspan = 3, background = "black", foreground = "orange", sticky = "NSEW", font = Font(family = "Impact", size = 28))
		# create a variable and add a label for our image
		self.imageLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 3, sticky = "NSEW", background = "black")
		# load the image into the imageLabel object 
		self.image = PhotoImage(file = "music_player.png")
		self.imageLabel["image"] = self.image
		# label and button to load the music file
		self.addLabel(text = "Enter a music file name to load:", row = 2, column = 0, background = "black", foreground = "orange", sticky = "NE")
		self.musicFile = self.addTextField(text = "", row = 2, column = 1, width= 35)
		self.addButton(text = "Load Song", row = 2, column = 2, command = self.loadFile)

		# 3 buttons for the music player functions
		self.playButton = self.addButton(text= "Play", row = 3, column = 0, state = "disabled", command = self.playMusic)
		self.playButton = self.addButton(text= "Pause", row = 3, column = 1, state = "disabled", command = self.pauseMusic)
		self.playButton = self.addButton(text= "Resume", row = 3, column = 2, state = "disabled", command = self.resumeMusic)

	# Event handling functions for the command buttons
	def loadFile(self):
		# initialize the pygame mixer
		mixer.init()
		songFile = self.musicFile.getText()
		mixer.music.load(songFile)
		self.playButton["state"] = "normal"
		mixer.music.play()

	def playMusic(self):
		# play the loaded music file
		mixer.music.play()
		self.pauseButton["state"] = "normal"

	def pauseMusic(self):
		# pause the current song
		mixer.music.pause()
		self.resumeButton["state"] = "normal"
		self.pauseButton["state"] = "disabled"

	def resumeMusic(self):
		mixer.music.unpause()
		self.resumeButton["state"] = "disabled"
		self.pauseButton["state"] = "normal"




# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	musicPlayerGUI().mainloop()

# global call to the main() method
main()


