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

change_bpm(100, True, .82)
change_bpm(80, True, .81)

k1 >> play("V-V*V.-V*.", dur=.25, amp=.8)
k2 >> play("xxx[xx]x.x[xx].xxx[xx]x[xx]xxx", dur=[3/5,2/5], amp=1)
d2 >> rdrum2("afaea.fae.", dur=.25, amp=1)

d1 >> rdrum("a.[aa][bb]a.a[aa]aa[aa][aa]b", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=PWhite(.8,1.1)).span(0)

d2 >> play("<x-x--><(v....)....>", dur=1/5, root=0, amp=PWhite(.8,1.1))
b2 >> bass303(chords, dur=var([2/5,1/5],5), sus=.4, oct=var([5],10), bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).pause(0,16)
b2 + [2,1,0,2,4]

d2 >> play("<x-x--><(v....)....>", dur=var([1/5,1/4,1/3],[5,3,2]), root=0, amp=PWhite(.8,1.1))


d2 >> play("<x-x-><(v...)...>", dur=1/4, root=0, amp=PWhite(.8,1.1))
d2 >> play("<x--><(v..)..>", dur=1/3, root=0, amp=PWhite(.8,1.1))

d3 >> play("o*[oo]m", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=PWhite(.8,1.1))

d2 >> play("X(xx[xx])(*.[oo]x.)", dur=1/3)

chords = var([0,5,-2,2,3,-4],[10,5,5,2.5,2.5,5])
Scale.default = Scale.major

b1 >> blip(chords, dur=var([1/5,2/5,1/4],5), sus=linvar([.3,3],16), oct=7) + [0,[0,1],[0,2,4],-2,1]
d2 >> delikey(chords, dur=var([1/5,2/5,1/4],5), sus=linvar([.3,3],16), oct=5) + [0,[0,1],[0,2,4],-2,1]

b2 >> blip(chords, dur=1/5, sus=linvar([.3,3],16), oct=7) + (P[0,[0,1],[0,2,4],-2,1]+ var([2,-4]))

b1 >> blip(chords, dur=1/5, sus=linvar([.3,3],16), oct=7) +
m1 >> marimba(chords, dur=2/5, sus=linvar([.3,3],16), oct=P[4,5].stutter(2))


################################################################


from FoxDot.preset import *

bass303, rdrum, rdrum2, marimba = add_chains("bass303", "rdrum", "rdrum", "marimba")
hpluck, delikey, crazykit = add_chains("hpluck", "delikey", "crazykit")

change_bpm(140, True, .82)

def shift_clock(time, shift):
    time *= 5
    return max(time-shift,0)

cshift = 0


@nextBar(shift_clock(0, cshift))
def a():
Clock.meter = (5,4)
change_bpm(140, True, .82)
d1 >> rdrum("aaa a a aa a aa aaaa", dur=[3/5,2/5], root=0, amp=[.9,1,.95]).span(0)
d2 >> rdrum2("ghg hg gh  ghh hgg hg hg", dur=1/5, root=0, amp=PWhite(.4,.9)).span(1)
d3 >> rdrum3("f (EFfEE)  ", dur=1/5, root=0, amp=PWhite(.4,.9), vol=1.3).span(.5)
d_all.amplify=linvar([.3,1.5,0],[10,0,inf], start=Clock.mod(5))
@nextBar(shift_clock(5, cshift)) # 25 beats later
def a():
    d_all.stop()
    change_bpm(80, True, .82)
@nextBar(shift_clock(6, cshift))
def a():
    d_all.amplify = 1
    d1 >> rdrum("a", dur=[3/5,2/5], root=0, amp=PWhite(.9,1)).span(.5)
@nextBar(shift_clock(10, cshift))
def a():
    d1 >> rdrum("aaa.aa.aba..aaab.baaa", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1)).span(.2)
@nextBar(shift_clock(14, cshift))
def a():
    d1 >> rdrum("a.[aa][bb]a.a[aa]aa[aa][aa]b", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1)).span(0)
@nextBar(shift_clock(19, cshift)) # 25 beats later
def a():
    pass

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
# Clock.bpm = linvar([1480,100], [15,inf], start=Clock.mod(5))
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

b2 >> bass303(chords, dur=var([2/5,1],5), sus=var([1/2,1.02],5), oct=var([4,5],10), bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).pause(0,16)
b2 + [2,1,0,P*(0,2,1),4]

################################################################

change_bpm(120)

d1 >> rdrum("aaa a a aa a aa aaaa", dur=[3/5,2/5], root=0, amp=[.9,1,.95]).span(0)
d1 >> rdrum("a", dur=[3/5,2/5], root=0, amp=[.9,1,.95]).span(0)
d1 >> rdrum("a", dur=[1/5,2/5,2/5], root=0, amp=[.9,1,.95]).span(0)
# d1.fadein(10)
d2 >> rdrum2("gh(.g)h[gh]", dur=1/5, root=0, amp=PWhite(.4,.9)*sinvar([.3,1.2],[2,1,5,1,3])).span(1)
d3 >> play("oo(.o)o[oo]", dur=1/5, root=0, amp=PWhite(.1,.9)*sinvar([.1,1.2],[2,1,5,1,3]), sample=3, crush=16).span(1)



d2 >> rdrum2("ghg hg gh  ghh hgg hg hg", dur=1/10, root=0, amp=.7).span(1)
# d2.ampfadein(10)
# d3.ampfadein(10)
d3 >> rdrum2("f (EFfEE)  ", dur=1/5, root=0, amp=PWhite(.4,.9), vol=1.3).span(.5)

d_all.ampfadeout(2)

################################################################

def shift_clock(time, shift, factor=10):
    time *= factor
    shift *= factor
    return max(time-shift,0)

cshift = 0

change_bpm(80, True, .81)
change_bpm(80)
Clock.meter = (5,4)

@nextBar(shift_clock(0, cshift))
def a():
    d1 >> rdrum("a", dur=[1.5/5,1/5], scale=Scale.major, root=0, amp=PWhite(.8,1.1), vol=1.2).span(.5)
    d2 >> rdrum2("gfg", dur=[.5/5,1/5], scale=Scale.major, root=0, amp=PWhite(.8,1.1), vol=1.2).span(.5).ampfadein(10)
@nextBar(shift_clock(1.8, cshift))
def a():
    d1.stop()
    d2.stop()
@nextBar(shift_clock(2, cshift))
def a():
    d1 >> rdrum("a", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1), vol=1.2).span(.5)
    d2 >> rdrum2("<...........d>", dur=[3/5,2/5], root=0, amp=1.1, vol=1.2).span(1)
@nextBar(shift_clock(4, cshift))
def a():
    d2 >> rdrum2("<......c....d>", dur=[3/5,2/5], root=0, amp=1.1, vol=1.2).span(0)
@nextBar(shift_clock(6, cshift))
def a():
    d2 >> rdrum2("<......c...[dd]d>", dur=[3/5,2/5], root=0, amp=1.1, vol=1.2).span(1)
@nextBar(shift_clock(7, cshift))
def a():
    d2 >> rdrum2("<......c...[dd]d>", dur=Pvar([[3/5,2/5],[1/5]], [7,3]), root=0, amp=1.1, vol=1.2).span(0)
@nextBar(shift_clock(9, cshift))
def a():
    d1.stop()
    d2 >> rdrum2("......c...[dd]d", dur=[3/5,2/5], root=0, amp=1.1, vol=1.2).span(0)
@nextBar(shift_clock(9.5, cshift))
def a():
    d2 >> rdrum2(".[fg]gf...c...[dd]d", dur=[3/5,2/5], root=0, amp=1.1, vol=1.2).span(0)
@nextBar(shift_clock(11, cshift))
def a():
    d1 >> rdrum("a", dur=1/5, root=0, amp=PWhite(.8,1.1), vol=1.2).span(.5)
@nextBar(shift_clock(13, cshift))
def a():
    d2 >> rdrum("<..(cc[.c][cd])>", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1), vol=1.2).span(1)
@nextBar(shift_clock(15, cshift))
def a():
    d1 >> rdrum("a", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1), vol=1.2).span(.5).pause(5,25)
@nextBar(shift_clock(16, cshift))
def a():
    chords = var([0,5,-2,2,3,-4],[10,5,5,2.5,2.5,5])
    Scale.default = Scale.major
    # Scale.default = Scale.chromatic
    # b1 >> hpluck(chords, sus=1, dur=var([1/5,2/5],10), oct=4).span(srot(25))
    b1 >> hpluck(chords, dur=[2/5], sus=2, oct=4, amp=PWhite(.7,1)).fadein(10) + [0,[1,2,-2,-1]]
@nextBar(shift_clock(18, cshift))
def a():
    b2 >> blip(chords, sus=1, dur=var([1/5,2/5],10), oct=7, amp=.2).mpan(PRand(0,5))
@nextBar(shift_clock(19, cshift))
def a():
    b2 >> blip(chords, sus=1, dur=var([1/5,2/5],10), oct=7, amp=.2).mpan(PRand(0,5)) + P*(0,4,-5)
@nextBar(shift_clock(21, cshift))
def a():
    b1.amp=sinvar([.2,.8,.3,.4], [3,2,5])
    b1.pause(10,25)
    b2.pause(15,25,15)
@nextBar(shift_clock(23, cshift))
def a():
    d2 >> play("<x-x--><(v....)....>", dur=1/5, root=0, amp=PWhite(.8,1.1)).ampfadein()
@nextBar(shift_clock(24, cshift))
def a():
    d3 >> play("ccmc", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=PWhite(.8,1.1)).mpan(PWhite(.4,1))
@nextBar(shift_clock(26, cshift))
def a():
    d3 >> play("ccm(c[cc])", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=2).mpan(PWhite(.4,1))
@nextBar(shift_clock(27, cshift))
def a():
    # b1 >> hpluck(chords, dur=[1/5,2/5], sus=.5, oct=4, amp=PWhite(.7,1)) + [0,0,0,0,[2,0,4,-2,0]]
    # b1 >> hpluck(chords, dur=[4/5], sus=2, oct=4, amp=PWhite(.7,1)) + [0,0,0,0,[2,0,4,-2,0]]
    b1 >> bass303(chords, dur=[1/5], oct=[4,5], amp=PWhite(.7,1), vol=.6).span(srot(25)) + [0,[1,2,-2,-1]]
    b1 >> bass303(chords, dur=[1/5], oct=[4,5], amp=PWhite(.7,1), vol=.6, bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).span(srot(25)) + [0,[4,0,-3,1,-1]]
    # b1.reset()

b2 >> epiano(chords, sus=1, dur=var([1/5,2/5],10), oct=7).mpan(PRand(0,5)) + P*(0,4,7,11)

b1 >> bass303(chords, dur=[1/2], oct=[4,5], amp=PWhite(.7,1), vol=.6, bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).span(srot(25)) + [0,[4,0,-3,1]]

k1 >> play("(VVV[vv])-V*V.-V(*[**]).", dur=[1.5/5,1/5], amp=1.3, crush=4, bits=4).pause(8,32,12).mpan(PRand(0,5))


@nextBar(shift_clock(26, cshift))
def a():
    b_all.only()



@nextBar(shift_clock(28, cshift))
def a():
@nextBar(shift_clock(28, cshift))
def a():
@nextBar(shift_clock(28, cshift))
def a():


d4 >> play("V-", rate=1)

change_bpm(80)

d2 >> play("<x-x--><(v....)....>", dur=1/5, root=0, amp=PWhite(.8,1.1)).ampfadein()

d3 >> play("o*[oo]m", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=PWhite(.8,1.1), sample=3)
d3 >> play("o=[oo]*", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=PWhite(.8,1.1), sample=3).stop()
d3 >> play("ccmc", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=PWhite(.8,1.1))
d3 >> play("ccm(c[cc])", dur=Pvar([[3/5,2/5],[1/5,1/5,2/5],[3/5,4/5]],[10,2.5,5]), root=0, amp=2)

d1 >> rdrum("aaaa.aa[aa]aaaaaa", dur=[3/5,2/5], root=0, amp=PWhite(.8,1.1), vol=1.2).span(0)
d1 >> rdrum("a([cc]ac)aa", dur=[3/5,2/5], root=0, scale=Scale.chromatic, amp=PWhite(.8,1.1), vol=1.2).span(0)
d1 >> rdrum("a([cc]ac)aa", dur=[1/5], root=0, scale=Scale.chromatic, amp=PWhite(.8,1.1), vol=1.2).span(0)
d1.vol=1.2
d1.stop()

k1 >> play("(VVV[vv])-V*V.-V(*[**]).", dur=[1.5/5,1/5], amp=1.3, crush=4, bits=4).pause(8,32,12).mpan(PRand(0,5))

k1 >> play("V-V*V.-V*.m*V-V*V.-V", dur=[1.5/5,1/5], amp=1, crush=4, bits=4, amplify=1).mpan(.5).stop()
k2 >> play("Ooooo", dur=.5, amp=1, crush=4, bits=4, amplify=1).mpan(.5)

k1 >> play("V-Vm(*.)", dur=[1.5/5,1/5], amp=1, crush=4, bits=4, amplify=1).mpan(.5)
b1 >> blip(chords, dur=1/4, sus=linvar([.3,3],16), oct=7) + [0,[0,1],[0,2,4],-2]

k1 >> play("V-Vm(*.)m", dur=[1.5/5,1.5/5,1/5], amp=1, crush=4, bits=4, amplify=1).mpan(.5)
b2 >> blip(chords, dur=1/5, sus=linvar([.3,3],16), oct=7) + [0,[0,1],[0,2,4],-2]

k2 >> play("O.((oo[oo]))", dur=1/3, amp=1, crush=4, bits=4, amplify=1).mpan(.5)

Scale.default = Pvar([Scale.major, Scale.minorPentatonic, Scale.chromatic, Scale.minor], 5)
b1 >> blip(chords, dur=1/5, sus=linvar([.3,3],16), oct=7) + [0,[0,1],[0,2,4],-2,1]
b1 >> blip(chords, dur=var([1/5,2/5,1/4],5), sus=linvar([.3,3],16), oct=7) + [0,[0,1],[0,2,4],-2,1]

b2 >> bass303(chords, dur=var([2/5,1/5],5), sus=.2, oct=var([5],10)) + [2,1,0,2,4]
b2 >> bass303(chords, dur=var([2/5,1/5],5), sus=.4, oct=var([5],10), bass303_cutoff=linvar([0,1], 20), bass303_decay=0, bass303_reso=linvar([.5,1],15)).pause(0,16)
