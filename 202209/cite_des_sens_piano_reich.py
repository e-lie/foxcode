from FoxDot.preset import *



joueur1 >> blip([0, 1, -2], dur=1/2)

joueur1 >> epiano([5,12,1], dur=1/2) + P*(0,2)

joueur2 >> epiano([5,12,1], dur=1/20, oct=var([3,4,5,6,7], 4), amp=2, amplify=linvar([0,1], 16)) + P(0,2)

joueur3 >> supersaw([5, 12,1], dur=1, oct=[5,6,7], amp=1) + P(0,-2)

joueur4 >> epiano([5, 12,1], dur=1, oct=(2,3), amp=2) + [(0,2),P*(0,2)]

joueur5 >> batterie("<liyanna><aziza>", amp=1, dur=cascara)

joueur6 >> batterie("V", amp=1, dur=clave23)

arrêter()

joueurs.stop()


Gamme.default=Pvar([mineur, majeur, pentatonique], 16)

Root.default = var([0,-2,-3,-4], 12)

joueur1 >> marimba([0, 1, -2, 4], dur=[1/2]*3+[1], amp=2, oct=8)

joueur2 >> blip([0, 1, -7], dur=PSum(3,2), oct=(4,5), amp=2)

joueur5 >> epiano([0, 1, -2], dur=[1/4]*7+[2], oct=(3,7), crush=32)

joueur9 >> blip([0, 1, -2], dur=cascara, oct=[8], crush=0, sus=linvar([.1,3], 32))

joueur2.pause(4,16)
joueur1.pause(2,8,3)

joueur3 >> batterie("X([oo])(O--[--])", dur=clave23, sample=var([0,1,2,3]), amp=.8, crush=linvar([0,32], 128))

joueur5 >> batterie("X   X V    X ", dur=1/4, sample=0, amp=.8, crush=0)
joueur6 >> batterie("xx ", dur=1/4, sample=0, amp=.8, crush=0)

joueur4 >> batterie("( cC C C[CCCc][ccccccC][OoO])(Oc-[-c])", dur=cascara, sample=0, amp=.8, crush=linvar([0,16], 32))

joueur6 >> batterie("X(    )", dur=clave23, sample=2)

[1/2]*3+[1]

joueur7 >> batterie(" (   [***])", dur=clave23, sample=2, amp=4)

joueur6 >> noisynth([0,2,-2], dur=2)
