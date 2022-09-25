from FoxDot.preset import *

Scale.default = Scale.major
Root.default = 0


joueur1 = Player()
joueur2 = Player()
joueur3 = Player()
joueur4 = Player()
joueur5 = Player()
joueur6 = Player()
joueur7 = Player()
joueur8 = Player()
joueur9 = Player()
joueur10 = Player()

joueurs = Group(joueur1, joueur2, joueur3, joueur4, joueur5, joueur6, joueur7, joueur8, joueur9, joueur10)

batterie = play

joueur1 >> blip(P[0])

joueur1 >> blip(P[1,2,3,4,5,6])

joueur1 >> blip(P[1,1,2,2,3,3])

joueur1 >> blip(P[1,1,2,2,3,3], oct=5)

joueur1 >> blip(P[1,1,2,2,3,3], oct=7)

joueur2 >> blip(P[1,1,2,2,3,3], oct=3)

joueur1 >> blip(P[1,1,2,2,3,3].shuffle(), oct=7)
joueur3 >> blip(P[1,1,2,2,3,3].shuffle(), oct=5)

joueur1.dur=1
joueur2.dur=[.4, .3, .3]
joueur2.oct=[3,4,2,5]
joueur3.dur=.25

joueur2 + P(0,2,4)

joueur4 >> batterie("-(-[--]-)", rate=[1,3,5,.5,2], formant=0)
joueur4 >> batterie("X-(X[ V])(-[ =]-[=-])", sample=2, rate=linvar([1,2]), formant=linvar([0,4], 6), amp=3)

joueurs.fadeout()
joueurs.stop()

def arreter():
    joueurs.fadeout(8)
     #joueurs.stop(8)

joueurs.amp = 1

arreter()

joueurs.amp= PWhite(.2,1)

joueurs.root = Scale.minor

supercollider(sverb_dw=0, glitch_dw=0)
