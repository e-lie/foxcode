p2 >> play("<[--]><**o*>", sample=2).mpan(P[range(6)].stutter(3))
p1 >> play("<[.o].......><     (*[**])          >").mpan(1)
p3 >> play("Vvvv", dur=.25).mpan(3)
p2.amplify = pa32

p_all.sample=var([0,1,3], 32)
p_all.amplify=pa16

b1 >> blip(PRand(7), root=var([0, 2, 4], 16), dur=.25,
           oct=var([4, 5, 6], 32)).mpan(P[range(6)].stutter(4))
b1.fadein(32)

b1 >> blip([0, 2, 6], dur=.25,
           root=var([0, 2, 4], 16)).mpan(0) + [0, P/(1, 2), (2, 4), (0, 2, 6)]

b1.oct = P[4, 5, 7].stutter(7)

p_all.amp = .3

# player starts in 16 beats at the beginning of the bar
p5.nx(16).stop >> play()

# player start in 4 beats and will stop 16 beats later
p5.nsp(16, 4) >> play()

# start in 16 beats stop after 64 beats by fading on 32 beats
p5.nspf(64, 16, 32)

p5.nx(16) >> play()

p3 >> play("TT", sample=PTri(4).stutter(4), dur=cubalet).mpan(drot(P[23,8,48]))

p3.stop(2)

## TODO:
# - [x] integrate presets
# - [x] mpan(0) as default
# - test reaper effect presets
# - [x] stop(16)
# - nx as player method
# - fix bug of mpan with P(0,2) to use multiple speakers
# - [x] try a jam with named players and groups
# - [ ] find funny names
# - fx activation feature
