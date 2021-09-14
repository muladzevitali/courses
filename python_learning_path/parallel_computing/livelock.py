import threading
import time
import random

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count

    while sushi_count > 0:
        first_chopstick.acquire()
        if not second_chopstick.acquire(blocking=False):
            print(name, 'released their first chopstick')
            first_chopstick.release()
            time.sleep(random.random() / 10)
        try:
            if sushi_count > 0:
                sushi_count -= 1

                print(name, 'took a piece, remaining', sushi_count)

            if sushi_count == 100:
                raise ZeroDivisionError
        finally:
            second_chopstick.release()
            first_chopstick.release()


if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Olivia', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Steve', chopstick_c, chopstick_a)).start()
