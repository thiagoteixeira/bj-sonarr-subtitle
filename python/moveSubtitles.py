import os
import shutil

sourcePath = os.environ['NZBPP_DIRECTORY']
destinationPath = os.environ['NZBPP_FINALDIR']


if  os.environ['NZBPP_TOTALSTATUS'] == "SUCCESS" and os.environ['NZBPP_UNPACKSTATUS'] == 2:
	for file in files:
		    if file.endswith('.srt'):
		        shutil.copy(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
