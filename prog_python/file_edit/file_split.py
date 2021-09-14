def create_new_file(new_file_name, start_pos, end_pos, lines):
    with open(new_file_name, 'w') as new_file:
        for line in lines[start_pos: end_pos]:
            new_file.write(line)


def split_file_by_records_limit(file_split, limit):
    with open(file_split, 'r') as log_file:
        lines = log_file.readlines()

    file_size = len(lines)
    counter = 1
    start_pos = 0
    end_pos = limit
    while file_size - end_pos >= 0:
        create_new_file(file_split + '_' + str(counter), start_pos, end_pos, lines)
        counter += 1
        start_pos = end_pos

        if file_size - limit > 0:
            file_size -= limit
            end_pos += limit
        else:
            end_pos = file_size


file_split = ""
split_file_by_records_limit(file_split, 50)
