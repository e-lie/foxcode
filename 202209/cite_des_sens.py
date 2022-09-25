from FoxDot.preset.common import *


        # 1 jouer des notes au piano

joueur1 >> piano(0)

joueur1 >> piano(2)

arreter() # ou CTRL + MAJ + .

joueur1 >> piano([0,2])

joueur1 >> piano([1,2,3,4,5])

## Essaye de changer les notes
## Essaye de faire une melodie qui monte et qui descend

        # 2 ajouter un deuxieme joueur qui joue en même temps

## relancer le joueur1

joueur2 >> piano(8)

joueur2 >> harp(8)

joueur1 >> blip([0,0,0,1,2,1,0,2,1,1,0], dur=[1,1,1,1,2,2,1,1,1,1,4], dur=linvar([.3,1], 8))

Scale.default = majeur

Clock.bpm = 360

joueur2 >> basse([0,4,2,0], dur=4)

joueur3

joueur1 >> harp([0,2])

## ajoute un troisieme joueur qui joue des notes à la basse

## arrete le joueur2 avec joueur2.stop()

        # 3 Tempo et longueur des notes

## Montrer, expliquer le metronome

## Lancer des joueurs

## Changer le bpm avec

Clock.bpm = 60
Clock.bpm = 180
Clock.bpm = 120 # tempo normal

## Changer la durée des notes avec dur=

joueur1 >> blip([1,2,3,4,5], dur=1/2)
joueur1 >> blip([1,2,3,4,5], dur=2)
joueur1 >> blip([1,2,3,4,5], dur=[1,2,1/2])

## Faire jouer un joueur avec la durée 1/4

## Ajouter des pauses

## Au clair de la lune

joueur1 >> blip
