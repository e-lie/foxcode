



ch = var([0,5,2,3],[8,4,2,2])
ch = var([0],[4])


dd >> bells(P[0,2,6,2,0], dur=PSum(5,4), sus=PSum(5,4)-0.05) + Pvar([(2,4),(-1,2),(-2,4)],[13,13,4], amp=[1,.5,.7,1])

ff >> play("X ")

Scale.default = Pvar([Scale.minor,Scale.major],6)

cc >> kitdatai([0,1], scale=Scale.chromatic, oct=3)

bb >> sawbass(ch, dur=PSum(3,2), sus=PSum(3,2)-0.01, oct=(2,3), pan=0, vol=.6, scale=Scale.major)

vv >> strings(ch + [[2,0,0],0,[0,2,2],[0,0,2]], dur=ch.dur, sus=ch.dur-0.05,
            oct=(3,4)) + var([(0,2),(2,4)],[28,4])

bb >> sawbass([[2,0,0],0,[0,2,2],[0,0,2]], oct=3, dur=1, sus=1-0.05) + var([(0,2),(2,4)],[28,4])

vv.amp=var([.7,0],[48,16])

b1 >> opbass([0,2,2,3], dur=P[3,3,5,5]/8, oct=3, sus=P[3,3,5,5]/8-0.05, root=var([0,2,5,0]))
b1 >> opbass(Pvar([[0,2,0,2,3],[0,0,3,2,3]],8), dur=PSum(5,3), oct=2, sus=PSum(5,3)-0.05, root=var([0,2,0,5], scale=Scale.majorPentatonic))

b1 >> opbass(Pvar([[0,1,4,0,1,4,4,0],P[0,2,4,0,5,4,4,0].reverse()],16), dur=Pvar([PSum(6,4), PSum(5,4)], 12), oct=2, sus=Pvar([PSum(6,4)-0.05, PSum(5,4)-0.05], 12), root=var([0,1,4,0],4), scale=Scale.majorPentatonic)
d2 >> play("<V ><X >", dur=1/2, sample=2)


d1 >> play("o-o---o----=", dur=[4/10,3/10,3/10], amp=[.8,.8,1.5])

print(PSum(5,3))

A = var([1,0],[16.5,15.5])
zz >> zap([3,2,0], dur=1/3, sus=1/2, amp=A*2, pan=1) + [0,[0,(0,2),0],0]
pp >> pluck([0,2], dur=1/4, sus=1/2, amp=A, pan=-1) + [0,0,[0,0,1]]

be >> bells([2,1,0,2,3], dur=1/2, oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])
be >> bells([2,1,0,2,3], dur=PSum(5,4), oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])

d1 >> kitdatai([0,1,2], channel=2, dur=1/2, scale=Scale.chromatic)

Scale.default.set(Scale.chromatic)
