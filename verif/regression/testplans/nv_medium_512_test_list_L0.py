############################################# PDP ###################################
add_test(name='pdp_3x3x33_2x2_ave_int8_0',
         tags=['L0', 'pdp'],
         unwritten = True,
         args=[FIXED_SEED_ARG, DISABLE_COMPARE_ALL_UNITS_SB_ARG, '-uwm cmod_only'],
         config=['nvdla_utb'],
         desc='''copied from pdp_full_feature_14''')

############################################# SDP ###################################
add_test(name='sdp_13x4x29_ew_lut_int8',    #sdp_cmod_full_feature_7
         tags=['L0', 'sdp'],
         unwritten = True,
         args=[FIXED_SEED_ARG, DISABLE_COMPARE_ALL_UNITS_SB_ARG, '-uwm cmod_only'],
         config=['nvdla_utb'],
         desc='''copied from sdp_cmod_full_feature_7, input: 13x4x29, BS/BN disabled, EW enabled w/ MUL(per-channel),LUT enabled, both input/output are INT8''')

############################################# CDP ###################################
add_test(name='cdp_8x8x64_lrn9_int8_0',
         tags=['L0', 'cdp'],
         unwritten = True,
         args=[FIXED_SEED_ARG, DISABLE_COMPARE_ALL_UNITS_SB_ARG],
         config=['nvdla_utb'],
         desc='''copied from cdp_full_feature_0, read from CV, write to CV''')

############################################# CC ####################################
#DC mode
add_test(name='dc_8x16x128_3x3x128x32_int8',    #cc_full_feature_0
         tags=['L0', 'cc'],
         unwritten = True,
         args=[FIXED_SEED_ARG, DISABLE_COMPARE_ALL_UNITS_SB_ARG, '-uwm cmod_only'],
         config=['nvdla_utb'],
         desc='''copied from cc_small_full_feature_0, kernel stride 1x1, unpacked, pad L/T/B, no clip truncate, partial weight''')

#Image-in mode
add_test(name='img_51x96x4_1x10x4x32_R8G8B8A8_int8_0', #pixel format 0xf
         tags=['L0','cc', 'img'],
         unwritten = True,
         args=[FIXED_SEED_ARG, DISABLE_COMPARE_ALL_UNITS_SB_ARG, '-uwm cmod_only'],
         config=['nvdla_utb'],
         desc='''copied from cc_small_full_feature_17, kernel stride 2x2, unpacked, no padding, clip truncate 3, full weight, input cvt enable, cvt_scale 1, cvt_offset 0, cvt_truncate 0''')

