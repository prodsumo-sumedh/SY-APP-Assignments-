import threading
import time

def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", letter)
        time.sleep(1)

def print_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=print_squares)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("All tasks completed successfully.")

'''output:
Number: 1
Letter: A
Square of 1 = 1
Letter: B
Number: 2
Square of 2 = 4
Square of 3 = 9
Letter: C
Number: 3
Letter: D
Number: 4
Square of 4 = 16
Square of 5 = 25
Number: 5
Letter: E
All tasks completed successfully.'''
