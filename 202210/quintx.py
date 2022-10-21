from FoxDot.preset import *

marimba, marimba2, marimba3 = add_chains("marimba", "marimba", "marimba")

rdrum, rdrum2, rdrum3, = add_chains("rdrum", "rdrum", "rdrum")
bass303, hpluck, delikey = add_chains("bass303", "hpluck", "delikey")


fordrip, whibot = add_chains("fordrip", "whibot")

d1 >> rdrum("abcde", dur=cubalet, amp=PWhite(.6,.9), vol=1.5).span(expvar([0,3,.5,4], [16,.5]))

b1 >> blip(0, dur=var([1/3,1/6], 5)) + P(0,7)


k1 >> delikey([0,2,-2,0,2], dur=cascara, oct=4, delikey_polydisto=linvar([0,1],16))

Clock.bpm=130

Root.default = var([0,4,-1,3,-2], 25)

m1 >> marimba([0,0,0,0,2]).span(expvar([0,2,0])) + var([0,4,-1,3,-2], 5)
m1 >> marimba([0,0,0,0,2]).span(expvar([0,2,0])) + var([0,4,-1,3,-2], 5)
m2 >> marimba([4,0,0,0,-2], oct=4).span(var([3,1], 8)) + var([0,4,-1,3,-2], 5)
m3 >> marimba2([4,0,0,0,-2], oct=4).span(var([3,1], 2)) + var([0,4,-1,3,-2], 5)

m_all.amp = PWhite(.6,1)
m_all.amplify = linvar([.2,1.3],25)
m1.dur = Pvar([[.98,1,1.02,1,1], clave23], 15)
m2.dur = Pvar([[.48,.5,.52,.5,.5], cascara], 15)

d1 >> marimba("aa[abcde]a(bbbb[cc])", root=0, dur=1, scale=Scale.egyptian)

m1 >> marimba([0,0,0,0,2])

################################################################

# Partir sur une sorte de solo de batterie en quintuplets, faire rentrer des blip ou autre sons très numériques avec une descente de quinte
# finir en accélérant/ faisant des trucs vraiment impossible pour un humain voire en ajoutant des effets artificiels

change_bpm(80)
Clock.bpm = linvar([80,200], [16,inf], start=Clock.mod(4))
change_bpm(100)

d1 >> rdrum("b", root=0)
d1 >> rdrum("c", root=0)
d1 >> rdrum("f", root=0, amp=PWhite(.4,1.1))
d1 >> rdrum("e", root=0, amp=PWhite(.4,1.1))


d1 >> rdrum("gh", dur=1/5, root=0, amp=PWhite(.4,.9))
d1 >> rdrum("h", root=0, amp=PWhite(.4,1.1))


d1 >> rdrum("aaa a a aa a aa aaaa", dur=[3/5,2/5], root=0, amp=[.9,1,.95]).span(0)
d2 >> rdrum2("ghg hg gh  ghh hgg hg hg", dur=1/5, root=0, amp=PWhite(.4,.9)).span(1)
d3 >> rdrum3("f (EFfEE)  ", dur=1/5, root=0, amp=PWhite(.4,.9), vol=1.3).span(.5)

d3 >> play("Vv", dur=.5)

d_all.amplify=sinvar([.5,1.6],[16,7])

b1 >> blip(Scale.chromatic, dur=Pvar([[3/5,2/5],1/5],5), sus=.5, scale=Scale.egyptian)

m1 >> marimba("abcA", dur=cubalet, amp=PWhite(.4,.9))
d1.vol=1

d1 >> rdrum("a  aa", dur=1/5, root=0, amp=[.9,1,.95]*PEuclid(7,15), amplify=1).span(0)
d2 >> rdrum2("g", dur=1/8, root=0, amp=[.9,1,.95]*(PEuclid(8,15)[1:]|PEuclid(8,15)[0]), amplify=1).span(1)
print(PEuclid(7,15))

################################################################



@nextBar()
def a():
Clock.meter = (5,4)
change_bpm(140, True, .82)
d1 >> rdrum("aaa a a aa a aa aaaa", dur=[3/5,2/5], root=0, amp=[.9,1,.95]).span(0)
d2 >> rdrum2("ghg hg gh  ghh hgg hg hg", dur=1/5, root=0, amp=PWhite(.4,.9)).span(1)
d3 >> rdrum3("f (EFfEE)  ", dur=1/5, root=0, amp=PWhite(.4,.9), vol=1.3).span(.5)
d_all.amplify=linvar([.3,1.5,0],[10,0,inf], start=Clock.mod(5))

@nextBar(25)
def a():
    d_all.stop()
    change_bpm(80, True, .82)
@nextBar(30)
def a():
    d_all.amplify = 1
    d1 >> rdrum("a", dur=[3/5,2/5], root=0, amp=PWhite(.9,1)).span(.5)
@nextBar(50)
def a():
    d1 >> rdrum("aaa.aa.aba..aaab.baaa", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1)).span(.2)
@nextBar(70)
def a():
    d1 >> rdrum("a.[aa][bb]a.a[aa]aa[aa][aa]b", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1)).span(0)

@nextBar(95)
def a():

d1 >> rdrum("aaaa.aaaaaaaaa", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1), vol=1.2).span(0)
# d2 >> rdrum2("ghgghghh.hggg.", dur=2/5, root=0, amp=PWhite(.8,1.1)).span(1).ampfadein(10)
b1 >> blip([0,0,0,1,-2], sus=[3,1,.7], dur=Pvar([1, 1/3, [3/5,2/5]], 5), oct=(8,9)).mpan(PRand(0,4))
b1 >> marimba([0,0,0,1,-2], sus=[3,1,.7], dur=Pvar([1, 1/3, [3/5,2/5]], 5), oct=(8,9)).mpan(PRand(0,4))
m1 >> marimba([0,0,0,1,-2], dur=Pvar([1, 1/3, [3/5,2/5]], 5), oct=[4,5]).span(.5)

Scale.default = Scale.egyptian
Root.default = var([0,4,-1,3,-2,2,-3,1],10)
b1 >> blip([0,2,-2,4,0], sus=[3,1,.7], dur=[.5])
d1 >> rdrum("a.[aa][bb]a.a[aa]aa[aa][aa]b", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1)).span(expvar([0,5],25))
d1 >> rdrum("a[a]ab", dur=[2/5,1/5,2/5], root=0, amp=PWhite(.8,1.1)).span(expvar([0,5],25))
# Clock.bpm = linvar([80,100], [15,inf], start=Clock.mod(5))
k1 >> play("V-V*V.-V*.", dur=.5, amp=1.3)

# k1 >> play("V-V*V.-V*.", dur=[3/5,2/5], amp=1.3, crush=4, bits=4).pause(8,32,12)
k1 >> play("(VVV[vv])-V*V.-V(*[**]).", dur=[3/5,2/5], amp=1.3, crush=4, bits=4).pause(8,32,12).mpan(PRand(0,5))
k2 >> play("X.", dur=.5, amp=1.3, crush=0, bits=4).pause(4,16,10)
k2 >> play("(XXX[XX]).", dur=.5, amp=1.3, crush=0, bits=4).pause(4,16,10)
change_bpm(100, True, .82)
change_bpm(120, True, .82)
change_bpm(160, True, .82)

k3 >> play(".-", dur=1, rate=1.5).mpan(PRand(0,5))
k2 >> play("V....V.V..", dur=1)
k2 >> blip(0, dur=[5,2,3], oct=(3,4))

change_bpm(140, True, .82)

b2 >> bass303([0,2,0,0,4], dur=var([1/3,1],5), sus=.7, oct=4, bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).pause(0,16)
b2.only()
### Wait for 8 beats
