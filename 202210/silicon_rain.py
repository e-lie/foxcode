
Root.default=0

Clock.bpm=160

b3 >> blip(0, dur=PWhite(.1,.5), sus=PWhite(.2,2), amp=PWhite(.2,1.5)) + PWhite(0,.5) + var([0,1,3],clave23)
b1 >> blip(0, dur=PWhite(.1,.5), sus=PWhite(.2,2), amp=PWhite(.2,1.5), oct=3) + PWhite(0,.5)

b1 >> blip(0, dur=PWhite(.1,.5), sus=PWhite(.2,2), amp=PWhite(.2,1.5), oct=3) + PRand(0,5)
b1 >> blip(0, dur=PWhite(.1,.5), sus=3, amp=PWhite(.2,1.5), oct=3) + PRand(0,5)

b1 >> blip(0, dur=PWhite(.1,.5), sus=3, amp=PWhite(.2,1.5), oct=var(PRand(2,7)[:16],PRand(2,6))) + PRand(0,5)

b1.mpan(PRand(0,5))

b3.mpan(PRand(0,5))

d1 >> play("(VVVV)(.(O...O).(*..[**]))", sample=1, amp=1, crush=8, bits=2).mpan(mrot(32))

################################################################

# on part d'un pluie minimale, on augmente la randomisation de plusieurs paramètres
# diminue ensuite la randomisation pour aller vers une melodie tout mimi comme dans polybloiferous
# puis comme dans ce morceau on rajoute un kick vener en contraste avec la mélodie

t2 >> blip(0)

b1 >> blip([0,2,-2], dur=[.5,1,1,.25,.25], oct=PRand(3,4)).pause(4,16)
b2 >> blip([0,2,-2], dur=[.5,1,1,2], oct=PRand(5,7)).pause(4,16,10)

d1 >> play("(vvvV)(.(---[**]))", sdb=0, amp=1, amplify=1)

################################################################

from FoxDot.preset import *

fordrip, hpluck, digivibes = add_chains("fordrip", "hpluck", "digivibes")

change_bpm(160, True, .82)
change_bpm(160)

def shift_clock(time, shift, factor=16):
    time *= factor
    shift *= factor
    return max(time-shift,0)

cshift = 0

f1.vol=.6
f1.span(srot(32))
f1.fadeout(16)

@nextBar(shift_clock(0, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*20, sus=1, oct=PRand(5,6)).ampfadein(16)
@nextBar(shift_clock(1, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*10, sus=1, oct=PRand(5,6))
@nextBar(shift_clock(2, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*6, sus=linvar([.3,3]), oct=PRand(5,6)).mpan(PRand([0,.5,3]))
@nextBar(shift_clock(3, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([5,6,3])).mpan(PRand([0,.5,3]))
@nextBar(shift_clock(4, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([5,6,7])).mpan(PRand([0,.5,3]))
@nextBar(shift_clock(5, cshift))
def a():
    b2 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.7,10]), oct=PRand([4,6,3])).mpan(PRand([1,2,3])).ampfadein(16)
@nextBar(shift_clock(6, cshift))
def a():
    b2 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([4,6,3])).mpan(PRand([1,2,3])).pause(4,12)
    b1 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
@nextBar(shift_clock(7, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
@nextBar(shift_clock(8, cshift))
def a():
    b1 >> blip(PWhite(0,.7), dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
    b2 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=PRand([4,6,3])).mpan(PRand([1,2,3])).pause(4,12)
@nextBar(shift_clock(9, cshift))
def a():
    b1 >> blip(PWhite(0,.7), dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=var(PRand(5,7)[:16],PRand(2,6))).mpan(PRand([0,.5,3])).pause(4,12,6)
    b2 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*4, sus=linvar([.3,3]), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
@nextBar(shift_clock(10, cshift))
def a():
    b1 >> blip(PWhite(0,.7), dur=PWhite(.1,.5)*4, sus=linvar([1,10],16), oct=var(PRand(5,7)[:16],PRand(2,6))).mpan(PRand([0,.5,3])).pause(4,12,6)
    b2 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*4, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
@nextBar(shift_clock(11, cshift))
def a():
    b1 >> blip(PWhite(0,.7), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(5,7)[:16],PRand(2,6))).mpan(PRand([0,.5,3])).pause(4,12,6)
    b2 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
@nextBar(shift_clock(12, cshift))
def a():
    b1 >> blip(PWhite(0,.7), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(5,7)[:16],PRand(2,6))).mpan(PRand([0,.5,3])).pause(4,12,6)
    b1 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
@nextBar(shift_clock(13, cshift))
def a():
    b1 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*4, sus=linvar([.3,3],16), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6) + PRand(0,5)
@nextBar(shift_clock(14, cshift))
def a():
    pass
    # d1 >> play("<xx.><vvv.>", dur=PWhite(.1,.5)*4).ampfadein()
@nextBar(shift_clock(15, cshift))
def a():
    pass
    f1 >> fordrip(0, dur=8, sus=6, oct=5).fadein(16)
    f1.vol=.6
    f1.span(srot(32))
@nextBar(shift_clock(16, cshift))
def a():
    b2 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12) + PRand(0,8)
@nextBar(shift_clock(17, cshift))
def a():
    b2 >> blip(0, dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12) + PRand(0,8)
@nextBar(shift_clock(18, cshift))
def a():
    b1 >> blip(0, dur=PWhite(.1,.5)*4, sus=linvar([.3,3],16), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6) + PRand(0,5)
@nextBar(shift_clock(19, cshift))
def a():
    Root.default = 0
    Scale.default = Scale.minor
    chords = var([0,5,2,3],[8,4,2,2])
    chords = var([0,5,-2,2,3,-4],[8,4,4,2,2,4])
    b1 >> blip(chords, dur=PWhite(.1,.5)*2, sus=linvar([.3,3],16), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
@nextBar(shift_clock(20, cshift))
def a():
    b2 >> blip(chords, dur=PWhite(.1,.5)*1, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12) + PRand(0,1)
    b1 >> blip(chords, dur=.5*PWhite(.8,1.2), sus=linvar([.3,3],16), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
@nextBar(shift_clock(22, cshift))
def a():
    b2 >> blip(chords, dur=PWhite(.5,1.5)*clave23, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
    b1 >> blip(chords, dur=cascara*PWhite(.5,1.5), sus=linvar([.3,3],16), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
@nextBar(shift_clock(24, cshift))
def a():
    b2 >> blip(chords, dur=PWhite(.1,.5)*clave23, sus=linvar([1,10], 16), oct=7).mpan(PRand([1,2,3])).pause(4,16)
    b1 >> blip(chords, dur=cascara*PWhite(.5,1.5), sus=linvar([.3,3],16), oct=5).mpan(PRand([0,.5,3])).pause(4,16,8)
@nextBar(shift_clock(25, cshift))
def a():
    b2 >> blip(chords, dur=PWhite(.1,.5)*clave23, sus=linvar([1,10], 16), oct=7).mpan(PRand([1,2,3])).pause(4,16)
    b1 >> blip(chords, dur=cascara*PWhite(.8,1.2), sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,16,8)
@nextBar(shift_clock(27, cshift))
def a():
    b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=7).mpan(PRand([1,2,3])).pause(4,16)
    b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,16,8)
@nextBar(shift_clock(29, cshift))
def a():
    b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=7).mpan(PRand([1,2,3])).pause(4,16) + P(0,2)
    b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,16,8) + P[0, 2, 0, P(0,2)]
@nextBar(shift_clock(30, cshift))
def a():
    f1.fadeout(16)
    b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,12,6) + P[0,(0,2),P*(0,2),4] | P[0,(0,2),P(0,2),4]
@nextBar(shift_clock(32, cshift))
def a():
    b3.amplify=1
    b3.amp=1
    b3 >> digivibes(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,12,6).fadein(8) + P[0,(0,2),P*(0,2),4] | P[0,(0,2),P(0,2),4]
    b3.digivibes_fx=linvar([0,.5],32)
    b3.digivibes_sync=linvar([0,1],7)
    b3.digivibes_detune=linvar([0,.5],12)
    b3.digivibes_filter=linvar([0,1],15)
@nextBar(shift_clock(34, cshift))
def a():
    k2 >> play("V.", dur=.5, amp=1.3, crush=8, bits=6, output=10).mpan(.5)
@nextBar(shift_clock(36, cshift))
def a():
    k2 >> play("<(VVV(V[.V]V[VV]))(...V)>", dur=.5, amp=1.3, crush=8, bits=linvar([6,2],24, start=Clock.mod(4)), output=10).mpan(.5)
    k1 >> play("<v.>", dur=.5, amp=1.3, crush=0, bits=0, rate=1).mpan(.5)
@nextBar(shift_clock(38, cshift))
def a():
    k2 >> play("<(VVV(V[.V]V[VV]))(...V)>", dur=.5, amp=1.3, crush=8, bits=linvar([6,2],24, start=Clock.mod(4)), output=10).mpan(.5).pause(8,32,4)
    k1 >> play("<v.>", dur=.5, amp=1.3, crush=0, bits=0, rate=1).mpan(.5).pause(8,32)
@nextBar(shift_clock(44, cshift))
def a():
    b3.fadeout(16)
@nextBar(shift_clock(45, cshift))
def a():
    k2.ampfadeout(16)
@nextBar(shift_clock(47, cshift))
def a():
    # b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=7).mpan(PRand([1,2,3])).pause(4,16)
    # b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,16,8)
    b2 >> blip(chords, dur=PWhite(.1,.5)*clave23, sus=linvar([1,10], 16), oct=7).mpan(PRand([1,2,3])).pause(4,16)
    b1 >> blip(chords, dur=cascara*PWhite(.8,1.2), sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,16,8)
@nextBar(shift_clock(47.5, cshift))
def a():
    k1.ampfadeout(8)
@nextBar(shift_clock(49, cshift))
def a():
    b2 >> blip(chords, dur=PWhite(.5,1.5)*clave23, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
    b1 >> blip(chords, dur=cascara*PWhite(.5,1.5), sus=linvar([.3,3],16), oct=PRand([5,6,7])).mpan(PRand([0,.5,3])).pause(4,12,6)
@nextBar(shift_clock(50, cshift))
def a():
    b1 >> blip(PWhite(0,.7), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(5,7)[:16],PRand(2,6))).mpan(PRand([0,.5,3])).pause(4,12,6)
    b2 >> blip(PWhite(0,3), dur=PWhite(.1,.5)*2, sus=linvar([1,10], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).mpan(PRand([1,2,3])).pause(4,12)
@nextBar(shift_clock(51, cshift))
def a():
    b_all.ampfadeout(32)
@nextBar(shift_clock(52, cshift))
def a():
    Clock.clear()

@nextBar(shift_clock(53, cshift))
def a():
@nextBar(shift_clock(54, cshift))
def a():
#
# b1 >> digivibes(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).mpan(mrot(32)).pause(4,12,6) + P[0,(0,2),P*(0,2),4] | P[0,(0,2),P(0,2),4]
# b1.digivibes_fx=linvar([0,.5],32)
# b1.digivibes_sync=linvar([0,1],7)
# b1.digivibes_detune=linvar([0,.5],12)
# b1.digivibes_filter=linvar([0,1],15)
# b1.span(srot(32))

## # TODO:
# derandomiser mpan quand on entre dans la mélodie puis le rerandomiser au meilleur moment
# finir le morceau en rerandomisant vers la pluie mais 2x plus vite
# changer la chords progression
# faire un bon break au milieu avec un effet riser


d3 >> delikey(0, dur=PWhite(.1,.5)*2, sus=linvar([.4,2], 16), oct=var(PRand(2,4)[:16],PRand(2,6))).span(PRand([1,2,3])).pause(4,12)
d3.delikey_fx=linvar([0,1],32)
d3.delikey_fm=linvar([0,1],7)
d3.delikey_phaser=linvar([0,1],12)
d3.delikey_polydisto=linvar([0,1],15)
@nextBar(shift_clock(20, cshift))
def a():
    # Root.default = var([0,2,-2,4,0],8)


b1 >> delikey(chords, dur=cascara, sus=PWhite(.2,4)) + [0,(0,2),P*(0,2),4] | [(0,2),P(0,2),4]
b2 >> delikey(chords, dur=clave23, sus=PWhite(.2,4), oct=7, amp=[1,1,0]) + (0,2)

b_all.mpan(PRand(0,5))

b3 >> delikey(chords, dur=P[2,1,1]*2, sus=P[2,1,1]*2, oct=3).span(.5)

k2 >> play("<(VVV(V[.V]V[VV]))(...V)>", dur=.5, amp=1.3, crush=8, bits=linvar([2,6],16), output=10).mpan(.5)
k1 >> play("<v.>", dur=[3/5,2/5], amp=1.3, crush=0, bits=0, rate=1).mpan(.5)

k2 >> play("<V.>", dur=[3/5,2/5], amp=1.3, crush=4, bits=4).pause(8,32,12)
k1 >> play("<V.>", dur=[3/5,2/5], amp=1.3, crush=0, bits=0, rate=(.7,1)).pause(8,32,12)

b1 >> blip([0,1,2,0,-2,0,1,4,5,1,0,-2], dur=[.5,.25,.25,.25,.75, .5, .5, 1], sus=PWhite(.2,4))
b2 >> blip([0,1,2,0,-2,0,1,4,5,1,0], dur=[1,2,1,1,1], sus=PWhite(.2,4), oct=7) + (0,2)


b1 >> blip(0, dur=PWhite(.1,.5), sus=3, amp=PWhite(.2,1.5), oct=var(PRand(2,7)[:16],PRand(2,6))) + PRand(0,5)
