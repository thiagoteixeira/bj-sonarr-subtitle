LOG_FILE = "/tmp/bj-sonarr-subtitle.log"

SOURCE_PATH = $sonarr_episodefile_sourcepath
DESTINATION_PATH = $sonarr_episodefile_path

echo "SOURCE_PATH: $SOURCE_PATH " >> $LOG_FILE
echo "DESTINATION_PATH: $DESTINATION_PATH " >> $LOG_FILE

find $SOURCE_PATH '*.srt' -exec cp -vuni '{}' $DESTINATION_PATH ";"
