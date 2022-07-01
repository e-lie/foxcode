

p2 >> play("X((   [ooiiiiXXoooooo])(I i[XXXXX]))", rate=linvar([1,2.5], 16), amp=.6)

p2 >> play("Xooo", rate=linvar([1,2.5], 16), amp=.6)

change_bpm(200)

Clock.bpm = 60
Clock.sync_to_espgrid()

p3 >> play("bonjour", rate=.5, dur=cascara)
p4 >> play("chloe", rate=1, dur=cubalet)
p1 >> play('Vi', sample=P[range(25)], sbd=2, rate=PWhite(.3,4)[:17], amp=.5).faderand()
p1.degrade()

p4 >> play("cb  b  v d x hloe", rate=PWhite(.02,-2)[:40], crush=16).faderand()


b1 >> blip([0,1,2,3], oct=[2,4,6], amp=2, sus=2, att=1, room=3, root=var(PRand(2,6)[:13], [6,4,8])).faderand(37)


f1 >> pads([0,0,2], dur=16, oct=4, amp=2)
f2 >> filthysaw([0,0,2], dur=.5, oct=7, amp=1, sus=1) + (0,2)

d1 >> play("- -=i[iii]- -  w --- - [--]-      i", crush=32, bits=linvar([2,64], 32), dur=cascara, rate=.25)
d4 >> play("V", sample=P[range(16)], rate=P[1,-1].stutter(4), crush=0, bits=16, dur=clave23)


change_bpm(120)

M = var([(0,2),(2,3)],[8,4,2,2])
m3 >> marimba2(M + [[2, 0, 0], 0, [2, 2]], dur=cascara, oct=P[5,4,7].stutter(4))

m3 + P*(0,2,4,5)
m3.oct=[2,5,8]
