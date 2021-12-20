
Clock.bpm=sinvar([100,140,100,140],[16,16,16,inf], start=Clock.mod(4))

Clock.bpm=sinvar([100,140,100,140,10],[16]*4+[inf], start=Clock.mod(4))

Clock.bpm=100

p1 >> kit808("wwow", dur=gnawa)
p2 >> kitcuba("-o- -[--]", dur=Pvar([[1/3],gnawa],6))
d2 >> kicker([14,3], dur=1, resob_dw=.2)
d2 >> kicker(6, dur=1, resob_dw=.2)

k2 >> kora([0,2,4], dur=1/2)

b1 >>  kora([0,0,2,1,0,4],
            dur=2,
            oct=(3,5,6),
            root=var([0,0,2,0,4],6),
            vol=.9,
            amp=[.8,.6,.7],
            scale=Pvar([Scale.minor, Scale.major], 24),
            ) + P/(0,2,4)
