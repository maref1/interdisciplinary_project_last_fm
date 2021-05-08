# interdisciplinary_project_last_fm

**Steps to run the code:**
1. Download Last.fm dataset from http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-1K.tar.gz and unzip the files to "lastfm-dataset-1K"
2. Downnload tag sql file from Million song dataset's website from http://millionsongdataset.com/sites/default/files/lastfm/lastfm_tags.db and place the file in the root directory
3. Run the data_analysis_and_preprocessing.ipynb which takes the downloaded files and api collected data in the repository and produces processed csv files in "preprocessed_data" folder
4. Now you can run the following notebooks in any order:
    * general_network_metrics.ipynb (constructs graphs a calculates some network metrics)
    * preferential_attachment_analysis.ipynb (analysis of the preferential attachment)
    * forgetting_analysis.ipynb (analysis of the forgetting)
    * create_sql_lite_db.ipynb (creates a sqlite .db file for the streamanalysis code which is not part of the repo)

**Other code files:**
* data_collection_1.ipynb - code which queries Last.fm api and returns album ids for songs, you can run multiple copies of the notebook in parallel, it is needed to set SPLIT_NR and TOTAL_SPLIT_NR in each copy accordingly (you need to have your apikey in apikey.txt file - at least TOTAL_SPLIT_NR apikeys)
* album_date_api_collection.py - uses "unique_albums.csv" and queries the Musicbrainz API to get the release dates, can be run in parallel, takes 2 arguments similarly as data_collection_1.ipynb which identify the split and the total number of splits. It is needed to run the code on multiple machines as many queries from the same ip address will cause the API to not respond.
