"""
Created by anthony on 12.11.17
global variables shared across the app to prevent cyclic references
"""
import logging

# TODO move config into configFile  in config.log_config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


log = logging.getLogger(__name__)

log.info('> Starting globals')

updater = None
queue = None
automata = None

log.info('Globals have started')
