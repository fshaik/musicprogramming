import wx
from random import randint
import math
import time

class Mixer(wx.Panel):
    def __init__(self, parent, pos, size, sf1, sf2):
        wx.Panel.__init__(self, parent=parent, pos=pos, size=size)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.pos = None
        self.selected = None
        self.mtoggle = None
        self.millisAtLastPaint = None
        self.curMillis = None
        self.curRotateFactor = None
        w,h = self.GetSize()
        self.mposx = w/2 +10
        self.mposy = h/24
        self.sf1 =sf1
        self.sf2 = sf2
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

        # draw the label of the vinyl album
        # labelW = w / 3.2
        # middleXPos = w/2
        # middleYPos = h/2
        # dc.SetBrush(wx.Brush("#FFFFFF"))
        # dc.DrawEllipse(0 + middleXPos - labelW/2,
                       # 0 + middleYPos - labelW/2, 
                       # labelW,
                       # labelW)

        # draw the spindle hole of the vinyl album
        # spindleW = labelW / 8
        # dc.SetBrush(wx.Brush("#000000"))
        # dc.DrawEllipse(0 + middleXPos - spindleW/2,
                       # 0 + middleYPos - spindleW/2, 
                       # spindleW,
                       # spindleW)

        #draw the teal radius guide lines
        # dc.SetPen(wx.Pen("#00FFFF"))
        # for i in range(0,12):
            # rads = i * ((2 * math.pi) / 12)
            # startXLinePos = math.cos(rads + self.curRotateFactor) * (labelW/2) + middleXPos
            # startYLinePos = math.sin(rads + self.curRotateFactor) * (labelW/2) + middleYPos
            # endXLinePos = math.cos(rads + self.curRotateFactor) * (w/2) + middleXPos
            # endYLinePos = math.sin(rads + self.curRotateFactor) * (w/2) + middleYPos
            # if (i != 11):
                # pass
                # disabled the sectional indicators for now, there were some refresh issues
                # that were visually distracting.
                # dc.DrawLine(startXLinePos, startYLinePos, endXLinePos, endYLinePos)
            # else:
                # draw a special red marker that marks the beginning of the sample
                # (at 2:00 o'clock, 11th position counterclockwise from horizontal origin).
                # penSize = 3
                # dc.SetPen(wx.Pen("#FF0000", penSize))
                # dc.DrawLine(startXLinePos, startYLinePos, endXLinePos, endYLinePos)
                # dc.SetPen(wx.Pen("#00FFFF", 1))

        # reset pen to black, 1 pixel.
       # dc.SetPen(wx.Pen("#000000", 1))

        # make sure that millisAtLastPaint is set.
        #self.millisAtLastPaint = self.curMillis

        # draw the marker that indicates the 'scratch sample' begin position
        # draw the label at 2 o'clock (11/12 running counter clockwise
        # from horizontal position.
#        rads = 11 * ((2 * math.pi) / 12)
#        dc.SetBrush(wx.Brush("#FF0000"))
#        startLabelW = 30
#        startLabelH = 10
#        dc.DrawRectangle(middleXPos + labelW/2,
#                         middleYPos - startLabelH/2, 
#                         startLabelW,
#                         startLabelH)

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
            sf2mul = float(self.mposx) / float(w)
            print "Setting Mul to " + str(sf2mul)
            self.sf2.setMul(sf2mul)
            self.sf1.setMul(1-sf2mul)

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
