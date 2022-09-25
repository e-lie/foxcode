

Clock.meter =(9,4)
Clock.bpm = 112
Scale.default = Scale.major

pp >> pluck(
    [4,2,3]*3+[7,5,4,2,3],
    dur=[1,1/2,1/2]*4+[1/2,1/2], # = 6 beats total
    sus=1
)

bd >> play("x.", sample=2)
hh >> play("-----.", dur=.25, sample=1)

ch = var([0,1,-2,3], [4,5])

bb >> bbass(ch, dur=PSum(3,2)/2, oct=3)
bb >> bbass(ch, dur=PSum(5,3), oct=3, slidefrom=[0,0,[0,0,1]])

sn >> play("..o."*3 + "..o.o.", sample=2, amp=.75)
sn >> play("..o...o...o..oo[ o]".replace("o","i"), sample=2, amp=.75)

fl >> play(
    "[popo]{popo}",
    amplify=var([0,1], [16,2]),
    rate=PTri(10,20)/10,
    pan=PSine()
)

cc >> charm((ch, ch+2, ch+4, 9)).offbeat()
cc >> charm((ch, ch+2, ch+4, 9), dur=PRand([1,2,1/2,1/4,1/8])).offbeat()

dd >> dirt([2,1,0,4], oct=6, dur=1/4)
dd >> dirt(
    [2,1,0,4],
    oct=6,
    dur=1/4,
    sus=1,
    hpf=PRange(9*4)*100,
    pan=var([-1, 1], [2.25]),
)

dd.degree = [2,1,0,[4,5,9,6]]


pp >> pluck(
    [4,2,3]*3+[7,5,4,2,3],
    dur=[1,1/2,1/2]*4+[1/2,1/2],
    sus=1,
    pan=(1,-1),
) + (0,9)

Scale.default = Scale.minor

pp >> pluck(
    [4,2,3]*3+[7,5,4,2,3],
    dur=[1,1/2,1/2]*4+[1/2,1/2],
    sus=1,
) + 0

ch = var([0,-1, -2, 2], [4,5])
# update players using ch

hh.stop()
sn.stop()

Scale.default = Scale.major

pp >> bell(
    [4,2,3]*3+[7,5,4,2,3],
    dur=[1,1/2,1/2]*4+[1/2,1/2],
    sus=1,
) + 0
pp.only()

cc >> charm(
    (ch, ch+2, ch+4, 9),
    dur=PRand([1,2,1/2,1/4]),
    # sus=,
).offbeat()

bb >> bbass(ch, dur=PSum(5,3), oct=3, slidefrom=[0,0,[0,0,1]])
bb.degree = ch + [0,-2,-2,-2]
bb.degree = ch + [0,5,5,-2]


bd >> play("x.", sample=2)
sn >> play("..o...o...o..oo[ o]".replace("o","H"), sample=2, amp=.75)

hh >> play("- = ", amp=1.5)

pp >> viola(
    [4,2,3]*3+[7,5,4,2,3],
    dur=[1,1/2,1/2]*4+[1/2,1/2],
    sus=1,
) + 0

cc.only()

be >> play("xxo[xoxo]xox[oo]", dur=1, rate=.25, sample=2, sus=0.1)
be >> play("(x )( x)", dur=1, rate=1, sample=2, sus=0.1)
be.rate=4

bb >> bbass(
    ch + [0,5,5,-2],
    dur=PSum(5,3),
    oct=3,
    slidefrom=[0,0,[0,0,1]]
) + [0,0,0,7,6,0,2,0,4]

ba >> pluck(dur=PSum(7,6), sus=3, pan=PWhite(-1,1)).follow(bb)
ba + PStutter([(0,9),(0,11), (0,8), (0,10)], PRand(8)[:4])

hh >> play("---[--][--]{---}{----}     ")
hh.every(2, "shuffle")

be >> play("o [of^+]", rate=[(n,n+1.2) for n in PWhite(5,10)])

lo >> play(".(..xx)", rate=3)

dd.only()

Clock.meter(4,4)
Scale.default = Scale.minor
Clock.bpm=136

kk >> klank((0,2), sus=4, lpf=PTri(40)*100, amp=1.5)

bd >> play("(X )( X)")
bd >> play("(X )( X)O( [OO])")
hh >> play(" -", amp=2)

dd >> dirt(
    [2,1,0,[4,5,9,6]],
    oct=6,
    dur=1/32,
    sus=1,
    hpf=PRange(9,4)*100,
    pan=PSine(256),
    amp=.7,
)

bd >> play("(X )( XX)(OO[OX])( X [OO])")

ch = var([0,2,3,4],4)

bb >> bbass(
    ch,
    dur=PSum(5,3),
    oct=3,
    slidefrom=[0,0,[0,0,1]]
) + [0,0,0,7,6,0,2,0,4]

bd.rate = (.9,.95)
# bd.rate = (.9,.95,2,4,.4)

bd.every(3,"reverse")
bd.every(3,"reverse",0)

bd.pan=[-1,0,1,-1]

################################################################
# Tips selection

Clock.meter = (9,4)

drum.every(n, "reverse")
drum.every(n, "shuffle")
drum.rate = (.9,1,2)
n.rate = PSine(32)
hpf=PRange(9,4)*100
lpf=PTri(40)*100

ba + PStutter([(0,9),(0,11), (0,8), (0,10)], PRand(8)[:4])

bass.dur = PSum(5,3)

ch = var([0,2,3,4],4)
ba >> pluck(ch + [0,5,5,-2]) + [0,7,5,6]

bass.slidefrom=[0,0,[0,0,1]]
