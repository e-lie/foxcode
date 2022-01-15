

p1deg = zipvar([
("oo---o oo ooxo oooo oxo o o oooxx-o o oo oo ooo",4),
(" ",4),
("oo---o oo ooxo oooo oxo o o oooxx-o o oo oo ooo",12),
(" ",12),
])
p1dur = zipvar([
(cascara*4,8),
(1/4,8),
(1/6,4),
(gnawa*2,12),
])
p1 >> crubass(
    p1d,
    dur=p1dur,
    amp=sinvar([.2,1], [5,7,9,2,7]),
    reverb_dw=.2,
    oct=[2,3,4],
)
#

p2 >> kit808("w", dur=clave23*4, amp=sinvar([.2,1], [5,7,9,2,7]))
p3 >> kicker([(6,5),(1,3,12)], dur=Pvar([[2/3],[1],[4/3]],16), amp=sinvar([.2,.8], [5,7,9,2,7]), reverb_dw=.6)
