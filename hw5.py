from music import *
from gui import *
from random import*
import time

# hw5.py
#
# Author: Ryan Frates
# Class: CSIS110
# Due Date: April 21, 2023
#
# Purpose: To visually display a short melody and display circles
#
# Input: R also mouse clicks
#
# Output: Plays the melody and displays the image
#

# Create a display to work with
d = Display("My Homework", 1000, 600)



radius = 10
#creates the radius fo the circle
def changeSize(newRadius):
   global radius 
   radius = newRadius
   print radius
slider1 = Slider (VERTICAL, 0, 127, 63, changeSize) #creates the slider

#creates random notes
def randomNote():
   myPhrase = Phrase()
   pitch = int(random() * 127)     # get random pitch between C1 and C6
   duration = random() * 3.6    # get random duration (0.0 to 2.0)
   dynamic = randint(PP, FFF)   # get random dynamic between P and FF
   note = Note(pitch, duration, dynamic) # create note
   myPhrase.addNote(note) 
   Play.midi (myPhrase)
   
#creates a drop down list to slect instruments from
def pickInstrument (which):
   if which == "Piano":
      Play.setInstrument(PIANO)
   if which == "Flute":
      Play.setInstrument(FLUTE)
   if which == "Marimba":
      Play.setInstrument(MARIMBA)
   if which == "Trumpet":
      Play.setInstrument(TRUMPET)
   if which == "Harpsichord":
      Play.setInstrument(HARPSICHORD)
dropDownList1 = DropDownList(["Piano", "Flute", "Marimba", "Trumpet", "Harpsichord"], pickInstrument)

#creates a drop down list to change the backround
def setBackround (which):
   if which == "Red":
     d.setColor(Color(255,0,0))
   if which == "Blue":
     d.setColor(Color(0,0,255))
   if which == "Green":
     d.setColor(Color(0,255,0))
   if which == "Black":
      d.setColor(Color(0,0,0))
   if which == "White":
      d.setColor(Color(255,255,255))
dropDownList2 = DropDownList(["Blue", "Red", "Green", "Black", "White"], setBackround)
#creates the witdget drop down list

#This key action takes a little bit of time to complete it alos freezes the program for a little also might have to retry the program
#Plays notes and displays text through a note
def keyAction(key):
   print "It's going to be a little bit"
   if key == "r":
      for i in range (0, 3):
        
         myPhrase = Phrase()
         pitches = [G2,E2]
         durations = [EN, EN]
         dynamic = [FFF,FFF]
         myPhrase.addNoteList (pitches, durations, dynamic)
         labelTemp = Label("U broke it")
         labelTemp.setFont(Font("Dialog", Font.PLAIN, 36))
         d.add (labelTemp,300,400)
         time.sleep(5)
         Mod.mutate(myPhrase)
         Play.midi(myPhrase)
         


#It stops the circles from appearing
def stop():
      d.removeAll()
      b1 = Button("Start", createCircle)
      d.add(slider1, 600, 10)
      d.add(b1, 65, 70)
      d.add (dropDownList1, 65, 150)
      d.add (dropDownList2, 65, 200)
      d.onKeyType (keyAction)
      d.add (label1, 520, 100)
      d.add (label2, 65, 125)
      d.add (label3, 65, 175)
      d.add (label4, 520, 30)
      d.add (label5, 520, 190)

#creates the circles amd makes them pop up in radom locations when you click them
#then they will dissapear 
def createCircle(a=None,b=None):
      d.removeAll()
      b2 = Button("stop", stop)
      d.add(b2, 90,30)
      x = int (random()*800+100)
      y = int (random()*400+100)
      circle = d.drawCircle(x,y, radius, Color(int(random()*255),int (random())*255,int (random()*255),255),1)
      print x
      print y
    
      circle.onMouseClick(createCircle)
      randomNote()
#creates the start button and adds all of the widgets
def start():
   b1 = Button("Start", createCircle)
   d.add(slider1, 600, 10)
   d.add(b1, 65, 70)
   d.add (dropDownList1, 65, 150)
   d.add (dropDownList2, 65, 200)
   d.onKeyType (keyAction)
   d.add (label1, 520, 100)
   d.add (label2, 65, 125)
   d.add (label3, 65, 175)
   d.add (label4, 520, 30)
   d.add (label5, 520, 170)


#creates labels   
label1 = Label("Circle Size")
label2 = Label("Instrument")
label3 = Label("Backround color")
label4 = Label("bigger")
label5 = Label("smaller")
d.onKeyType (keyAction)
start()
