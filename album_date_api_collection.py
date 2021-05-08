import logging
import pandas as pd
import numpy as np
from argparse import ArgumentParser
import sys
import urllib.request, json 
import time


def main(args):
    partNr = args.split_nr
    totalParts = args.total_splits

    uniqueAlbums = pd.read_csv('unique_albums.csv')
    uniqueAlbumsSplit = np.array_split(uniqueAlbums, totalParts)[partNr]

    ablbumDates={}
    logging.basicConfig(filename=f'album_date_api_collection_part_{partNr}.log', level=logging.INFO)

    for i,albumId in enumerate(uniqueAlbumsSplit['album_id']):
        
        try:
            with urllib.request.urlopen(f"http://musicbrainz.org/ws/2/release/{albumId}?fmt=json") as url:
                data = json.loads(url.read().decode())
                ablbumDates[albumId] = data['release-events'][0]['date']
                time.sleep(1)       
        except:
            pass

        # log progress
        if(i%100==0):
            logging.info(f' Part nr.:{partNr} - {i/len(uniqueAlbumsSplit):.2f}% done')

    results = pd.DataFrame()
    results['album_id']=ablbumDates.keys()
    results['album_date']=ablbumDates.values()
    results.to_csv(f'album_dates_part_{partNr}.csv',index=False)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--split_nr',
                        help='Nr. of this split in range 0...total_number_of_splits-1', type=int,
                        required=True)
    parser.add_argument('-n', '--total_splits',
                        help='Total number of splits', type=int,
                        required=True)
    args = parser.parse_args()
    main(args)
