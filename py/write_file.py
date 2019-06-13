import os


def write_file(file_path, file_name, write_str, encoding='utf8'):
    """把字符串写入文件，如果目录不存在就创建目录"""
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path_name = os.path.join(file_path,file_name)
    with open(file_path_name, 'w', encoding=encoding) as f:
        return f.write(write_str)


if __name__ == '__main__':
    write_file('/Users/qudian/tmp/bb/aa', 'aabb.txt', 'haha')
    write_file('/Users/qudian/tmp/cc/aa/', 'aabb.txt', 'haha')
