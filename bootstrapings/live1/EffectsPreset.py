
track_default = {
    "vol": 1,
    "pan": 0,
}

reverb_default = {
    "reverb_dw": 0,
    "reverb_hifreq": .89,
    "reverb_lowfreq": .11,
    "reverb_decay": .41,
}

resob_default = {
    "resob_dw": 0,
    "resob_color": .85,
    "resob_gain": .66,
    "resob_width": 1,
}

eq_default = {
    "eq_gainlo": .85,
    "eq_gainmid": .85,
    "eq_gainhi": .85,
    "eq_freqlo": .3,
    "eq_freqhi": .57,
}

delay_default = {
    "delay_vol": 0,
    "delay_time": 0,
    "delay_feedback": .5,
    "delay_pan": .9,
    "delay_dry": 1,
}

hamp_default = {
    "hamp_dw": 0,
    "hamp_gain": .47,
    "hamp_low": .68,
    "hamp_mid": .68,
    "hamp_high": .6,
    "hamp_cabinet": .23,
    "hamp_vol": .68,
    "hamp_rack_vol": .83,
}

phaser_default = {
    "phaser_dw": 0,
    "phaser_drive": 0,
    "phaser_width": 1,
    "phaser_reso": 1,
    "phaser_phase": .9,
    "phaser_lfo1": .3,
    "phaser_lfo2": .3,
    "phaser_lfo3": .5,
}

config_default = {} | track_default | reverb_default | eq_default | resob_default | delay_default | hamp_default | phaser_default

###########################################################
###########################################################
###########################################################




reverbp = {
    "reverb_dw": 0,
    "reverb_hifreq": 0,
    "reverb_lowfreq": 0,
    "reverb_decay": 0,
}

resobp = {
    "resob_dw": 0,
    "resob_color": 0,
    "resob_gain": 0,
    "resob_width": 0,
}

phaserp = {
    "phaser_lfo1": 0,
    "phaser_lfo2": 0,
    "phaser_lfo3": 0,
    "phaser_phase": 0,
    "phaser_reso": 0,
    "phaser_drive": 0,
    "phaser_width": 0,
    "phaser_dw": 0,
}

hampp = {
    "hamp_gain": 0,
    "hamp_low": 0,
    "hamp_mid": 0,
    "hamp_high": 0,
    "hamp_cabinet": 0,
    "hamp_vol": 0,
    "hamp_dw": 0,
    "hamp_rack_vol": 0,
}

################################################################
################################################################
##################    Instruments params     ###################
################################################################
################################################################


crubassp = {
    "crubass_i_wt_pos":.2,
    "crubass_i_glide":3,
    "crubass_i_intensity":.8,
    "crubass_i_cutoff":.1,
    "crubass_i_crush":.2,
    "crubass_i_delay":.4,
    "crubass_i_reso":.3,
    "crubass_i_filter":.3,
}

tb303p = {
    "tb303_i_decay":.2,
    "tb303_i_freq":3,
    "tb303_i_reso":.8,
    "tb303_i_drive":.1,
    "tb303_i_delay":.2,
    "tb303_i_dfreq":.4,
}

ubassp = {
    "ubass_i_wt_pos":.2,
    "ubass_i_drive":3,
    "ubass_i_intensity":.8,
    "ubass_i_chorus":.1,
    "ubass_i_cutoff":.2,
    "ubass_i_flt_dec":.4,
    "ubass_i_reso":.3,
    "ubass_i_dec_time":.3,
}

bellsp = {
    "bells_i_bright":.2,
    "bells_i_detune":.2,
    "bells_i_material":.2,
    "bells_i_mod_amount":.2,
    "bells_i_attack":.2,
    "bells_i_decay":.2,
    "bells_i_mod_freq":.2,
    # "bells_i_volume":.2, # keep it 0dB
}

pianop = {
    "piano_i_bright":.2,
    "piano_i_hardness":.2,
    "piano_i_glue":.2,
    "piano_i_reverb":.2,
    "piano_i_attack":.2,
    "piano_i_release":.2,
    "piano_i_tone":.2,
    # "piano_i_volume":.2,
}

danceorgp = {
    "danceorg_i_bright":.2,
    "danceorg_i_spike":.2,
    "danceorg_i_tone":.2,
    "danceorg_i_space":.2,
    "danceorg_i_attack":.2,
    "danceorg_i_release":.2,
    "danceorg_i_tremolo":.2,
    # "danceorg_i_volume":.2,
}

danceorg_amb1 = {
    "danceorg_i_bright":0,
    "danceorg_i_spike":0,
    "danceorg_i_tone":.9,
    "danceorg_i_space":.7,
    "danceorg_i_attack":.7,
    "danceorg_i_release":.8,
    "danceorg_i_tremolo":0,
    # "danceorg_i_volume":.2,
}
