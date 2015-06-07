#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  yaml.py
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
import yaml, sys

class YamlConf(object):
    """  """
    
    def __init__ (self, confdir='../conf/', tag='dev'):
        """ Class initialiser """
        
        config = yaml.load(open(confdir+'example.yaml','rb').read())
        try:
            self.rawconfig = config[tag]
        except KeyError:
            logging.error("No configuration was found for tag [%s] " % tag )
            exit(1)
        self.setAccounts()
        if not self.validateAccounts():
            logging.error("Could not validate the account section. Dumping it.")
            pprint(self.accounts)
            exit(1)
    
    def validateAccounts(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        return True
    
    def setAccounts(self):
        """ Parses the raw config − Generates YamlConf.accounts array
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        logging.info("yamltest.YamlConf.parserawconf ! ")
        
        # BEGIN Setting self.accounts
        self.accounts=[]
        for account in self.rawconfig['accounts']:
            # BY simply copying the current account
            acc=account
            # BY appending servers into each account
            try:
                for server in self.rawconfig['servers']:
                    try:
                        acc['servers'].append(server)
                    except KeyError:
                        acc['servers']=[server]
            except KeyError as e:
                pass
            # BY overriding the nodeprefix key, if present. 
            try:
                acc['nodeprefix']=self.rawconfig['nodeprefix']
            except KeyError as e:
                pass
            # BY Making sure servers are unique
            acc['servers']=list(set(acc['servers']))
            # BY Appending resulting accounts 
            self.accounts.append(acc)
        # END
try:
    yamlconf=YamlConf(confdir='../conf/', tag='prod')
    print("---yamlconf.accounts---")
    pprint(yamlconf.accounts)
except KeyError:
    logging.error("KeyError exception while parsing configuration file")
