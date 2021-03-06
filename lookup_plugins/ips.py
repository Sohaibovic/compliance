
# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
import json

display = Display()

class LookupModule(LookupBase):

    def run(self, eap, variables=None, **kwargs):

        # lookups in general are expected to both take a list as input and output a list
        # this is done so they work with the looping construct 'with_'.
        ret = {}
        for ip in eap[0]:
            if 'Customer' in eap[0][ip]['tags']:
                customer = eap[0][ip]['tags']['Customer']
                if customer in ret:
                    ret[customer].append(ip)
                else:
                    rlist = []
                    rlist.append(ip)
                    ret[customer] = rlist
        lret = []
        lret.append(ret)
        return lret


