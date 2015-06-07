#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  publish.py
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

from pprint import pprint

import logging
from classes.base import PubsubClient
import random

class PublishClient(PubsubClient):
    """  """
    
    def __init__(self, jid='pub_sub@moeyeb.us/script_publish', password='pubsub'):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        super(PublishClient, self).__init__(jid=jid, password=password)
        
        logging.basicConfig(level=logging.INFO)
        # Needed to add a random seed if a resource is defined (to prevent auth failures)
        if '/' in jid:
            r=random.randint(0,999)
            jid=jid+str(r)
        
        """ self.action_list = [ [where, what, node, data], [...] ] """
        self.action_list=[]
        self.result_list=[]
        
        logging.info("publish.add_event")
        self.add_event_handler('session_start', self.start)
    
    def do_it(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        #try:
        logging.warn("===================================================")
        logging.warn(
            "self.do_it() args : server=%r node=%r action=%r data=%r"%
            (self.pubsub_server, self.node, self.action, self.data) )
        getattr(self, self.action)()
        #except:
            #logging.error('Could not execute: %s' % self.action)
    
    def start(self, event):
        logging.info("publish.start")
        self.get_roster()
        self.send_presence()
        for do in self.action_list:
            try:
                self.pubsub_server     = None
                self.action            = None
                self.node              = None
                self.data              = None
                try:
                    self.pubsub_server = do['server']
                except KeyError:
                    print('KeyError')
                    pass
                try:
                    self.action        = do['action']
                except KeyError:
                    pass
                try:
                    self.node          = do['node']
                except KeyError:
                    pass
                try:
                    self.data          = do['data']
                except KeyError:
                    pass
            except:
                logging.error("Unexpected exception. Malformed self.action_list variable? ")
            self.do_it()
            self.result_list.append(self.result)
        self.started=True
        logging.info("WE DID the self.start() !")
    
    def publish(self):
        payload = ET.fromstring("<test xmlns='test'>%s</test>" % self.data)
        try:
            result = self['xep_0060'].publish(self.pubsub_server, self.node, payload=payload)
            self.result=result
            id = result['pubsub']['publish']['item']['id']
            print('Published at item id: %s' % id)
        except:
            logging.error('Could not publish to: %s' % self.node)
            self.result=False
