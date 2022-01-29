
dynvars = {}

# See theory of rhythm by Malcolm Braff
rhythms = {
"half" : P[1/2],
"swing100" : P[4/10,6/10],
"swing" : P[3/10,7/10],
"triplet" : P[1/3],
"binlet" : P[1/2,1/4,1/4],
"cubalet" : P[4/10,3/10,3/10],
"binlet2" : P[1/4,1/2,1/4],
"gnawa" : P[3/10,4/10,3/10],
"quarter" : P[1/4],
"brazlet" : P[3/10,1/5,1/5,3/10],
"brazlet100" : P[1/3,1/6,1/6,1/3],
"quintuplet" : P[1/5],
"brafflet" : P[3/12,2/12,2/12,2/12,3/12,2/12],
"clave" : P[3/15,3/15,4/15,2/15,3/15],
"clave23" : P[3/16,3/16,4/16,2/16,4/16],
"cascara" : P[2/16,2/16,1/16,2/16,1/16,2/16,1/16,2/16,2/16,1/16],
}

dynvars |= rhythms

for dynvar,value in dynvars.items():
    globals()[dynvar] = value
