from FoxDot.preset import *

Scale.default = Scale.minor
change_bpm(140)

sc >> supercollider(reverb_wet=.9, reverb_size=.8)

d1 >> play("<(=[--]=[==]) >< +>", dur=.5, sdb=1, sample=3,
           rate=.2).mpan(var([4, 1], [.5,1,2,4]))

d2 >> play(
    "<(=[--]=[==]) >< +>",
    dur=var([.5, 2 / 3], [24, 8]),
    sdb=1,
    sample=3,
    rate=var([1.5, (1.5, 2)], [24, 8])
).mpan(var([2, 5], [.5, 4, .5, 2]))

d3 >> play(
    "(XXX(X[XX]X[ X])) ",
    sdb=1,
    sample=(1, 8),
    amp=4,
    lpf=200,
    formant=(0, 4),
    bits=var([16, 2], [24, 8]),
    crush=var([2, 4, 8, 16, 32, 64, 128, 256])
)

d5 >> play(
    "+++=+", dur=PSum(5, 8) / 2, sdb=1, sample=1, amp=3, rate=linvar([.8, 1.2])
)

d6 >> play(
    "(oo[oo])",
    dur=PSum(3, 8) / 2,
    sdb=1,
    sample=1,
    amp=6,
    rate=linvar([.8, 1.2])
)

m1 >>
(var([0, 3, 2, -2]), dur=var([.25, 1 / 3],
                                          [24, 8])) + [0, 2, 1, -2]

################################################################

Scale.default = Scale.minor
Scale.default = Scale.major

@nextBar()
def a():

tt >> blip([3,2,0,-2,0,1], dur=.25, sus=.2, amp=[.2,.6,.8,0,1,0,1,.8], lpf=500, amplify=2).mpan(mrot(18))

tt.amp = [.4,.8,1,1,1,1,1,.8]

tt.sus=linvar([.2,1],[8,inf], start=Clock.mod(8))

tt + [0,(0,2),0]

tt + [0,(0,4),(0,-5)]

d1 >> play("<-+>", sdb=1, sample=[1,1,3,3], rate=[.2], lpf=300)
k1 >> play("(VVV.V.)(...V.V)(....V.)", sdb=1, sample=[4], rate=1)

d1.mpan(var([4, 1], [.5,1,2,4]))

d2 >> play(
    "<(=[--]=[==]) >< +>",
    dur=.5,
    sdb=1,
    sample=3,
    rate=1.5
)

d1 >> play("<(=[--]=[==]) >< +>", dur=.5, sdb=1, sample=3,
           rate=.2).mpan(var([4, 1], [.5,1,2,4]))



@nextBar(8)
def a():
@nextBar(16)
def a():

tt >> blip([3,2,0,-2,0,1], dur=.25, sus=linvar([.2,1],8), amp=[1]*4+[1,0,1,.8], lpf=sinvar([100,10000], 2)).mpan(mrot(18))

dd >> play("X-", amp=6)


@nextBar(32)
def b():
    play("V ", lpf=400)

d1 >> play(" =", sbd=1, sample=3, rate=1.6, amp=2)
