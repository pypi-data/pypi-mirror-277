dflt_params = {                        # CONFIG VALUE             # DEFAULT VALUE
    'SCHEMA_VER':                      '0.0.4',

    'DC_START':                        '220.0.1.1',                # '220.0.1.2'
    'DC_STEP':                         '0.0.1.0',                  # '0.0.1.0'

    'LOOPBACK':                        '221.0.0.1',                # '221.0.0.1'
    'PAL':                             '221.1.0.0',                # '221.1.0.0'
    'PAR':                             '221.2.0.0',                # '221.2.0.0'
    'GATEWAY':                         '222.0.0.1',                # '222.0.0.1'

    'DPUS':                             8,                         # 8

    'ENI_START':                        1,                         # 1
    'ENI_COUNT':                        256,                       # 256
    'ENI_STEP':                         1,                         # 1
    'ENI_L2R_STEP':                     1000,                      # 1000

    'VNET_PER_ENI':                     1,                         # 16 TODO: partialy implemented

    'ACL_NSG_COUNT':                    5,                         # 5 (per direction per ENI)
    'ACL_RULES_NSG':                    1000,                      # 1000
    'IP_PER_ACL_RULE':                  100,                       # 100
    'ACL_MAPPED_PER_NSG':               500,                       # 500, efective is 250 because denny are skiped

    'MAC_L_START':                      '00:1A:C5:00:00:01',
    'MAC_R_START':                      '00:1B:6E:00:00:01',

    'MAC_STEP_ENI':                     '00:00:00:18:00:00',       # '00:00:00:18:00:00'
    'MAC_STEP_NSG':                     '00:00:00:02:00:00',
    'MAC_STEP_ACL':                     '00:00:00:00:01:00',

    'IP_L_START':                       '1.1.0.1',                 # local, eni
    'IP_R_START':                       '1.4.0.1',                 # remote, the world

    'IP_STEP1':                         '0.0.0.1',
    'IP_STEP_ENI':                      '0.64.0.0',
    'IP_STEP_NSG':                      '0.2.0.0',
    'IP_STEP_ACL':                      '0.0.1.0',
    'IP_STEPE':                         '0.0.0.2',

    'TOTAL_OUTBOUND_ROUTES':            25600000                  # ENI_COUNT * 100K
}
