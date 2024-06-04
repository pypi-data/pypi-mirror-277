#!/usr/bin/python3
"""SAI generator for Acl Groups"""

import os
import sys

from dpugen.confbase import ConfBase
from dpugen.confutils import common_main


class AclGroups(ConfBase):

    def __init__(self, params={}):
        super().__init__(params)
        self.num_yields = 0

    def items(self):
        print('  Generating %s ...' % os.path.basename(__file__), file=sys.stderr)
        p = self.params

        for eni_index, eni in enumerate(range(p.ENI_START, p.ENI_START + p.ENI_COUNT * p.ENI_STEP, p.ENI_STEP)):  # Per ENI
            print(f'    acl_group:eni:{eni}', file=sys.stderr)
            for stage_in_index in range(p.ACL_NSG_COUNT):  # Per inbound stage
                table_id = eni * 1000 + stage_in_index

                self.num_yields += 1
                yield {
                    'name': f'in_acl_group_#{table_id}',
                    'op': 'create',
                    'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                    'attributes': [
                        'SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY', 'SAI_IP_ADDR_FAMILY_IPV4',
                    ]
                }

            for stage_out_index in range(p.ACL_NSG_COUNT):  # Per outbound stage
                table_id = eni * 1000 + 500 + stage_out_index

                self.num_yields += 1
                yield {
                    'name': f'out_acl_group_#{table_id}',
                    'op': 'create',
                    'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                    'attributes': [
                        'SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY', 'SAI_IP_ADDR_FAMILY_IPV4',
                    ]
                }


if __name__ == '__main__':
    conf = AclGroups()
    common_main(conf)
