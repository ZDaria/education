import csv
from prog_python.experiments.tests.dump_diff import DumpDiff


def get_csv_file_rows():
    dump_diff_file = []
    with open('../test_data/example.csv', newline='') as csv_file:
        row_reader = csv.reader(csv_file, delimiter=',')
        for row in row_reader:
            dump_diff_file.append(DumpDiff(*row))
    return dump_diff_file
