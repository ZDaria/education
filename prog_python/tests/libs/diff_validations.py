from prog_python.tests.helpers.diff_file_load import \
    get_csv_file_rows

diff_file = get_csv_file_rows()


def compare_old_new_tenor(old_tenor, new_tenor):
    errors_list = []
    for line in diff_file:
        if line.old_value.find(old_tenor) != -1 and \
                line.diff_action.find("CHANGED") != -1:
            if line.new_value.find(new_tenor) == -1:
                errors_list.append([line.instrument, line.old_value,
                                   line.new_value])
    return errors_list
