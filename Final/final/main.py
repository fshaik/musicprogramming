#!/usr/bin/python

# turntables project.

# import WX Python
import wx
from pyo import *
from turntable import Turntable
from mixer import Mixer
from tempo import Tempo
from freq import Frequency

# start the pyo server.
s = Server()

# Set the MIDI input device number. See pm_list_devices() to obtain valid devices.
print pm_list_devices() 
s.setMidiInputDevice(3)

# start the pyo audio engine.
s.boot().start()
snd = "../music/bassfuck.wav"
sf = SfPlayer(snd, speed=1, loop=False, mul=.5)
snd = "../music/grama.wav"
sf2= SfPlayer(snd, speed=1, loop=False, mul=.5)
bq = Biquadx(sf,freq=0, q=.75, type=1)
bq2 = Biquadx(sf2,freq=0, q=.75, type=1)

# declare the MyFrame class that extends wx.Frame.
class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=wx.ID_ANY, title="TurnTables", pos=(50,50), size=(1100,700)):
        global sf
		
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.panel = wx.Panel(self)
        self.timer=wx.Timer(self)
        self.timer.Start(milliseconds=5, oneShot=False)
        
        self.turntableL = Turntable(self.panel, pos=(150,50), size=(400,400), sf=sf, bq=bq)
        self.turntableR = Turntable(self.panel, pos=(550,50), size=(400,400), sf=sf2, bq=bq2)
        self.mixer = Mixer(self.panel, pos=(350, 500), size=(400,100), sf1=sf, sf2=sf2)
        self.tempoL = Tempo(self.panel, pos=(50,50), size=(50,400),sf=sf)  
        self.tempR = Tempo(self.panel, pos=(1000,50), size=(50,400),sf=sf2) 
        
        
        self.freqL = Frequency(self.panel, pos=(200,450), size=(100,50),sf=sf, bq=bq)  
        
        self.freqR = Frequency(self.panel, pos=(800,450), size=(100,50),sf=sf2, bq = bq2) 
        
        self.Bind(wx.EVT_TIMER,self.OnTimer)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Show()

    def OnPaint(self, evt):
        pass
        #print "TRACE: MyFrame Paint()"

    def OnTimer(self, event):
        self.turntableL.Refresh()
        self.turntableR.Refresh()
        self.mixer.Refresh()
        
app = wx.App(False)
frame = MyFrame()

app.MainLoop()




