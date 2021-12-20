Clock.bpm = 120

ch = var([0,5,2,3],[8,4,2,2])
# ch = var([0,2,5],1/2)
bb >> bass(ch, dur=PSum(3,2), oct=(4,5), amp=.7)

vv >> viola(ch + [[2,0,0],0,[0,2,2],[0,0,2]], dur=ch.dur,
            oct=(4,5)) + var([(0,2),(2,4)],[28,4])

vv.amp=var([.7,0],[48,16])

A = var([1,0],[16.5,15.5])
zz >> zap([3,2,0], dur=1/3, sus=1/2, amp=A*2, pan=1) + [0,[0,(0,2),0],0]
pp >> pluck([0,2,4,7,8,2], dur=1/2, sus=1/2, amp=A, pan=-1) + [0,0,[0,0,1]]

be >> bell([2,1,0,2,3], dur=1/2, oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])
be >> bell([2,1,0,2,3], dur=PSum(5,4), oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])

bd >> kitdatai("(x )(-[-x]-)", sample=2, dur=1/2)
cp >> play("  ( H) ")
cp >> play("  H ")
sh >> play("  s ")
sh >> play("s s( s)")
sn >> play(" (   I)I(   [II])")
tm >> play("m  m  m( [ m])")
tm.rate=(.8,1)
tm.pan=(-.5,.5)

drum = Group(bd,cp,sh,sn,tm)
drum.amplify = 1

drum.pan=PSine(32)
drum.lpf = 20000

fi >> play("ss[ss][ss]", dur=1/2, sample=5)
# fi >> play("o[oooooo]", sample=5)
fi.pan=(-1,1)
fi.rate=(.9,1)
# fi.rate=PRange(2,10)
fi.amp=var([0,1],[14,2])
