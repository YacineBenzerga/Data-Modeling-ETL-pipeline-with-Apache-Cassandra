import os
import glob
from utils import *
from queries import *
from cassandra.cluster import Cluster


def main():

    # Input/Ouput
    # get files list path
    file_path_list = []
    for root, dirs, files in os.walk('../input/event_data'):
        file_path_list = glob.glob(os.path.join(root, '*'))

    # Get csv files
    data_rows_list = get_csv_files(file_path_list)
    header_row_list = ['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length',
                       'level', 'location', 'sessionId', 'song', 'userId']
    # combine all csv files into a single file
    write_csv_from_list(data_rows_list, header_row_list,
                        'event_datafile_new.csv')

    # DB connection
    try:
        cluster = Cluster(["127.0.0.1"])
        session = cluster.connect()
    except Exception as e:
        print("Error: Couldn't connect to cluster")
        print(e)

    keyspace_config = {'class': 'SimpleStrategy', 'replication_factor': 1}
    create_keyspace(session, 'spokifydb', keyspace_config)


if __name__ == "__main__":
    main()
