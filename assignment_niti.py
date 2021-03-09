import threading

class Kocka:
    def __init__(self,a):
        self.a = a
    def zapremina(self):
        print("Zapremina je: {}".format(self.a*self.a*self.a))
    def duzinaSvihIvica(self):
        print("Duzina svih ivica je: {}".format(self.a*12))
    
if __name__ == "__main__":
    kocka1 = Kocka(13)
    kocka2 = Kocka(7)
    
    t1 = threading.Thread(target=Kocka.duzinaSvihIvica, args=(kocka1,))
    t2 = threading.Thread(target=Kocka.zapremina, args=(kocka1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    t1 = threading.Thread(target=Kocka.duzinaSvihIvica, args=(kocka2,))
    t2 = threading.Thread(target=Kocka.zapremina, args=(kocka2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

