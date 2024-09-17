import os
import time

for root, dirs, files in os.walk(".."):
    for file in files:
        file_path = os.path.join(file)
        file_time = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер:{file_size}  байт,'
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
