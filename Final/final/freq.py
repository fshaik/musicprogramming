import wx
from random import randint
import math
import time

class Frequency(wx.Panel):
    def __init__(self, parent, pos, size, sf, bq):
        wx.Panel.__init__(self, parent=parent, pos=pos, size=size)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.pos = None
        self.selected = None
        self.mtoggle = None
        self.millisAtLastPaint = None
        self.curMillis = None
        self.curRotateFactor = None
        w,h = self.GetSize()
        self.mposx = w/2 -10
        self.mposy = h/24
        self.sf =sf
        self.bq = bq

        #print "TRACE: Rotations per second", self.rotationsPerSecond

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.MouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.MouseUp)
        self.Bind(wx.EVT_MOTION, self.Motion)

    def OnPaint(self, evt):

        w,h = self.GetSize()

        #ajust the width and height such that they are slightly smaller than the entire container
       
        
        dc = wx.PaintDC(self)
        #draw crossfader
        # draw the vinyl album.
        dc.SetBrush(wx.Brush("#C0C0C0"))
        dc.DrawRectangle(0 ,0, w,h)
        
        w -= (w/12)
        h -= (h/12)
        
        dc.SetBrush(wx.Brush("#FFFFFF"))
        dc.DrawRectangle(self.mposx ,self.mposy, 10,h)
        #dc.DrawEllipse(0,0,w,h)

    def MouseDown(self, evt):
        self.drop = False
        self.CaptureMouse()
        self.pos = evt.GetPosition()
        self.mposx = self.pos[0]
        
        print "TRACE: mouse down, position is ", self.pos


    def MouseUp(self, evt):
        if self.HasCapture():
            self.pos = evt.GetPosition()
            print "TRACE: mouse up, position is ", self.pos
            self.ReleaseMouse()
            self.pos = self.selected = None
            self.Refresh()
            w,h = self.GetSize()
            halfway = h/2
            x = self.mposx
            
            freq = float(x)/float(w) *20000
            
            print "Setting freq " +  str(freq)

            self.bq.setFreq(freq)

    def Motion(self, evt):
        w,h = self.GetSize()
        if self.HasCapture():
            (xPos, yPos) = evt.GetPosition()
            print "TRACE: moving mouse ", (xPos, yPos)

            # if yDiff is negative, we are moving down.  If yDiff is positive, we are going up.
            yDiff = yPos - self.pos[1]

            directionString = "NOWHERE"

            if yDiff < 0:
                directionString = "UP"
            elif yDiff > 0:
                directionString = "DOWN"

            print "TRACE: we are going ", directionString

            self.curRotateFactor += (-yDiff * 2 * math.pi) / 300

            self.pos = (xPos, yPos)
            self.Refresh()
