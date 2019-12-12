#import cassandra
import os
import glob
import csv


def write_csv_from_list(data_list):
    csv.register_dialect(
        'myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length',
                         'level', 'location', 'sessionId', 'song', 'userId'])
        for row in data_list:
            if (row[0] == ''):
                continue
            try:
                writer.writerow((row[0], row[2], row[3], row[4], row[5],
                                 row[6], row[7], row[8], row[12], row[13], row[16]))
            except Exception as e:
                print(e)


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


def main():

    for root, dirs, files in os.walk('../input/event_data'):
        file_path_list = glob.glob(os.path.join(root, '*'))

    print(file_path_list[0])


if __name__ == "__main__":
    main()
