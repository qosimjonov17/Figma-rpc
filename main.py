import threading
import time

from rpc import connect, update
from timer import Timer

timer = Timer()


def rpc_loop():
    while True:
        try:
            update(timer.timestamp())
        except Exception as e:
            print("RPC Error:", e)

        time.sleep(15)


def main():

    connect()

    if timer.data["start_time"] is None:
        timer.start()

    threading.Thread(
        target=rpc_loop,
        daemon=True
    ).start()

    while True:
        elapsed = timer.elapsed()

        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60

        print(
            f"\rRunning: {hours:02}:{minutes:02}:{seconds:02}",
            end=""
        )

        time.sleep(1)


if __name__ == "__main__":
    main()
