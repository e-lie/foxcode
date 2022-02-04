
Clock.bpm=130

d1 >> kitdatai("< ([--][---]=)(-=-[--])>< (s[ss]ss)><(       [ox]) >", dur=1/2, resob_dw=.5)


d2 >> kit808("www", dur=[4/10,3/10,3/10], amp=Pvar([[.5,1],[0]],16), reverb_dw=0)

d3 >> kicker((5,11,15,1), amp=var([0,1],[8,56])).every(8,"stutter",2)

d3 >> kicker((1,11)).every(8,"stutter",2)

b1 >> crubass([0,2,4,0,2,3],
              root=var([0,4,0,0,4,5],12),
              dur=Pvar([PSum(12,7),PSum(6,5)],12),
              oct=2,
              amp=var([0,.6,1],[36,4,52]),
              i_intensity=1,
              i_cutoff=sinvar([0,.6], 16))

b2 >> tb303([0,0,0,2,0,0],
            # dur=1/4,
            oct=3,
            vol=.8,
            i_freq=linvar([.1,.7], 16),
            i_reso=linvar([.7,1], 7),
            i_delay=linvar([.1,.5], 12),
            i_decay=linvar([.4,.6], 8),
            reverb_dw=.4,
            amp=var([1,.6,0],[120,4,32]))

g1 = Group()

Clock.bpm=160

trucmuch = bidule c'est trop bien le livecoding

drum = msm([
    ('init','xxo[-o][-o]xo[-o]'),
    ('xxo[-o][-o]xo[-o]','xxo[-o][-o]x  ', 'mod64b4r4'),
    ('*','----ooo[ooo]','mod32r4'),
    # ('*','x-o--xo-','mod64r8'),
    # ('*','x-o-','mod128r8'),
    # ('x-o--xo-', , 'mod16'),
]).pvar


def zipvar(duration_pattern_list):
    patterns = [item[0] for item in duration_pattern_list]
    durations = [item[1] for item in duration_pattern_list]
    pprint(patterns)
    pprint(durations)
    return Pvar(patterns, durations)

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
]), dur=1/2, resob_dw=0)
