import threading
import time


class ChefOlivia(threading.Thread):
    def run(self) -> None:
        print('Olivia started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Olivia is done cutting sausage')


if __name__ == '__main__':
    print('Barron started & requesting Olivias help')
    olivia = ChefOlivia()
    print('Olivia are you alive?', olivia.is_alive())

    print('Barron tells Olivia to start.')
    olivia.start()
    print(' Olivia are you alive?', olivia.is_alive())

    print('Barron continues cooking soup.')
    time.sleep(0.5)
    print(' Olivia are you alive?', olivia.is_alive())

    print('Barron waits for olivia to finish and join')
    olivia.join()

    print(' Olivia are you alive?', olivia.is_alive())

    print('Both are done')
