def count_lines(name):
    file = open(name)

    return len(file.readlines())


def count_chars(name):
    file = open(name)

    return len(file.read())


def test(name):
    file_structure = {'count_lines': count_lines(name), 'count_chars': count_chars(name)}

    return file_structure
