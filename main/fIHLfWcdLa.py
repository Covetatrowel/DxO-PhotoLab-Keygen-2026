import os
import json
import shutil
from datetime import datetime

class FileUtility:
    def __init__(self, directory):
        self.directory = directory
        self.file_list = []
    def scan_files(self):
        self.file_list = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
    def get_file_info(self):
        file_info = {}
        for file in self.file_list:
            path = os.path.join(self.directory, file)
            file_info[file] = {
                'size': os.path.getsize(path),
                'modified': datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
            }
        return file_info
    def backup_files(self, backup_directory):
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
        for file in self.file_list:
            src = os.path.join(self.directory, file)
            dst = os.path.join(backup_directory, file)
            shutil.copy2(src, dst)
    def save_info_to_json(self, output_file):
        info = self.get_file_info()
        with open(output_file, 'w') as f:
            json.dump(info, f, indent=4)

if __name__ == '__main__':
    util = FileUtility('./')
    util.scan_files()
    util.backup_files('./backup')
    util.save_info_to_json('file_info.json')
