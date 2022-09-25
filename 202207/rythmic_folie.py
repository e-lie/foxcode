

from FoxDot.preset.common import *
from FoxDot.preset.reaper import *

change_bpm(136, True, .81)
Clock.meter = (6,8)
Scale.default = Scale.egyptian

d1 >> play("-", dur=P[.5] << [0,linvar([0,.2],4),linvar([0,.1],4)])


d2 >> play("-", dur=PSum(7,3), sample=3)
d3 >> play("VvvXvv")

d_all.rate = (.9,linvar([.5,3],17),2)
d_all.pan = [(-1,0,1),-1,(-1,0,1),1]
d_all.amp = PTri(7,12)/10
d_all.sample = PRand(0,4)[:77]
d_all.crush = linvar([0,32],64)

################################################################

ch = var([0,2,3,-1], 3)
bb >> hpluck(ch, dur=PSum(5,3) << [0,.1,0,0,-.05], oct=3).humz()
b2 >> tb303(ch, dur=PSum(4,3) << [0,0,.05,0,-.05,0], oct=4)

Root.default = var([0,-5,-1,2],6)

################################################################

change_bpm(136, True, .81)
Clock.meter = (6,8)

d1 >> play("<V..><.(.-)(...(-[.-]))>", sample=3, rate=1)
d2 >> play("x(.[---])", sample=0, rate=1, dur=1, amplify=pa16)
d3 >> play("ttt  T", dur=P[.5] << [0,.1,.05])
