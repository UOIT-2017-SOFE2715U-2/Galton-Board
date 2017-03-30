from pyramid import Pyramid



class GaltonBoard():

    __queue = []
    __levels = 0
    #__marbles = 0
    __pyramid = Pyramid



    def __init__(self,levels = 13):
        self.__queue = []
     #   self.__levels = levels
     #   self.__marbles = 0
        self.__pyramid = Pyramid(levels + 1)

    def fill(self, marbles):
        self.__queue = []
        for m in xrange(0,marbles):
          self.__queue.append(self.__pyramid.random_path())
        return self.__queue

    def get_queue(self):
        return self.__queue
