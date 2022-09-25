from FoxDot.preset import *

Clock.meter = (5,4)

b1 >> blip(ch, dur=cubalet, oct=[4,5,6])

cclock = TempoClock()

d1 >> play("Osssss", dur=1)
d2 >> play("X-o-", dur=1, sample=0, amp=.7).stop()

@nextBar()
def change():
    d1 >> play("Tiiiii", dur=1)
    d2 >> play("X-o-", dur=1, sample=2, amp=.7).stop()


### Example from ryan (slightly moded)

Clock.meter = (9,4)
Clock.bpm = 160
Scale.default = Pvar([Scale.major, Scale.minor], 9)

ch = var([0,1,-2,3], [4,5])


bb >> tb303(ch, dur=PSum(3,8)/4, oct=(3,4))
b2 >> blip(ch + [0,2,0,4], dur=.25)

sn >> play("..i."*3 + "..i.i.", sample=0, amp=.75).mpan(var(P[range(6)], 1.5))

hh >> play("---[--]"*3 + "-----[--]", sample=2, amp=.75)
k1 >> play("X."*6 + "X.X.XX", sample=2, amp=1)
cc >> play("[VV]********", dur=1, sample=0, amp=.75)

################################################################

Clock.bpm = 125

d1 >> play("*", dur=PSum(3,2)).every(16,"stutter",2)
d2 >> play("-", dur=PSum(3,8)/4, amp=2).every(16,"stutter",3)
d3 >> play("..(---.)(---[--])", dur=.25, amp=1)

################################################################

Clock.bpm = 130

d1 >> play("*", dur=clave23, amp=1.2).every(8,"stutter",2)
d3 >> play("X.", dur=.5, amp=1)
d2 >> play("i", dur=cascara, amp=.70, amplify=pa32_2).every(32,"stutter",3)
d4 >> play(".-", dur=.5, amp=3, amplify=pa16)

m1 >> marimba("aabb", dur=clave23)
