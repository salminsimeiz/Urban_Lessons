import time
import threading


def write_words(word_count: int, file_name: str):
    for i in range(1, word_count + 1):
        with open(file_name, "a", encoding="utf8") as file:
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = time.time()
time_res = time_end - time_start
print(f"Работа потоков {time_res:.3f}")
time_start = time.time()
thread_first = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread_second = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread_third = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread_forth = threading.Thread(target=write_words, args=(100, "example8.txt"))
thread_first.start()
thread_second.start()
thread_third.start()
thread_forth.start()
thread_first.join()
thread_second.join()
thread_third.join()
thread_forth.join()
time_end = time.time()
time_res = time_end - time_start
print(f"Работа потоков {time_res:.3f}")
