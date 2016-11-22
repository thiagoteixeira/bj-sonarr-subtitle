SOURCE_PATH = $sonarr_episodefile_sourcepath
DESTINATION_PATH = $sonarr_episodefile_path

find $SOURCE_PATH '*.srt' -exec cp -vuni '{}' $DESTINATION_PATH ";"
