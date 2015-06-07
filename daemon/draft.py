#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  draft.py
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
import sys
from time import sleep

def main(args):
    
    sys.path.append('.')
    
    from classes.publish import PublishClient
    
    moeb='pubsub.moeyeb.us'
    chao='pubsub.chaouki.fr'
    jabb='pubsub.forlorn.fr'
    
    action_list=[
        #{'server':moeb, 'action':'create',  'node':'/home/moeyeb.us/data/1'},
        #{'server':moeb, 'action':'publish', 'node':'/home/moeyeb.us/data/1',  'data':'One!'},
        #{'server':moeb, 'action':'get',     'node':'/home/moeyeb.us/data/1',  'data':'599919EBB3819'},
        #{'server':moeb, 'action':'nodes',   'node':'/home/moeyeb.us/data/1'},
        #{'server':moeb, 'action':'nodes' },

        {'server':jabb, 'action':'create',  'node':'/home/moeyeb.us/data/1'},
        {'server':jabb, 'action':'publish', 'node':'/home/moeyeb.us/data/1',  'data':'Some Data!'},
        {'server':jabb, 'action':'get',     'node':'/home/moeyeb.us/data/1'},
        {'server':jabb, 'action':'nodes',   'node':'/home/moeyeb.us/data/1'},
        {'server':jabb, 'action':'nodes'},

        #{'server':chao, 'action':'create',  'node':'/home/moeyeb.us/data/1'},
        #{'server':chao, 'action':'publish', 'node':'/home/moeyeb.us/data/1',  'data':'One!'},
        #{'server':chao, 'action':'get',     'node':'/home/moeyeb.us/data/1',  'data':'599919EC72A85'},
        #{'server':chao, 'action':'nodes',   'node':'/home/moeyeb.us/data/1'},
        #{'server':chao, 'action':'nodes' },
    ]
    
    xmpp=PublishClient(jid='pub_sub@moeyeb.us/script_draft',password='pubsub')
    xmpp.action_list=action_list
    
    if xmpp.connect():
        xmpp.process(Threaded=False,block=True)
        
    else:
        logging.error("Could not connect to server")
    logging.info("WE DID THE main() !")
    
    while not xmpp.started:
        logging.info("xmpp.started == False")
        sleep(1)
    logging.info("xmpp.started == True")
    pprint(xmpp.result_list)
    xmpp.disconnect()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
