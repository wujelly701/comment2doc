
import os
from src.single import run


def get_file_list(dir_path, file_list, walk_dir):
    """
    获取指定目录下的所有文件列表
    :param dir_path: str - 指定目录的路径
    :param file_list: list - 存储文件列表的数组
    :param walk_dir: str - 遍历的起始目录路径
    :return: list - 返回文件列表
    """
    read_file(dir_path, file_list, walk_dir)
    return file_list


dirs = {}


def read_file(dir_path, file_list, walk_dir):
    """
    递归遍历指定目录下的文件和文件夹
    :param dir_path: str - 当前遍历的路径
    :param file_list: list - 存储文件列表的数组
    :param walk_dir: str - 遍历的起始目录路径
    """

    files = os.listdir(dir_path)  # 需要用到同步读取
    print(files)
    for file_name in files:
        print(file_name)
        file_path = os.path.join(dir_path, file_name)
        file_stat = os.stat(file_path)
        if file_stat.st_mode & os.path.isdir(file_path):
            new_dir_path = os.path.join(dir_path, file_name)
            out_dir = os.path.join(os.path.dirname(__file__), 'out', new_dir_path[len('src/'):])
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            read_file(new_dir_path, file_list, walk_dir)
        else:
            file_name = file_path
            file_list.append(file_name)
            parts = file_name.split('/')

            def generate_key(root, i):
                if i == len(parts) - 1:
                    if i == 0:
                        if '0' not in root:
                            root['0'] = {'files': []}
                        root['0']['files'].append(parts[i])
                    else:
                        root['files'].append(parts[i])
                    return
                key = parts[i]
                if key not in root:
                    root[key] = {'files': []}
                generate_key(root[key], i + 1)

            generate_key(dirs, 0)


print(os.path.abspath(os.path.join(os.getcwd(), "../test")))
file_list = []
file_list = get_file_list(os.path.abspath(os.path.join(os.getcwd(), "../test")), file_list, "test")
print(file_list)
for file_name in file_list:
    run(os.path.join(os.path.dirname(__file__), '', file_name),
        os.path.dirname(os.path.join(os.path.dirname(__file__), 'out', file_name)))

heap = []


def walk(obj):
    if not isinstance(obj, dict):
        return
    for key, value in obj.items():
        if key == 'files':
            heap.extend(value)
        else:
            heap.append(key)
            walk(value)


walk(dirs)

tmp = []
tab = 0
content = ''
for item in heap:
    tmp.append(item)
    if len(tmp) % 2 == 0:
        if isinstance(item, list):
            tab = 0
            dir_path = ''
            for part in tmp:
                if isinstance(part, list):
                    for file_name in part:
                        for _ in range(tab):
                            content += '    '
                        content += '* ['
                        content += file_name
                        content += '](/'
                        content += dir_path + file_name + '.md)'
                        content += '\n'
                    tab -= 1
                else:
                    if part != '0':
                        for _ in range(tab):
                            content += '    '
                        content += '* '
                        content += part
                        content += '\n'
                        dir_path += part + '/'
                        tab += 1
            tmp = []

with open(os.path.join(os.path.dirname(__file__), 'out', 'SUMMARY.md'), 'w', encoding='utf-8') as f:
    f.write(content)
