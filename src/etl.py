import os
import glob
from utils import *
from queries import *
from cassandra.cluster import Cluster
import pandas as pd


def main():

    # DB connection
    try:
        cluster = Cluster(["127.0.0.1"])
        session = cluster.connect()
    except Exception as e:
        print("Error: Couldn't connect to cluster")
        print(e)

    keyspace_config = {'class': 'SimpleStrategy', 'replication_factor': 1}
    create_keyspace(session, 'spokifydb', keyspace_config)

    # Input/Output
    input_files_path = os.path.abspath(
        os.path.join(os.getcwd()) + '/input/event_data')
    file_path_list = []
    for root, dirs, files in os.walk(input_files_path):
        file_path_list = glob.glob(os.path.join(root, '*'))

    # Get csv files
    data_rows_list = get_csv_files(file_path_list)
    header_row_list = ['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length',
                       'level', 'location', 'sessionId', 'song', 'userId']
    # combine all csv files into a single file
    write_csv_from_list(data_rows_list, header_row_list,
                        'event_datafile_new.csv')

    df = pd.read_csv('event_datafile_new.csv')

    # Create tables:
    exec_queries(session, create_table_queries)

    # Insert rows:
    for q in insert_table_queries:
        insert_rows_from_df(session, df, q[0], q[1])


if __name__ == "__main__":
    main()
