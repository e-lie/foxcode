from FoxDot.preset import *

p1 >> play("X ", dur=.5, output=2)

pp >> sca()

p2 >> marimba(
    "abcaca",
    oct=var([3, 4], 16),
    root=var([0, 4, 2, -5], 4),
    output=2,
    amp=PWhite(1, .6)[:187],
    dur=cubalet,
    scale=Pvar([Scale.major, Scale.minor], 6),
    reverb_wet_amount=.4,
    reverb_decay_time=2,
    reverb_room_size=2,
)
