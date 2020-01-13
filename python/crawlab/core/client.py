import os
from zipfile import ZipFile, ZIP_DEFLATED

from prettytable import PrettyTable

from crawlab.core import CRAWLAB_TMP
from crawlab.core.config import config
from crawlab.core.request import Request


def zip_dir(start_dir, target_path):
    start_dir = start_dir  # 要压缩的文件夹路径
    file_new = target_path  # 压缩后文件夹的名字

    z = ZipFile(file_new, 'w', ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            print(f_path + filename)
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_new


def get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        filepath = os.path.join(input_path, file)
        if os.path.isdir(filepath):
            get_zip_file(filepath, result)
        else:
            result.append(filepath)


def zip_file_path(input_path, target_path):
    f = ZipFile(target_path, 'w', ZIP_DEFLATED)
    file_list = []
    get_zip_file(input_path, file_list)
    for file in file_list:
        f.write(file)
    f.close()
    return target_path


class Client(object):
    def __init__(self):
        pass

    @staticmethod
    def list(columns, items):
        tb = PrettyTable()
        tb.field_names = columns
        for item in items:
            row = []
            for col in columns:
                row.append(item.get(col))
            tb.add_row(row)
        print(tb)
        print(f'total: {len(items)}')

    @staticmethod
    def update_token():
        data = Request.post('/login', data={
            'username': config.data.username,
            'password': config.data.password,
        })
        if data.get('error'):
            print('error: ' + data.get('error'))
            print('error when logging-in')
            return
        config.data.token = data.get('data')
        config.save()
        print('logged-in successfully')

    @staticmethod
    def list_nodes():
        data = Request.get('/nodes')
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data') or []
        columns = ['_id', 'name', 'status', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def list_spiders():
        data = Request.get('/spiders', {'page_size': 99999999})
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = (data.get('data').get('list') or []) if data.get('data') is not None else []
        columns = ['_id', 'name', 'display_name', 'type', 'col', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def list_schedules():
        data = Request.get('/schedules', {'page_size': 99999999})
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data') or []
        columns = ['_id', 'name', 'spider_name', 'run_type', 'cron', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def list_tasks(number=10):
        data = Request.get('/tasks', {'page_size': number})
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data') or []
        columns = ['_id', 'status', 'node_name', 'spider_name', 'error', 'result_count', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def upload_customized_spider(directory=None, name=None, col=None, display_name=None, command=None, id=None):
        # check if directory exists
        if not os.path.exists(directory):
            print(f'error: {directory} does not exist')
            return

        # compress the directory to the zipfile
        target_path = os.path.join(CRAWLAB_TMP, name or os.path.basename(directory)) + '.zip'
        zip_dir(directory, target_path)

        # upload zip file to server
        if id is None:
            res = Request.upload('/spiders', target_path, data={
                'name': name,
                'display_name': display_name,
                'col': col,
                'command': command,
            })
            if res.get('error'):
                print('error: ' + res.get('error'))
                return
        else:
            res = Request.upload(f'/spiders/{id}/upload', target_path)
            if res.get('error'):
                print('error: ' + res.get('error'))
                return
        print('uploaded successfully')

    @staticmethod
    def upload_configurable_spider(directory=None, name=None, col=None, display_name=None, command=None, id=None):
        pass


client = Client()