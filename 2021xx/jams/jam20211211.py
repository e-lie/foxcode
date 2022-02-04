
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
d1 >> kit808(zdrum1, dur=P[4/10, 3/10, 3/10]*2).solo()

d2 >> kicker((0,8), amp=var([1,0],[12,4]), reverb_dw=expvar([0,.6],4))

b2 >> crubass_2([0,1,0,4],dur=[2/4-.1,2/4+.1], oct=6, root=var([0,1,2,3], 4), amp=var([1,0],[24,8]), reverb_dw=sinvar([.3, .8], 16) )

b1 >> tb303([0,4,7], oct=Pvar([[1],[2],[3],[4]],3), dur=P[4/10, 3/10, 3/10], amp=var([1,0], 32), root=var([1,4,0],8))

b3 >> balafon(PWalk()[:457], dur=var([2/4, 2/3, 2], 8), oct=(5,6,7), amp=var([1,0],[6,2]), delay_vol=.5, pan=sinvar([-1,1],16), vol=.8)

mm >> mixer()
Clock.bpm=160
