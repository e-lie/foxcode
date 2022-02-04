
Clock.bpm=sinvar([100,140,100,140],[16,16,16,inf], start=Clock.mod(4))

Clock.bpm=sinvar([100,140,100,140,10],[16]*4+[inf], start=Clock.mod(4))

Clock.bpm=sinvar([120,140],32, start=Clock.mod(4))

Clock.bpm=70

p1 >> kit808("wwow", dur=gnawa/1.5, resob_dw=sinvar([0,.6],8))
p2 >> kitcuba("-o- -[--]", dur=Pvar([[1/3],gnawa],6))
d2 >> kicker([14,3], dur=1, resob_dw=0)
d2 >> kicker((6,3), dur=1, resob_dw=0)

k2 >> kora([0,2,4], dur=1/2, amp=[1,.8,.9,.9,1], scale=Pvar([Scale.minor, Scale.major], 24))

b1 >>  danceorg([0,0,2,1,0,4],
                dur=2,
                oct=(3,5,6),
                root=var([0,0,2,0,4],6),
                vol=.9,
                amp=[.8,.6,.7],
                scale=Pvar([Scale.minor, Scale.minor], 24),
                danceorg_i_bright=sinvar([0,1], 16),
                ) + P/(0,2,4)

b1.stop()

p1 >> kit808("o", dur=[1/3])
p2 >> kit808("w", dur=[2/5])
p3 >> kit808("<x><V>", dur=[4,3,2])

# see braff

Clock.bpm=130

p1 >> kitcuba("oo---o oo ooxo oooo oxo o o oooxx-o o oo oo ooo", dur=cascara*4, amp=sinvar([.2,1], [5,7,9,2,7]), reverb_dw=.5)
p2 >> kit808("w ww w w www w w www www ww w", dur=clave23*2, amp=sinvar([.2,1], [5,7,9,2,7]))
p3 >> kicker((6,5), dur=1, amp=sinvar([.2,.5], [5,7,9,2,7]), reverb_dw=.6)


print(rhythms)
