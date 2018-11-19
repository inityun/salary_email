import threading
import time


class MyThread(threading.Thread):


    def __init__(self):
        super(MyThread, self).__init__()

        # self.th1 = threading.Thread(target=self.sub_threading)
        self.sub_threading()

    def sub_threading(self):
        time.sleep(10)
        print('''
        主线程：{}
        子线程：{}
        '''.format(threading.main_thread(), threading.current_thread()))
    #     t3 = MyThread1()
    #     t3.start()
    #
    # def run(self):
    #     self.th1.start()

# class MyThread1(threading.Thread):
#
#
#     def __init__(self):
#         super(MyThread1, self).__init__()
#
#         self.th1 = threading.Thread(target=self.sub_threading)
#
#
#     def sub_threading(self):
#         print('''
#         主线程：{}
#         子线程：{}
#         '''.format(threading.main_thread(), threading.current_thread()))
#     def run(self):
#         self.th1.start()
def demo_sleep():
    time.sleep(10)
    print('done')

if __name__ == '__main__':

    def gen():
        for i in range(100):
            yield i

    def threading_generator_demo(gen):

        # while True:
        #     try:
        #         print(next(gen), threading.currentThread())
        #     except Exception:
        #         break
        for i in gen:
            print(i, threading.currentThread())
            # time.sleep(0.1)


    gen = gen()


    for i in range(4):
        t = threading.Thread(target=threading_generator_demo, args=(gen,))
        t.start()
    print(threading.enumerate())



    # t1 = threading.Thread(target=demo_sleep)
    # t1.start()
    # print(1)
    #
    # t1.join()