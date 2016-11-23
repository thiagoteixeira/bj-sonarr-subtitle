#!/usr/bin/python

import os
import shutil
import logging

try:	
	
	logger = logging.getLogger('bj-sonarr')
	hdlr = logging.FileHandler('/tmp/bj-sonarr-subtitle.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.INFO)

	sourcePath = os.environ.get('SONARR_EPISODEFILE_SOURCEFOLDER')
	destinationPath =  os.path.dirname(os.environ.get('SONARR_EPISODEFILE_PATH'))

	logger.info('sourcePath: ' + sourcePath)
	logger.info('destinationPath: ' + destinationPath)


	for file in os.listdir(sourcePath):
    		if file.lower().endswith('.srt'):
	    		shutil.copy(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
except Exception as e:
	logger.error(e)