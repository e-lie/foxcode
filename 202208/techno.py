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

m1 >> marimba(var([0, 3, 2, -2]), dur=var([.25, 1 / 3],
                                          [24, 8])) + [0, 2, 1, -2]
