#Import the library

from midiutil.MidiFile import MIDIFile
import random
import jdata

def chooseNote(data):
  return int(data * 150)





# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(2)

track = 0
time = 0

MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track,time,132)

track = 0
channel = 0
pitch = 50
time = 0
duration = 1
volume = 100

for i in range(len(jdata.calorie)):
  print "Hi"
  MyMIDI.addNote(track, channel, chooseNote(jdata.calorie[i]), time, duration, volume)
  pitch = pitch  + 1
  time = time + 2
  
track = 1;
time = 1
pitch = 50
duration = 1
volume = 100

MyMIDI.addTrackName(1, time, "sleep")
MyMIDI.addTempo(track, time, 132)

for i in range(len(jdata.sleep)):
  print "Hi"
  MyMIDI.addNote(track, channel, chooseNote(jdata.sleep[i]), time, duration, volume)
  pitch = pitch  + 1
  time = time + 2
  
#for i in range(0,10):
  #print "Hi"
  #MyMIDI.addNote(track, channel, pitch, time, duration, volume)
  #pitch = pitch  + 1
  #time = time + 1
  

  

# And write it to disk.
binfile = open("output2.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()