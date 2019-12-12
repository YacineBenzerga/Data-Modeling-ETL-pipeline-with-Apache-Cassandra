from cassandra.cluster import Cluster
import os
import glob
from utils import get_csv_files, write_csv_from_list


def init_db_conn():
    try:
        cluster = Cluster(["127.0.0.1"])
        session = cluster.connect()
    except Exception as e:
        print("Error: Couldn't connect to cluster")
        print(e)

    return session, cluster


def create_keyspace(session, keyspace_name, keyspace_config):
    try:
        session.execute("""CREATE KEYSPACE IF NOT EXISTS {} 
            WITH REPLICATION = {}
        """.format(keyspace_name, keyspace_config))
    except Exception as e:
        print("Error: Couldn't create keyspace")
        print(e)


def main():

    # Input/Ouput
    # get files list path
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
    session, cluster = init_db_conn()


if __name__ == "__main__":
    main()
