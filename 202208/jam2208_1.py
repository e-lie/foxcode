w1 >> whibot([0, 2], vol=.5)


change_bpm(120)

Scale.default = Scale.egyptian
m1 >> blip([0], dur=var([.25, 1 / 3, 1 / 5]),
              oct=[4, 5, 6]).mpan(mrot(16)) + P[0, 2, 3, 4, 0, -5].stutter(4)

m2 >> ceramic(
    [0],
    dur=var([.25, 1 / 3, 1 / 5]),
    oct=[2, 3, 4],
    lpf_freq=linvar([2000, 1000], 16) / 24000,
    lpf_bw=.05,
    ceramic_mute=1,
    ceramic_tone=linvar([0,1],7),
    ceramic_mod=linvar([0,1],7),
).span(srot(16))

m2 + P[0, -2, -3, -4, 0, 5].stutter(4)

d1 >> play("x-", dur=var([.25, 1 / 3, 1 / 5])).mpan(mrot(64))
d2 >> play("V-", dur=.5)
