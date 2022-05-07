change_bpm(110)
sc >> supercollider(reverb_wet=0).fadein(16)
mi >> mixer()
wh >> uber(feedback=0)  #sinvar([.7, .9], 8))
sv >> sverb()
de >> delay()
tx >> tex()
sh >> shim(mix=1)

e6 >> crazykit("uU", dur=8).span(linvar([0, 5.9], 8))
e6.fadein(32)  ####

e2 >> crazykit(
    "fF",
    # "F",
    dur=P[7, 1, 8, 3, 5]/2,
    dur=cascara,
    amp=[.6, .7, .9, 1.23],
    scale=Scale.major
)
e2.span(rotrand2)

d3 >> crazykit(
    # "H(H)",
    "hh(hhhy)",
    dur=cubalet,
    oct=3,
    amp=[.9, 1.22] * PWhite(.7, 1)[:17],
    amplify=pa32,
    phaser_wet=1,
    phaser_freq=sinvar([0, 20000], 7),
    phaser_rate=sinvar([0, 16], 17),
    phaser_depth=sinvar([0, 11000], 32),
    phaser_feedback=sinvar([0, 1], 8),
).every(8, "stutter", 2)

e2.phaser_dw = sinvar([0, .6], 17)

k1 >> kicker(
    "<(ad) ><b( B)>",
    dur=.5,
    # dur=clave23,
    shim=.2,
).span(rot16)

b1 >> crubass(
    [0, 2, 4, 0, 2, 4, 0, 2, 5],
    dur=PSum(3, 2),
    #dur=PSum(3, 2),
    oct=2
)

d4 >> crazykit(
    "tTTtT",
    dur=cascara,
    phaser_wet=0,
    phaser_dry=1,
    amplify=pa16,
    shim=.5,
    reverb_wet=.5,
)
d2 >> crazykit("wwW", dur=clave23)

Clock.bpm = bpmto(100, 16)

change_bpm(100, True)

Scale.default = Scale.majorPentatonic

k1.sfadeout(16)
k1.only()
