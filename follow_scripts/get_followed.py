import csv


def get_followed(path_to_file, name):
    file = open(path_to_file)
    reader = csv.reader(file)
    data = list(reader)

    print(len(data), data)

    for line in data:
        if name in line:
            print("found " + name)
            print(data.index(line))
            return True

    print(name + " not found")

    file.close()


if __name__ == '__main__':
    get_followed('../csv_files/followed.csv', 'crispiresyoga')
