#!/usr/bin/python3
# -*- coding: utf-8 -*-
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
#    Authors:
#     Arnaud Morin <arnaud1.morin@orange.com>
#     David Blaisonneau <david.blaisonneau@orange.com>

"""
Template parser
"""

from string import Template

class OpenSteakTemplateParser:

    def __init__(self, filein, fileout, dictionary):
        """
        Parse the files with the dictionary
        """
        fin = open(filein)
        fout = open(fileout,'w')
        template = Template(fin.read())
        fout.write(template.substitute(dictionary))