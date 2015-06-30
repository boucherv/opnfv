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

from opensteak.foreman_objects.objects import ForemanObjects
from opensteak.foreman_objects.item import ForemanItem


class OperatingSystems(ForemanObjects):
    """
    OperatingSystems class
    """
    objName = 'operatingsystems'
    payloadObj = 'operatingsystem'
    index = 'title'
    searchLimit = 20

    def __getitem__(self, key):
        """ Function __getitem__

        @param key: The operating system id/name
        @return RETURN: The item
        """
        ret = self.api.list(self.objName,
                            filter='title = "{}"'.format(key))
        if len(ret):
            return ForemanItem(self.api, key,
                               self.objName, self.payloadObj,
                               ret[0])
        else:
            return None