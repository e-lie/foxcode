


# interpolation de rythmes

bin3 = P[1/2,1/4,1/4]
gnawa = P[4/10,3/10,3/10]
ter3 = P[1/3,1/3,1/3]
tt >> kitcuba("Aaa", dur=Pvar(interpolate(bin3,ter3,step=7,go_back=True),2)*2)

# fonction delay ou autre filtre avec unpacking


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

b1 >> crubass(base1, dur=PSum(3,2), oct=3, scale=Scale.minor, pan=0, amp=var([1,0],[6,2,7,1]), **delay(vol=1, pan=.5,dry=0))
tt >> kitcuba("Aaa", dur=gnawa, **delay(vol=.5, pan=sinvar([0,1],2),dry=.5))
