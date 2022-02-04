
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



def randomize_params(param_dict, seed=0):
    params_values = PWhite(seed=seed)[:len(param_dict.keys())]
    for i, key in enumerate(param_dict.keys()):
        param_dict[key] = params_values[i]
    return param_dict
rndp = randomize_params
