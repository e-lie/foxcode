
Clock.bpm=130

d1 >> kitdatai("< ([--]=)->< s><(      [ox]) >", dur=1/2, oct=3, resob_dw=sinvar([.1,.5],16))

b1 >> crubass([0,2,4,0,2,3], root=var([0,4,0,0,5,4],16), oct=(2,3), dur=PSum(12,7))

d2 >> kicker((12,5), amp=var([1,0], [56,8])).every(8, "stutter", 2)

d3 >> kit808(Pvar(["www", "w ", " "], 16), dur=[4/10,3/10,3/10], amp=[.5,1])

b2 >>  tb303_2([0,0,4,0,0,2], dur=1/4, pan=sinvar([-1,1], 16),
                tb303_i_freq=linvar([.1,.7],16),
                tb303_i_reso=linvar([.7,.1],7),
                tb303_i_decay=linvar([.3,.6],12),
                tb303_i_delay=linvar([.1,.5],7),
                reverb_dw=linvar([.1,.5],12),
                amp=var([0,1], [8,56]))


g1 = Group(b2, d2, d3)

d2.stop()

Clock.bpm=160

d4 >> kitdatai(zipvar([
('xxo[-o][-o]xo[-o]',15),
('[oo]x',1),
('xxo[-o][-o]xo[-o]',14),
('[xx][ox]',2),
('xxo[-o][-o]xo[-o]',14),
('<ooxo>< = =>',2),
('xxo[-o][-o]xo[-o]',12),
(' ',4),
]), dur=1/2,
amp=var([1,0], [56,8]),
resob_dw=0)

That's all folks ! First recording ;)
