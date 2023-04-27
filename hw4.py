# hw4.py
#
# Author: Ryan Frates
# Class: CSIS110
# Due Date: March 31, 2023
#
# Purpose: To visually display a short melody
#
# Input: None
#
# Output: Plays the melody and displays the image
#
from music import *
from image import *
from random import *

# Map a pitch
# Inputs: p: the pitch to map (0-127)
# img: the image to map it onto
# count: which note we're mapping
# maxNotes: number of notes in melody
#
# Output: none, but img will be changed so a small red
# square has been placed in the image. The
# x coordinate is determined by the count and the
# y coordinate is determinted by the pitch (higher
# pitches closer to the top)
def mapPitch (p, img, count, maxNotes):
   xValue = count * (400 / maxNotes) - 2
   yValue = 399 - (p * (400 / 128))
   img.setPixel (xValue, yValue, [255,0,0])
   img.setPixel (xValue+1, yValue+1, [255,0,0])
   img.setPixel (xValue, yValue+1, [255,0,0])
   img.setPixel (xValue+1, yValue, [255,0,0])

def mapDynamic (p, img, count, maxNotes):
   xValue = count * (400 / maxNotes) - 2
   yValue = 399 -    (p * (400 / 128))
   img.setPixel (xValue, yValue, [55,100,82])
   img.setPixel (xValue, yValue+1, [55,100,82])
   img.setPixel (xValue-1, yValue, [55,100,82])
   img.setPixel (xValue+1, yValue, [55,100,82])
   img.setPixel (xValue, yValue-1, [55,100,82])

def mapDuration (p, img, count, maxNotes):
   xValue = count * (400 / maxNotes) - 2
   yValue = 399 - int(p * (400 / 4))
   img.setPixel (xValue, yValue, [25,51,236])
   img.setPixel (xValue-1, yValue-1, [25,51,236])
   img.setPixel (xValue+1, yValue-1, [25,51,236])
   img.setPixel (xValue+1, yValue+1, [25,51,236])
   img.setPixel (xValue-1, yValue+1, [25,51,236])


# Put a note onto image
# Inputs: Note: the note to map (with pitch, duration, and volume)
# img: the image to place it on (assumed to be 400x400 pixels)
# count: the number of the note (1, 2, 3, ...)
# maxNotes: the nubmer of notes total that will be placed in the image
# Outputs: none, but "img" has been changed
def mapNote(note, img, count, maxNotes):
   pitch = note.getPitch()
   duration = note.getDuration()
   dynamic = note.getDynamic()
# also need to get durations and volumes
   mapPitch (pitch, img, count, maxNotes)
   mapDuration (duration, img, count, maxNotes)
   mapDynamic (dynamic, img, count, maxNotes)
# also need to map durations and volumes to the image
# Main program: Create N-note phrase, with notes of varying volumes, pitches, and durations,
# and map it onto a 400x400 image
# Set up empty phrase and blank image

def randomNote(c):
   pitch = int(random() * 127)     # get random pitch between C1 and C6
   duration = random() * 3.6    # get random duration (0.0 to 2.0)
   dynamic = randint(PP, FFF)   # get random dynamic between P and FF
   note = Note(pitch, duration, dynamic) # create note
   mapNote (note, myPic, x, maxNotes)
   myPhrase.addNote(note) 

myPhrase = Phrase()
myPic = Image (400,400)
maxNotes = 20
# Create and map Note
#   note = Note (C4, QN, FFF)
#   myPhrase.addNote (note)
#   mapNote (note, myPic, 1, maxNotes)

x = 1
while x <= maxNotes:
   randomNote(x)
   x= x + 1


# Play phrase and display image
Play.midi (myPhrase)
myPic.show()