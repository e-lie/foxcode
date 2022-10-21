
from FoxDot.preset import *

################################################################
ouafakit, crazykit = add_chains("ouafakit", "crazykit")
bass303, hpluck, delikey = add_chains("bass303", "hpluck", "delikey")


d1 >> ouafakit([0,3], oct=3, dur=clave23, scale=Scale.chromatic)
d2 >> ouafakit(var([10,12],4), oct=4, dur=brafflet, sus=brafflet, scale=Scale.chromatic)
d3 >> play("=----", dur=[.5,.25], sample=3)
d4 >> play("v", dur=1, sample=0)
################################################################

Clock.bpm=111

d1 >> ouafakit(range(12), oct=var([3,4,5,6], 3), dur=.25, scale=Scale.chromatic)

d2 >> play("f", dur=clave23, sdb=4, sample=0, rate=[.6,.8,.7], amp=linvar([0,1],4))

d1 >> play("b", dur=[.5,1,1,.5], sdb=4, sample=0, rate=1, amp=linvar([0,1],7)).mpan(mrot(16))

d2 >> play("c", dur=cubalet*2, sdb=4, sample=0, crush=linvar([0,32],16), rate=1.2, amp=linvar([0,1],7), output=6)

d3 >> play("v", dur=var([2/3,1],16), sample=2)
d4 >> play("-", dur=var([1/3,.5],12), sample=0)

################################################################

d7 >> play("b", dur=[.5,1,1,.5], sdb=4, sample=0, rate=1, amp=linvar([0,1],7)).mpan(mrot(16))
d8 >> play("C", dur=[.5,1,1,.5], sdb=4, sample=0, rate=linvar([1,2],8), amp=linvar([0,1],7)).mpan(mrot(64))

d7 >> play("b", dur=[.5,1,1,.5], sdb=4, sample=0, cut=1, rate=1, amp=linvar([0,1],7)).mpan(mrot(16))
d8 >> play("C", dur=[.5,1,1,.5], sdb=4, sample=0, cut=2, rate=linvar([1,2],8), amp=linvar([0,1],7)).mpan(mrot(64))

################################################################

w1 >> play("B", sdb=4, dur=cascara, amp=.6, rate=1, sample=[0,1], cut=1, formant=linvar([0,4],[8,2]))
w1 >> play("B", sdb=4, dur=cascara, amp=1, rate=1, sample=[0,1], cut=1, chop=3, formant=0)

w1 >> play("B", sdb=4, dur=cascara, rate=1, sample=[0,1], cut=1, formant=0, amp=2)

w2 >> play("A", sdb=4, dur=clave23, rate=1, sample=[0,1], cut=1, formant=0)

w2 >> play("o", sdb=0, dur=1, rate=1, sample=0)

################################################################

Clock.bpm=160

r1 >> play(".a", sample=1, cut=.5, sdb=4, dur=.5)
r1 >> play("Aa", sample=1, cut=.5, sdb=4, dur=.5)
r1 >> play("(AAA[Aa])a", sample=1, cut=.5, sdb=4, dur=.5)
r1 >> play("(AAA[Aa])a", sample=1, cut=linvar([.3,2],16), sdb=4, dur=.5)

k1 >> play("v.")

r2 >> play("a", sample=1, cut=0, sdb=4, dur=2, rate=1.1)

r3 >> play("b", sample=1, cut=2, sdb=4, dur=2, rate=1)

r3 >> play("b", sample=1, cut=2, sdb=4, dur=2, rate=2)

w1 >> play("D", dur=cascara, cut=cascara, sdb=4, rate=.4, formant=4)

w2 >> play("A", dur=PSum(5,3), cut=1, sdb=4, rate=1.3, formant=4)

w3 >> play("..A...A.", dur=.5, cut=1, sdb=4, rate=1, formant=4)
w4 >> play("D....D..", dur=.5, cut=1, sdb=4, rate=.5, formant=0)
d1 >> play("X....X..", dur=.5, sdb=0, rate=1)

################################################################

bass303, fordrip = add_chains("bass303", "fordrip")

def shiftClock(time, shift):
    return min(time-shift,0)

@nextBar(2)
def a():
    w1.stop()
    # w2.stop()
    # r1.stop()
    # r2.stop()
    # k1.stop()
    Clock.meter = (4,4)
    change_bpm(160, True, .82)
    w1 >> play("B", dur=16, sdb=4, sample=[3])
@nextBar(16)
def a():
    w1.stop()
@nextBar(18)
def a():
    w1 >> play("b", dur=16, cur=4, sdb=4, sample=[3])
@nextBar(26)
def a():
    r1 >> play(".a", sample=1, cut=.5, sdb=4, dur=.5).mpan(0.2)
@nextBar(42)
def a():
    r1 >> play(".(aaa.)", sample=1, cut=.5, sdb=4, dur=.5)
    r2 >> play(".(...[aa])", sample=1, cut=.5, sdb=4, dur=.5, rate=linvar([1.1,1.5,1.5],[16,16], start=Clock.mod(4))).mpan(.8)
@nextBar(68)
def a():
    r1 >> play("Aa", sample=1, cut=.5, sdb=4, dur=.5)
@nextBar(84)
def a():
    r1 >> play("(AAA[Aa])a", sample=1, cut=.5, sdb=4, dur=.5)
@nextBar(100)
def a():
    r2.mpan(PRand(0,5))
    r1 >> play("(AAA[A.]).", sample=1, cut=linvar([.5,4],16), sdb=4, dur=.5)
    r3 >> play("(...[.a])a", sample=1, cut=linvar([.5,2],32), sdb=4, dur=.5, rate=1.1).mpan(.8)
@nextBar(132)
def a():
    r1 >> play("(AAA[A.]).", sample=1, cut=linvar([.5,4],16), sdb=4, dur=.5).pause(8,32,12)
    r3 >> play("(...[.a])a", sample=1, cut=linvar([.5,2],32), sdb=4, dur=.5, rate=1.1).pause(8,32,0)
@nextBar(164)
def a():
    k1 >> play("v.", amp=1.3).ampfadein(16)
@nextBar(196)
def a():
    r1 >> play("(DDA[A.]).", sample=1, cut=linvar([.5,4],16), sdb=4, dur=.5).pause(8,32,12)
    r8 >> play("b", dur=16, cur=4, sdb=4, sample=[3])
@nextBar(212)
def a():
    r3 >> play("b", sample=1, cut=.5, sdb=4, dur=4, rate=1).pause(6,12).mpan(.6)
@nextBar(228)
def a():
    r2 >> play("a", sample=1, cut=0, sdb=4, dur=2, rate=1.1).pause(16,24).mpan(PRand(0,5))
@nextBar(244)
def a():
    w1 >> play("D", dur=cascara, cut=cascara, sdb=4, rate=.4, formant=0, amplify=1, amp=1).mpan(mrot(12))
@nextBar(252)
def a():
    w1 >> play("(DE.D)(DDD.)D(E[DD])D", dur=cascara, cut=cascara, sdb=4, rate=.4, formant=0).mpan(mrot(24))
@nextBar(260)
def a():
    k1.ampfadeout(16)
    w1.amplify=1
    w1 >> play("(DE.D)(DDD.)D(E[DD])D", dur=cascara, cut=cascara, sdb=4, rate=linvar([.4,2],16, start=Clock.mod(4)), formant=0).mpan(mrot(24))
@nextBar(275)
def a():
    w1.solo()
@nextBar(292)
def a():
    k1 >> play("V.", sample=3, amplify=1)
@nextBar(308)
def a():
    k1 >> play("(VV[VV]V)(.)(VVVVVVV[VV])(.)", sample=3).mpan(PRand(0,5)[:16])
@nextBar(324)
def a():
    k1 >> play("<(VV[VV]V)(.[**]..)(VVVVVVV[VV])(..**)>", sample=3).mpan(PRand(0,5)[:16])
@nextBar(340)
def a():
    w1.pause(16,32,8)
    w1.cut=linvar([.5,1], 16)
    k2 >> play("=", sample=3, dur=var([.5, 1/3, 2/3],8)).mpan(PRand(0,5)[:16])
    w2 >> play("a", sample=2, sdb=4, cut=linvar([.5,2],16), dur=var([.5, 1/3, 2/3],8), rate=1, amp=1).mpan(var(range(6)))
@nextBar(372)
def a():
    k1.stop()
    w1.ampfadeout(16)
@nextBar(388)
def a():
    b2 >> bass303([0,2,3,5], dur=brafflet, vol=1.2, sus=.7, oct=5, bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).pause(4,16)
@nextBar(420)
def a():
    w1.amplify=1
    w3 >> play("..A...A.", dur=.5, cut=1, sdb=4, rate=1, amp=.7, formant=4).ampfadein(8)
    w4 >> play("D....D..", dur=.5, cut=1, sdb=4, rate=1.5, formant=0, amp=2).ampfadein(16)
    # d1 >> play("V....V..", dur=.5, sdb=0, rate=1, amp=1.2)



@nextBar(308)
def a():
@nextBar(308)
def a():
@nextBar(308)
def a():
@nextBar(308)
def a():
@nextBar(308)
def a():




# w1 >> play("DDD D[DD]", dur=cascara, cut=cascara, sdb=4, rate=linvar([.4,2],16, start=Clock.mod(4)), formant=sinvar([0,6],6))
w1 >> play("D", dur=cascara, cut=cascara, sdb=4, rate=linvar([.4,2],16, start=Clock.mod(4)), formant=0)
@nextBar(260)
def a():
w2 >> play("AAAAAAAAAAA.AA.AAAA.", dur=PSum(5,3), cut=1, sdb=4, rate=1.3, formant=4)
w3 >> play("..A...A.", dur=.5, cut=1, sdb=4, rate=1, formant=4)
    w4 >> play("D....D..", dur=.5, cut=1, sdb=4, rate=.6, formant=0)
d1 >> play("V....V..", dur=.5, sdb=0, rate=1, amp=1.2)
b2 >> bass303([0,2,4], dur=cascara, sus=.6, oct=4, bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).pause(4,16)

# @nextBar(292)
# def a():
#     r3 >> play("b", sample=1, cut=1, sdb=4, dur=6, rate=2).pause(0,12).mpan(.6)
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
@nextBar(42)
def a():
