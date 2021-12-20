
Clock.bpm=120

zdrum1 = zipvar([
('tto[-o][-o]to[-o]',15),
('[oo]t',1),
('tto[-o][-o]to[-o]',14),
('[tt][ot]',2),
('tto[-o][-o]to[-o]',14),
('<ooto>< = =>',2),
('tto[-o][-o]to[-o]',12),
(' ',4),
])
d1 >> kitdatai(zdrum1, dur=[1/3], amp=rnd([.9,.8]*5), vol=.8, reverb_dw=.5)

d2 >> kicker((1,12,6,14), amp=var([1,0],[12,4]))

b3 >> crubass_2([0,0,1], dur=[1,4/10,6/10], root=var([0,2,0,4],16),
                crubass_i_reso=sinvar([0,1],19),
                crubass_i_cutoff=sinvar([0,1],7),
                crubass_i_wt_pos=sinvar([0,1],11),
                amp=[.8,1], oct=(2,3), delay_vol=.5, pan=0, vol=1)

d3 >> kitcuba(Pvar([[11,12], [12,25]], [4,2,4,4,2]), dur=rnd5(3*[4/10,3/10,3/10]), amp=Pvar([PWhite(.3,1)[:17],[0]], [12,4]))

b3 >> crubass_2(**ZP(0,1/3,3,1/2,2,2/3,4,1.5), oct=(2,5), amp=1, delay_vol=.5, pan=sinvar([-1,1],16), vol=.8)

mm >> mixer(**lpf(linvar([0,1],[8,8,inf], start=Clock.mod(4))))
mm >> mixer()

dd >> kitcuba([30,32,30,31,25,12], dur=rnd5(microshift([1/3]*6, {0:.08, 1:.04, 3:.066, 4:.033})), amp=Pvar([PWhite(.3,1)[:17],[0]], [12,4]))

zdrum1 = zipvar([
('((oc)(oc)(oc)) (   [cc])',15),
('-[oo]t',1),
(' ',4),
('[cc]c ', 7),
('-[oo]t',1),
])
d1 >> kitdatai(zdrum1, dur=[1/3], amp=rnd([.9,.8]*5), vol=.8, reverb_dw=0)
