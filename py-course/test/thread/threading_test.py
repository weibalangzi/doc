import time
import random
from threading import Thread

def download(*, fileName):
    start = time.time()
    print(f'start--{fileName}')
    time.sleep(random.randint(3, 6))
    print(f'{fileName}--end')
    end = time.time()
    print(f'total {end - start:.3f}')

def main():
    threads = [
        Thread(target=download, kwargs={'fileName': '永生.txt'}),
        Thread(target=download, kwargs={'fileName': '神墓.txt'}),
        Thread(target=download, kwargs={'fileName': '遮天.txt'}),
    ]
    start = time.time()

    # 启动所有线程
    for thread in threads:
        thread.start()

    # 等待线程结束
    for thread in threads:
        thread.join()

    end = time.time()
    print(f'all: {end - start:.3f}')

if __name__ == '__main__':
    main()
