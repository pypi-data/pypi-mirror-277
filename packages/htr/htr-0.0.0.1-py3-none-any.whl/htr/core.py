#
# HTR
#
# (C)opyright 2024 cKnowledge
#

import sys
import os
import logging

htr = None
htr_logger = logging.getLogger(__name__)

############################################################
class HTR(object):
    """
    """

    ############################################################
    def __init__(self, home_path = '', cfg = {}):
        """
        """

        r = self.init(home_path, cfg)
        if r['return'] > 0: self.halt(r)


    ############################################################
    def init(self, home_path, cfg):
        """
        """

        ##########################################################################################
        # Default configuration
        self.cfg = {
        }

        self.cfg.update(cfg)

        ##########################################################################################
        # Configure logger

        self._logger = htr_logger
        logging.basicConfig(level = logging.INFO)

        self._logger.debug('initialize HTR class')

        return {'return': 0}

def cli():
    print ('HTR')


############################################################
if __name__ == "__main__":
    cli()


