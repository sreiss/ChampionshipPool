import csv


def load_csv(datafile):
    data_matrix = []
    data = open(datafile, 'r')
    reader = csv.reader(data)
    for row in reader:
        if len(row) > 0:
            data_matrix.append(row)
    return data_matrix


def extract_columns(columns, matrix):
    return [[each_list[i] for i in columns] for each_list in matrix]


def init_matrix(datafile):
    matrix = load_csv(datafile)
    clubs = extract_columns([0], matrix)
    dict1 = {}
    i = 0
    for row in matrix:
        if i != 0:
            dict2 = {}
            j = 0
            for value in row:
                if j != 0:
                    dict2[clubs[j][0]] = float(value)
                j += 1
            dict1[clubs[i][0]] = dict2
        i += 1
    return dict1
