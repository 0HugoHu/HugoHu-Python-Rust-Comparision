"""CLI interface for word_counter project.
"""
import argparse
import resource
import time
import psutil


def count_words(filename):
    """
    Count words in a text file.
    input: filename (str)
    output: word_count (int)
    """
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)


def main():
    parser = argparse.ArgumentParser(description="Count words in a text file")
    parser.add_argument("filename", help="Path to the text file")
    args = parser.parse_args()

    start_mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start_time = time.time()

    word_count = count_words(args.filename)

    core_usage = psutil.cpu_percent(interval=1, percpu=True)
    num_cores = len(core_usage)
    # Sum up the usage of all CPU cores
    total_usage = sum(core_usage)

    # Calculate the average CPU core usage
    average_usage = total_usage / num_cores

    end_time = time.time()
    execution_time = end_time - start_time
    end_mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    print(f"Word count: {word_count}")
    print(f"Time taken: {execution_time:.6f} seconds")
    print(f"Average CPU core usage: {average_usage:.2f}%")
    print(f"Memory usage: {end_mem_usage - start_mem_usage} kilobytes")
