import csv


def join(path1, path2, col_name, join_type):
    rows1 = []
    with open(path1, 'r') as file1:
        csvreader1 = csv.reader(file1)
        header1 = next(csvreader1)
        for row in csvreader1:
            rows1.append(row)

    # print(header1)
    # for _ in rows1:
    #     print(_)

    rows2 = []
    with open(path2, 'r') as file2:
        csvreader2 = csv.reader(file2)
        header2 = next(csvreader2)
        for row in csvreader2:
            rows2.append(row)

    # print(header2)
    # for _ in rows2:
    #     print(_)

    for head in header1:
        if col_name == header1[head]:
            if join_type.lower() == "left":
                for


print("File paths should be provided with the .csv extention")
path1 = input("Please provide a path for the first file:\n")
path2 = input("Please provide a path for the second file:\n")
col_name = input("Please provide a column name from first file:\n")
join_type = input("Please choose the join type (left, inner, right):\n")

join(path1, path2, col_name, join_type)
