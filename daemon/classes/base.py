#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  base.py
#  
#  Copyright 2015 Samir Chaouki <moebius.eye@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

#
# This is from https://github.com/fritzy/SleekXMPP/blob/develop/examples/pubsub_client.py
#

import sys
import logging

import sleekxmpp
from sleekxmpp.xmlstream import ET, tostring


# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')
else:
    raw_input = input

class PubsubClient(sleekxmpp.ClientXMPP):
    
    def __init__(self, jid='pub_sub@localhost/script_publish', password='pubsub'):
        super(PubsubClient, self).__init__(jid, password)
        
        self.register_plugin('xep_0030')
        self.register_plugin('xep_0059')
        self.register_plugin('xep_0060')
        
        self.use_ipv6 = False
        
        self.started=False
        self.pubsub_server=None
        self.node=None
        self.action=None
        self.data=None
        self.result=None

    def nodes(self):
        try:
            result = self['xep_0060'].get_nodes(self.pubsub_server, self.node)
            self.result=result
            for item in result['disco_items']['items']:
                print('  - %s' % str(item))
        except:
            logging.error('Could not retrieve node list.')
            self.restult=False

    def create(self):
        try:
            self['xep_0060'].create_node(self.pubsub_server, self.node)
            self.result=True
        except:
            logging.error('Could not create node: %s' % self.node)
            self.result=False

    def delete(self):
        try:
            self['xep_0060'].delete_node(self.pubsub_server, self.node)
            print('Deleted node: %s' % self.node)
            self.result=True
        except:
            logging.error('Could not delete node: %s' % self.node)
            self.result=False

    def get(self):
        try:
            result = self['xep_0060'].get_item(self.pubsub_server, self.node, self.data)
            self.result=result
            for item in result['pubsub']['items']['substanzas']:
                print('Retrieved item %s: %s' % (item['id'], tostring(item['payload'])))
        except:
            logging.error('Could not retrieve item %s from node %s' % (self.data, self.node))
            self.result=False

    def retract(self):
        try:
            result = self['xep_0060'].retract(self.pubsub_server, self.node, self.data)
            self.result=restult
            print('Retracted item %s from node %s' % (self.data, self.node))
        except:
            logging.error('Could not retract item %s from node %s' % (self.data, self.node))
            self.result=False

    def purge(self):
        try:
            result = self['xep_0060'].purge(self.pubsub_server, self.node)
            self.result=result
            print('Purged all items from node %s' % self.node)
        except:
            logging.error('Could not purge items from node %s' % self.node)
            self.result=False

