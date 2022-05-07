d1 >> vibra(0, dur=cascara, amp=1.2, root=PTri(0, 8, 2).stutter(4))

d2 >> play("T", dur=clave23, amp=.9)

k1 >> kicker([0, 9], oct=3, ssc=.8, dur=1).every(16, "stutter", 3)

b1 >> crubass([0, 0, 2, -5, 0, -2], oct=3,
              dur=[2, 2, 1, 3]).span(linvar([0, 5.9], [8, 0]))
b1.fadein(16)

# play with params

d2.amplify = d1.amplify = var([1, 0], [48, 16])

m1.crazykitdegree = Pvz([("h ", 16), ("h(hhh) ", 16), ("hh", 16), crazykit])

d3 >> play("sss ", dur=var([.25, .125], [12, 4]), amp=PWhite(.6, 1.1)[:17])
d3.mpan(PRand(0, 5)[:17])

d1.stop()

d4 >> play("/", dur=16, amp=2).mpan(range(6))

k1 >> kicker("<aAc ><C >", dur=cascara, amp=PWhite(.8, 1.2)[:17], ssc=.8)
