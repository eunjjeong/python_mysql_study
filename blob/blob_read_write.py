def read_file_blob(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


def write_file_blob(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
