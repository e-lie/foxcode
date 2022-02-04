

# This set is using some integration I've coded recently between FoxDot and Pylive (Ableton live OSC control)
# The goal is to use transparently live instruments and effects using a syntax consistent with FoxDot/SuperCollider SynthDefProxies



import live
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
ab = SmartSet(Clock, set)
kitcuba = Instruc(smart_track=ab.kitcuba, midi_channel=1, scale=Scale.chromatic, oct=3).out
kicker = Instruc(smart_track=ab.kicker, midi_channel=2, scale=Scale.chromatic, oct=3).out
kitdatai = Instruc(smart_track=ab.kitdatai, midi_channel=3, scale=Scale.chromatic, oct=3).out
ubass = Instruc(smart_track=ab.ubass, midi_channel=4, oct=4, scale=Scale.major).out
crubass = Instruc(smart_track=ab.crubass, midi_channel=5, oct=4, scale=Scale.major).out
strings = Instruc(smart_track=ab.strings, midi_channel=6, oct=5, scale=Scale.major).out
owstrings = Instruc(smart_track=ab.owstrings, midi_channel=7, oct=5, scale=Scale.major).out
balafon = Instruc(smart_track=ab.balafon, midi_channel=8, oct=6, scale=Scale.major).out
bells = Instruc(smart_track=ab.bells, midi_channel=9, oct=6, scale=Scale.major).out
kora = Instruc(smart_track=ab.bells, midi_channel=9, oct=6, scale=Scale.major).out

Clock.bpm = 120
Clock.midi_nudge = 0.29 # bpm 120

Clock.bpm = 130
Clock.midi_nudge = 0.22 # bpm 120

Clock.bpm = 140
Clock.midi_nudge = 0.19 # bpm 140

# TODO create a function to automatically compute and apply the nudge when changing bpm also with timevars

r = rest()
bin3 = P[1/2,1/4,1/4]
gnawa = P[4/10,3/10,3/10]
ter3 = P[1/3,1/3,1/3]

crubass_base = { "i_cutoff": 0, "i_reso": 0}
crubass_reso = { "i_cutoff": 1, "i_reso": 1}
crubass_resovar16 = { "i_cutoff": sinvar([0,1],16), "i_reso": sinvar([0,1],16)}

delay_base = { "delay_vol": 0, "delay_time": .5, "delay_feedback": .5, "delay_pan": .5}
delay_var = { "delay_vol": sinvar([0,.6], 32),
                "delay_time": .5,
                "delay_feedback": .5,
                "delay_pan": sinvar([0,1],.5)}

def delay(config=None, vol=None, time=None, feedback=None, pan=None, dry=None):
    delay_base = { "delay_vol": 0, "delay_time": .5, "delay_feedback": .5, "delay_pan": .5, "delay_dry": 1 }
    if config and 'var' in config:
        dur = int(config[3:])
        vol = sinvar([0,.6],dur)
        time = 1 / (Clock.bpm / 60) # synchro delay time with current bpm
    vol = vol if vol is not None else delay_base["delay_vol"]
    time = time if time is not None else delay_base["delay_time"]
    feedback = feedback if feedback is not None else delay_base["delay_feedback"]
    pan = pan if pan is not None else delay_base["delay_pan"]
    dry = dry if dry is not None else delay_base["delay_dry"]
    return { "delay_vol": vol, "delay_time": time, "delay_feedback": feedback, "delay_pan": pan, "delay_dry": dry}



def mvr(dur, pattern=1):
    pattern = P[pattern]
    if len(pattern) > 1:
        return P[rest(dur)] | pattern[:-1] | pattern[-1] - dur
    else:
        return P[rest(dur)] | P[pattern-dur]

print(mvr(1/10,[1/2,1/2]))

k2 >> play('t-ro-', dur=P[1,1]/2 | mvr(3/10,[1,1])/2)
k3 >> kicker(8,dur=1)














#TODO add a new simple bass but with good params
#TODO code instru factory
#TODO create a multibass ableton instrument (combining 3 bass sounds, techno, normal, sub)
#TODO look at atom hotkeys and code snippets
