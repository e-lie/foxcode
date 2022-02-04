b1 >> multibass(PWalk()[:65], dur=1 / 4, oct=3)


b1 >> crubass(PWalk()[:65], dur=1 / 4, oct=3)

print(interpolate(triplet, gnawa))
print(gnawa)

b1 >> balafon(
    PWalk()[:65], dur=var([1 / 4, 1 / 3, 1], 8), oct=6
)  # -> corriger pour avec if dur is None et pas if dur

b1 >> balafon(
    PWalk()[:65], dur=var([1 / 4, 1 / 3, 1], 8), oct=6, amp=var([1, 0], [6, 2])
)

b1 >> balafon(
    PWalk()[:65],
    dur=var([1 / 4, 1 / 3, 1], 8),
    oct=6,
    amp=var([1, 0], [6, 2]),
    delay_vol=0.5,
)

b1 >> balafon(
    PWalk()[:65],
    dur=var([1 / 4, 1 / 3, 1], 8),
    oct=(5, 6, 7),
    amp=var([1, 0], [6, 2]),
    delay_vol=0.5,
    pan=sinvar([-1, 1], 16),
    vol=0.8,
)

b2 >> sub303_2(
    PWalk()[:65],
    dur=var([1 / 4, 1 / 3, 1], 8),
    oct=3,
    tb303_i_freq=linvar([0.1, 0.6], 8),
    tb303_i_reso=sinvar([0.6, 1], 12),
    tb303_reverb_dw=linvar([0, 0.5], 6),
    pan=sinvar([1, -1], 16),
    vol=0.8,
)

d1 >> jazzkit(
    [0, 4, 12], dur=[0.5, 1, 0.3, 1.2], sus=0.1, reverb_dw=0.3, resob_dw=0.3
)
d1 >> jazzkit(
    [0, 4, 12],
    dur=P[0.5, 0.2, 0.2, 0.6, 0.3, 1.2] * 2,
    sus=0.1,
    reverb_dw=0.3,
    resob_dw=0.3,
)

help(live.track)
