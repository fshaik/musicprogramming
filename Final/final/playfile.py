import pyo
from pyo import *

s =  Server().boot()
s.start()
snd = "../music/bassfuck.wav"
sf = SfPlayer(snd, speed=1, loop=False, mul=1).out()
