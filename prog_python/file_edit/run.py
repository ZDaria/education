from argparse import ArgumentParser
file_name_old = ""
file_name_new = ""
replace_from = b""
replace_to = b""


def create_file_with_replaces_value(file_name_old, file_name_new, replace_from,
                                    replace_to):
    with open(file_name_old, 'wb') as from_file:
        with open(file_name_new, 'wb') as to_file:
            file_text = from_file.read()
            for line in file_text:
                if line.find(replace_from) != -1:
                    to_file.write(line.replace(replace_from, replace_to))

    return file_name_new


if __name__ == '__main__':
    arguments = ArgumentParser()
    arguments.add_argument("-of", '--old_file',dest='old file name', help="")
    # TODO: should be added as params
    # file_name_old = ""
    # file_name_new = ""
    # replace_from = b""
    # replace_to = b""
