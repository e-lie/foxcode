Root.default = 0
Scale.default = Scale.minor

change_bpm(110, True)

d1.stop()

d2 >> crazykit(
    "ffff f fff f ff",
    dur=cascara,
    scale=Scale.major,
    amp=PWhite(.5, 1.2)[:17],
    reverb_dw=sinvar([.2, .6], 32),
    reverb_decay=sinvar([0, .8], 16)
).span(rotrand1)

d3 >> crazykit(
    "h f hhh h ",
    dur=clave23,
    scale=Scale.major,
    amp=PWhite(.5, 1.2)[:17],
    reverb_dw=sinvar([.2, .6], 32),
    reverb_decay=sinvar([0, .8], 16)
).span(rot16)

d4 >> crazykit(
    "q q",
    dur=cascara * 4,
    scale=Scale.major,
    amp=PWhite(.5, 1.2)[:17],
    reverb_dw=sinvar([.2, .6], 32),
    reverb_decay=sinvar([0, .8], 16),
    vol=1
)

d4 >> crazykit("w ww www wwww", dur=clave23, amp=1.2)
d4.span(linvar([0, 5.9], [12, 0]))

te >> crazykit("aaa(f )", dur=Pvi(triplet, binlet, 16)).stop()
t2 >> crazykit("Hhhh").humz()
t2.phaser_dw = .6
