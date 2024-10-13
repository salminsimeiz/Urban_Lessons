from datetime import datetime
import multiprocessing
from threading import Thread


def read_info(file_name):
    all_data = []
    with open(file_name, "r", encoding="utf8") as file:
        while True:
            line = file.readline()
            if line.endswith("\n"):
                all_data.append(line.rstrip())
                continue
            else:
                print(f"Завершена запись данных из файла {file_name}")
                break
        return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.now()
result = list(map(read_info, filenames))
end = datetime.now()
execution_time = end - start
print(execution_time)

# execution_time = 0:00:16.167920

"""if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        result = list(pool.map(read_info, filenames))
    end = datetime.now()
    execution_time = end - start
    print(execution_time)"""

# execution_time = 0:00:19.291658

"""filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.now()
result = [read_info(name) for name in filenames]
end = datetime.now()
execution_time = end - start
print(execution_time)"""

# execution_time = 0:00:13.441628


"""def main():
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    threads = [Thread(target=read_info, args=(filename,)) for filename in filenames]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = datetime.now()
    main()
    end = datetime.now()
    execution_time = end - start
    print(execution_time)"""

# execution_time = 0:00:20.795973
