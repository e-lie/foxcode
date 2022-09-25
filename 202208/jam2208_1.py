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

d2 >> play("<v.><.(-[-i]-[-i]---[ii])>", dur=.5, amplify=pa16, sample=2, amp=PWhite(.8,1.1)[:17]).mpan(mrot(16))
d3 >> play("*", dur=cascara, amp=2, amplify=po16).mpan(mrot(10))

d3 >> play("*", dur=cascara, amp=3, amplify=1, rate=PWhite(4,7)).mpan([0,1])
d4 >> play("V", dur=clave23, amp=1, amplify=1, rate=.9).mpan(.5)

################################################################

m1 >> ceramic([0,2,3,-2], dur=PSum(5,3), oct=var([4,5],3), reverb_wet=1, reverb_size=.7)
m2 >> ceramic([0,2,3,-2], dur=PSum(3,2), oct=4, reverb_wet=1, reverb_size=.7)
m1.span(srot(16))



change_bpm(160)
