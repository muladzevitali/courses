import threading

garlic_count = 0
pencil_lock = threading.Lock()


def chopper():
    global garlic_count

    for i in range(10_000_000):
        pencil_lock.acquire()
        garlic_count += 1
        pencil_lock.release()


if __name__ == '__main__':
    barron = threading.Thread(target=chopper)
    olivia = threading.Thread(target=chopper)

    barron.start()
    olivia.start()

    barron.join()
    olivia.join()

    print('we should buy', garlic_count, 'garlic')
