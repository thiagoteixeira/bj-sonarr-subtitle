#!/usr/bin/python

import os
import shutil
import logging

logger = logging.getLogger('bj-sonarr')
hdlr = logging.FileHandler('/tmp/bj-sonarr-subtitle.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

sourcePath = os.getenv('Sonarr_EpisodeFile_Path', 'default')
destinationPath = os.getenv('Sonarr_EpisodeFile_Path', 'default')

logger.info('sourcePath: ' + sourcePath)
logger.info('destinationPath: ' + destinationPath)
try:
	for file in os.listdir(sourcePath):
    		if file.endswith('.srt'):
	    		shutil.copy(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
except Exception as e:
	logger.error(e)