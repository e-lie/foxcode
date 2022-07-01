
change_bpm(162)
change_bpm(110)
change_bpm(120)

d2 >> play("<V.O..Vo.>", dur=.5, sample=2, rate=linvar([.8,1.2], 16), amp=.8)

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)
d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa32_3)
d3 >> play("<(-~)->", dur=.5, amplify=pa32_3, sample=[2,3,4])

d4 >> play("<m><([ m ][ m][  a])>", dur=1, sdb=3, amplify=po32)


l1 >> loop("200173-breakbeat5.wav", 0, rate=1.35, dur=4).only()

l1 >> loop("200173-breakbeat5.wav", 0, rate=1, dur=4)
l1 >> loop("200173-breakbeat5.wav", 0, rate=1, dur=4)

l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=1.35, dur=[4,2,2, 1, 1, 1, 1])

l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=1.35, dur=[4,2,2, 1, 1, 1, 1], pan=[1,-1], amplitude=pa32)
l2 >> loop("200173-breakbeat5.wav", [0,0,4,2], rate=1.35, dur=[4,4,3,1], pan=[-1,1], amplitude=pa16)
l3 >> loop("200173-breakbeat5.wav", [2,2,0], rate=1.35, dur=1, pan=[1,0,-1], amplitude=pa16_2)

l1.dur=clave23
l1.dur=cascara
l3.dur=cascara

d1 >> play("^", dur=clave23, sample=2)
d2 >> play("i", dur=cascara)
elp with other installations
l1 >> loop("200173-breakbeat5.wav", [1], rate=1.35, dur=[3]).fadein()

l_all.fadeout(32)

b1 >> tb303([0,2,4,7,8,2], dur=Pvar([clave23,cubalet,1/3,.25,.5,cubalet,.25], [4,2,2, 1, 1, 1, 1]), oct=3, amp=1.5) + [0,0,[0,0,1]]
b1 >> marimba([0,2,4,7,8,2], dur=Pvar([clave23,cubalet,1/3,.25,.5,cubalet,.25], [4,2,2, 1, 1, 1, 1]), oct=3, amp=1.5) + [0,0,[0,0,1]]
b1 >> marimba([0,2,4,7,8,2], dur=clave23, oct=3, amp=1.5) + [0,0,[0,0,1]]
b1.pan=var([-1,1,0,1,-1,0], 2)
b1.every(7, "stutter", 2)
b1.every(7, "stutter", 0)

b1 + P*(0,2,4,6)
b1 + P*(0,2)
b1.oct = [3,4,5]
b1.sus=linvar([.1,.5])

b1 + P*(0,2)

v2.stop()

v1.stop()
v1 >> blip([0,2,4,7,8,2], dur=clave23, sus=1/2, pan=var([-1, 1], 12), oct=[5,6,7]) + [0,0,[0,0,1]]
v2 >> click([0,2,4,7,8,2], dur=cascara, sus=1/2, pan=var([-1, 1], 12), oct=[5,6,7]) + [0,0,[0,0,1]]
Root.default = var([0,-3,5,2],8)
Root.default = var([0,2,4,6,8,10,12],8)
Scale.default = Scale.minor
Scale.default = Scale.majorPentatonic
