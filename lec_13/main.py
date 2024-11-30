import os
import time
from collections import Counter
from threading import Thread, Lock
from multiprocessing import Process, Manager
import random


def create_large_file(filename, num_lines, num_words_per_line):
    words = ["word", "text", "python", "code", "example", "test", "performance"]
    with open(filename, "w") as file:
        for _ in range(num_lines):
            line = " ".join(random.choice(words) for _ in range(num_words_per_line))
            file.write(line + "\n")


def count_words(filename):
    with open(filename, 'r') as file:
        word_counter = Counter()
        for line in file:
            words = line.split()
            word_counter.update(words)
    return word_counter


def count_words_thread(chunk, word_counter, lock):
    counter = Counter(chunk.split())
    with lock:
        word_counter.update(counter)


def multithreaded_word_count(filename, num_threads=4):
    file_size = os.path.getsize(filename)
    chunk_size = file_size // num_threads
    word_counter = Counter()
    lock = Lock()

    with open(filename, 'r') as file:
        threads = []
        for _ in range(num_threads):
            chunk = file.read(chunk_size)
            if not chunk:
                break
            thread = Thread(target=count_words_thread, args=(chunk, word_counter, lock))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    return word_counter


def count_words_process(chunk, return_dict):
    counter = Counter(chunk.split())
    return_dict.update(counter)


def multiprocessing_word_count(filename, num_processes=4):
    file_size = os.path.getsize(filename)
    chunk_size = file_size // num_processes
    manager = Manager()
    return_dict = manager.dict()

    with open(filename, 'r') as file:
        processes = []
        for _ in range(num_processes):
            chunk = file.read(chunk_size)
            if not chunk:
                break
            process = Process(target=count_words_process, args=(chunk, return_dict))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    final_counter = Counter()
    for key, value in return_dict.items():
        final_counter[key] += value

    return final_counter


if __name__ == "__main__":
    filename = "large_text_file.txt"
    create_large_file(filename, num_lines=5000, num_words_per_line=100)

    start_time = time.time()
    sequential_result = count_words(filename)
    sequential_time = time.time() - start_time
    print(f"Sequential execution time: {sequential_time:.4f} seconds")

    start_time = time.time()
    threaded_result = multithreaded_word_count(filename)
    threaded_time = time.time() - start_time
    print(f"Multithreading execution time: {threaded_time:.4f} seconds")

    start_time = time.time()
    multiprocessing_result = multiprocessing_word_count(filename)
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing execution time: {multiprocessing_time:.4f} seconds")

    print("\nSpeedup:")
    print(f"Multithreading speedup: {sequential_time / threaded_time:.2f}")
    print(f"Multiprocessing speedup: {sequential_time / multiprocessing_time:.2f}")