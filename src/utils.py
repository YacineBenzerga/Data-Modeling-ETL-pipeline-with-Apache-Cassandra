import os
import glob
import csv
import pandas as pd


def get_csv_files(filepath):
    full_data_rows_list = []

    for f in filepath:
        try:
            with open(f, 'r', encoding='utf8', newline='') as csvfile:
                # creating a csv reader object
                csvreader = csv.reader(csvfile)
                next(csvreader)

                for line in csvreader:
                    full_data_rows_list.append(line)
        except Exception as e:
            print(e)

    return full_data_rows_list


def write_csv_from_list(data_list, header_row, filename):
    csv.register_dialect(
        'myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(header_row)
        print("Writing rows to csv")
        for i, row in enumerate(data_list):
            if (row[0] == ''):
                continue
            try:
                writer.writerow((row[0], row[2], row[3], row[4], row[5],
                                 row[6], row[7], row[8], row[12], row[13], row[16]))

            except Exception as e:
                print(e)
        print("Done writing to csv")


def create_keyspace(session, keyspace_name, keyspace_config):
    try:
        session.execute("""CREATE KEYSPACE IF NOT EXISTS {} 
            WITH REPLICATION = {}
        """.format(keyspace_name, keyspace_config))
        session.set_keyspace(keyspace_name)
    except Exception as e:
        print("Error: Couldn't create keyspace")
        print(e)


def insert_rows_from_df(session, df, query, cols):
    for i, row in df.iterrows():
        try:
            session.execute(query, tuple([row[x] for x in cols]))
        except Exception as e:
            print(e)
    print("Insert {} successful".format(query))


def exec_queries(session, queries):
    for q in queries:
        try:
            session.execute(q)
            print("Successfuly executed query: \n{}".format(q))
        except Exception as e:
            print("Error: Couldn't execute query:\n{}".format(q))
            print(e)
