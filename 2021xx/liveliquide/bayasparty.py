

bb >> strings(0, dur=PSum(3,2), oct=6,**lpf(sinvar([0,.5],8))).only()

groove=sinvar([1/2,1/2.5], 16)
d1 >> kitdatai("< [--]->< s><(xxxxxxx[-X]) >", sample=var([1,2], 4), dur=groove, reverb_dry_wet=sinvar([0,.5], 8), amp=.8).only()



k2 >> kit808("< [--]->< s><x >", sample=var([1,2], 4), dur=1/2, reverb_dry_wet=.5, amp=.8, resob_dry_wet=0)
k2 >> kit808("< [--]->< s>", sample=var([1,2], 4), dur=1/2, reverb_dry_wet=sinvar([0,.5], 8), amp=.8, resob_dry_wet=.4).only()


k2.only()

d1 >> kitdatai("< [--]->< s><x >", dur=1/2)
d1 >> kitdatai("< [--](-=-[--])>< s><(xxxxxxx[ox]) >", dur=1/2)

d1 >> kitdatai(Pvar(["< ([--][---]=)(-=-[--])>< (s[ss]ss)><(xxxxxxx[ox]) >", " --"],[24,8]),
                dur=1/2,
                reverb_dw=sinvar([0,.0], 8),
                resob_dw=0)
d2 >> kit808(Pvar(["www"," "],8), dur=Pvar([[.5,.25,.25],[4/10,3/10,3/10],], 16), amp=[.5,1], reverb_dw=sinvar([0,.3],16))
d3 >> kicker((1,5)).every(32, "stutter", 2)

b1 >> crubass(Pvar([[0,2,4,0,2,3], [0,4,0,4,3,2]], 36), dur=Pvar([PSum(12,7),PSum(6,5)], 36),
                   oct=Pvar([P[3,2], [3]],12), root=var([0,4,0,0,4,5],12), scale=Pvar([Scale.minor, Scale.romanianMinor], 64), reverb_dry_wet=.5)
b2 >> ubass(Pvar([[0,2,4,0,2,3], [0,4,0,4,3,2]], 36), dur=Pvar([PSum(12,7),PSum(6,5)], 36),
                 oct=Pvar([P[3,2], [3]],12), root=var([0,4,0,0,4,5],12), scale=Pvar([Scale.minor, Scale.romanianMinor], 64), reverb_dry_wet=.5)

b3 >> tb303(Pvar([[0,0,0,2,0,0], [0,2,0,2,0,3]], 12),
            dur=1/4,
            oct=Pvar([P[3,2], [2]],12),
            root=var([0,4,0,0,4,5],12),
            scale=Pvar([Scale.minor, Scale.romanianMinor], 64),
            i_freq=linvar([.1,.7],16),
            vol=.7,
            reverb_dw=.4)


Clock.bpm = 160
Clock.midi_nudge = 0.16

g1 = Group(b3, d4)
g1.only()

drum = msm([
    ('init','xxo[-o][-o]xo[-o]'),
    ('xxo[-o][-o]xo[-o]','xxo[-o]    ', 'mod64b4r4'),
    # ('*','----ooo[ooo]','mod32r4'),
    # ('*','x-o--xo-','mod64r8'),
    # ('*','x-o-','mod128r8'),
    # ('x-o--xo-', , 'mod16'),
]).pvar
d4 >> kitdatai(drum, dur=1/2, amp=var([.8,0],[12,4]), resob_dw=.1)

mm >> mixer(drum, dur=1/2, amp=linvar([0,1],[30,inf],start=Clock.mod(4)),**lpf( sinvar([0,.1,.3,.8],[6,6,6,inf],start=Clock.mod(4)) ))
