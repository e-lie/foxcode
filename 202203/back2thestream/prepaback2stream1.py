
from FoxDot.preset import *


change_bpm(120, True, 0.26)
bb >> mixer()
ss >> sends()
sc >> supercollider()

################################################################

t1 >> play('VnX(n*n/)', output=2).every(4, "stutter")
t1 >> play('Vn(VX/)( * [==])', output=2)
t1.amplify = var([1,0], [24,8])
sc.reverb_dw=.5
# sc.resob_dw=sinvar([.5,0],7)
sc.phaser_dw=.9

################################################################

s1 >> owstr([0,-2,12], oct=2, dur=4)
s1.setp(owstr_1)
s1.vol=.9

s1.i_interval = var([0,.9, .2, .7, .4], 2)

s1 >> owstr([0,2], oct=3)

s1.amplify = var([1, 0], [24,8])

s1.fadeout(16)

################################################################

d1 >> marimba([0,0,1], dur=.5, phaser_dw=.9, oct=[2,5,7]) + P*(0,4)
# d1.dur=Pvar([.5,PWhite(.2,.7)[:17]],16)
d1.amp=PWhite(.7,.9)[:17]
d1.fadein(16)
# d1.solo()
d1.degree = [0,0,1,-5,0,2,1,-3]

d2.fadeout(16)

d2 >> marimba([0,0,1], dur=cubalet, phaser_dw=0, oct=2, amp=[.8,1,.6,.4])

d2.i_bright = sinvar([.1,.8], 16)
d2.i_reverb = 0


d1.every(3,"stutter")

d1.fadeout(16)

################################################################

l1 >> loop("foxdot", P[6,7], dur=gnawa*2)
l2 >> loop("foxdot", [(6,5),7], dur=1)

print(P[0,1/3,0])

l1 >> loop("foxdot", [0,1/3,0,2/3], chop=2, amp=3, output=4)

################################################################

import requests
url = 'https://freesound.org/data/previews/616/616279_9497060-lq.mp3' # credit Erokia
sound = requests.get(url)
filename = url.rsplit('/', 1)[-1]
foxdot_loop_path = '/home/elie/Documents/2021-2022/FoxDot/FoxDot/snd/_loop_/'
filepath = foxdot_loop_path + filename
with open(filepath, 'wb') as f:
    f.write(sound.content)

################################################################

import freesound

client = freesound.FreesoundClient()
client.set_token("6MIPWRGu03npad6FYxTE1vIwUF60aD8bvuwbUBe8","token")

results = client.text_search(query="dubstep",fields="id,name,previews")

foxdot_loop_path = '/home/elie/Documents/2021-2022/FoxDot/FoxDot/snd/_loop_/'

sound = results[0]
sound.retrieve_preview(foxdot_loop_path,sound.name+".mp3")

################################################################

airwave = '621529__nlux__air-wave-03.wav' # credit nlux on freesound
coffermaker = '621309__seth-makes-sounds__keurig-single-cup-coffee-maker.wav' # credit seth make sounds on freesound

l3 >> loop(coffermaker, 5, amp=3, dur=4, output=4)
sc.resob_dw=.4
sc.phaser_dw=.5
l3.fadein(32)

l3.solo()

################################################################

l4 >> loop(airwave, [0,1,0], dur=[4,1/3,2/3])
