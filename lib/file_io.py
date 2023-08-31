def write_file(file_name, file_content):
    fname = str(file_name) + ".txt"
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(file_content)
    return

def append_file(file_name, append_content):
    fname = str(file_name) + ".txt"
    with open(fname, 'a', encoding='utf-8') as f:
        f.write(append_content)
    return

def read_file(file_name):
    fname = str(file_name) + ".txt"
    with open(fname, 'r', encoding='utf-8') as f:
        return f.read()