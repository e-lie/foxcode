
Clock.bpm = 160
Clock.midi_nudge = 0.29 # bpm 120

bin3 = P[1/2,1/4,1/4]
gnawa = P[4/10,3/10,3/10]
ter3 = P[1/3,1/3,1/3]

bb >> ubass(0, dur=PSum(3,2), oct=3,**lpf(sinvar([0,.5],8)))

k7 >> kicker([0], **lpf(sinvar([0,0,.4],[22,4,6])), pan=var([-1,1], 1)).every(8, "stutter", 3)

k2 >> kitdatai("<-  >< s  >", dur=1/4, resob_dry_wet=.2)
k3 >> kitcuba("-o-", dur=gnawa, amp=var([1,1], 16), reverb_dry_wet=0)

base1 = var([0,2,0,4],4)
root1 = var([0,4,2,0],16)

b1 >> crubass(base1, dur=PSum(3,2), oct=3, root=root1, scale=Scale.minor, vol=.9)

d1 >> kitcuba(PRand(range(20))[:32], dur=gnawa, amp=Pvar([[1,.8],0],[6,2]), pan=sinvar([1,-1],4), reverb_dry_wet=expvar([0,.8],8))

k1 >> kicker([1,7], dur=1, oct=3, amp=var([1,0],[12,4])).every(8, "stutter", 3)

s1 >> strings(base1, dur=2, oct=5, root=root1, scale=Scale.minor, vol=1, amp=var([1,0], [12,4]), i_release=.8 )

k1.only()

################################################################

Clock.bpm = 110
Clock.midi_nudge = 0.30
Scale.default = Scale.major

ch = var([0,5,2,3],[8,4,2,2])
# ch = var([0,2,5],1/2)
bb >> bass(ch, dur=PSum(3,2), oct=(4,5), amp=.7)

vv >> strings(ch + [[2,0,0],0,[0,2,2],[0,0,2]], dur=ch.dur,
            oct=(5,6)) + var([(0,2),(2,4)],[28,4])

vv.amp=var([.7,0],[48,16])

A = var([1,0],[16.5,15.5])
zz >> zap([3,2,0], dur=1/3, sus=1/2, amp=A*2, pan=1) + [0,[0,(0,2),0],0]
pp >> pluck([0,2], dur=1/4, sus=1/2, amp=A, pan=-1) + [0,0,[0,0,1]]

be >> balafon([2,1,0,2,3], dur=1/2, oct=(5,6), amp=0.7) + var([0,2],[12,4.5,11.5,4])
be >> balafon([2,1,0,2,3], dur=PSum(13,4), oct=(5,6), amp=1) + var([0,2],[12,4.5,11.5,4])

k2.stop()
bd >> play("(x )(-[-x]-)", sample=2, dur=1/2)
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

fi >> play("oo[oo][oo]", sample=5)
# fi >> play("o[oooooo]", sample=5)
fi.pan=(-1,1)
fi.rate=(.9,1)
# fi.rate=PRange(2,10)
fi.amp=var([0,1],[14,2])
fi.stop()

################################################################

Clock.bpm = 120
Clock.midi_nudge = 0.29 # bpm 120

d1 >> kit808(P["x--(-[--])o--(=-)"].layer("mirror"),
    pan=sinvar([-1,1],8),
    dur=PDur(5,8),
    sample=-1,
    rate=var([1,4],[28,4])).every(5,'stutter', 0).stop()

d2 >> play(PZip("Vs", "  n "), sample=2, hpf=var([0,4000], [28,4])).every(3, 'stutter', dur=1).stop()

s1 >> owstrings((0,2,4,const(6)), dur=4, oct=(5,6,7), amp=1) + var([0,[1,-1]], 8)

d3 >> play("[--]", amp=1.5)

b1 >> crubass(var([0,[1,-1],8]), dur=PDur(5,12), amp=1, oct=3) + [0,4,const(7)]

k2 >> kora(Pvar([[0,7,6,4,2],[0,2,2,2,4]], 16), sus=2, oct=5, dur=PSum(5,3))

k1 >> karp(dur=1/4, amp=.6, oct=var([6,7]), sus=1, rate=P[:32]*(1,2), delay=(0, 1/8), lpf=linvar([400,5000],12), pan=linvar([-1,1], 8)+var([0,-1,1,-7]))

p1 >> blip([var([0,-1,-1,0],2),4,[9,7],10], oct=(6,7), amp=2, sus=2, dur=PDur(5,8) )

Scale.default = Pvar([Scale.major, Scale.minor], 16)

################################################################

Clock.bpm = 160
Clock.midi_nudge = 0.16
drum = msm([
    ('init','xxo[-o][-o]xo[-o]'),
    ('xxo[-o][-o]xo[-o]','xxo[-o]    ', 'mod16b4r4'),
    ('*','----ooo[ooo]','mod16r4'),
    ('*','x-o--xo-','mod32r8'),
    ('*','x-o-','mod64r8'),
    # ('x-o--xo-', , 'mod16'),
]).pvar
d1 >> kit808(drum, dur=1/2, amp=var([.8,0],[12,4]), resob_dw=.1)

mm >> mixer(drum, dur=1/2, amp=linvar([0,1],[30,inf],start=Clock.mod(4)),**lpf( sinvar([0,.1,.3,.8],[6,6,6,inf],start=Clock.mod(4)) ))

p3 >> kitdatai(drum, dur=1/2, amp=1, eq_freqlo=0)


bassl = msm([
    ('init', [0,4,1,4,0,2,4,2]),
    ("*", [0,0,4,2],  'mod16b4r4'),
    ("*", PWalk()[:32],  'mod32r16'),
    ("*", [10,10,14,12],  'mod64r8'),
    # ('*','----ooo[ooo]','mod16r4'),
    # ('*','x-o--xo-','mod32r8'),
    # ('*','x-o-','mod64r8'),
    # ('x-o--xo-', , 'mod16'),
]).pvar
bb >> crubass(bassl, dur=1/2, sample=var([1,2],12), scale=Scale.minor) #var([1,0],[12,4]))#var([0,1,2,3],[8,8,4,5]), dur=1/2)
b2 >> ubass(bassl, dur=1/2, sample=var([1,2],12), scale=Scale.minor) #var([1,0],[12,4]))#var([0,1,2,3],[8,8,4,5]), dur=1/2)
