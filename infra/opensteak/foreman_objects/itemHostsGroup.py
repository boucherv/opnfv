#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Authors:
# @author: David Blaisonneau <david.blaisonneau@orange.com>
# @author: Arnaud Morin <arnaud1.morin@orange.com>

from opensteak.foreman_objects.item import ForemanItem
from opensteak.foreman_objects.subItemParameter import SubItemParameter
from opensteak.foreman_objects.subItemPuppetClass import SubItemPuppetClass
from opensteak.foreman_objects.subDict import SubDict


class ItemHostsGroup(ForemanItem):
    """
    ItemHostsGroup class
    Represent the content of a foreman hostgroup as a dict
    """

    objName = 'hostgroups'
    payloadObj = 'hostgroup'

    def __init__(self, api, key,
                 objName, payloadObj,
                 *args, **kwargs):
        """ Function __init__
        Represent the content of a foreman object as a dict

        @param api: The foreman api
        @param key: The object Key
        @param *args, **kwargs: the dict representation
        @return RETURN: Itself
        """
        ForemanItem.__init__(self, api, key,
                             self.objName, self.payloadObj,
                             *args, **kwargs)
        self.update({'puppetclasses':
                     SubDict(self.api, self.objName,
                             self.payloadObj, self.key,
                             SubItemPuppetClass)})
        self.update({'parameters':
                     SubDict(self.api, self.objName,
                             self.payloadObj, self.key,
                             SubItemParameter)})