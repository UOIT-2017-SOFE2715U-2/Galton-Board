from random import randint

class Node:
    __right_sibling = None
    __left_child = None
    __right_child = None
    __index = None

    def __init__(self,index):
        self.__right_sibling = None
        self.__left_child = None
        self.__right_child = None
        self.__index = index

    def set_right_sibling(self,right_sibling):
        self.__right_sibling = right_sibling

    def set_left_child(self,left_child):
        self.__left_child = left_child

    def set_right_child(self,right_child):
        self.__right_child = right_child

    def get_right_sibling(self):
        return self.__right_sibling

    def get_left_child(self):
        return self.__left_child

    def get_right_child(self):
        return self.__right_child

    def get_index(self):
        return self.__index


class Pyramid:
    __levels = 0
    __root = Node

    def __init__(self, levels=13):
        self.__levels = 1
        # first node at level 0 with index 0
        self.__root = Node(0)
        upper_level_left_most = self.__root
        for i in xrange(1, levels):
            upper_level_left_most = self.add_level(upper_level_left_most)

    def add_level(self, upper_level_left_most):
        # levels start from 0
        # index of nodes starts from 0
        # range of index from 0 to level
        # create the left most node
        upper_level_node = upper_level_left_most
        i = 0
        new_node = Node(i)
        left_most = new_node
        upper_level_node.set_left_child(new_node)

        while True:
            i += 1
            prev_new_node = new_node
            new_node = Node(i)
            prev_new_node.set_right_sibling(new_node)
            upper_level_node.set_right_child(new_node)
            upper_level_node = upper_level_node.get_right_sibling()
            if upper_level_node is None:
                self.__levels += 1
                return left_most
            upper_level_node.set_left_child(new_node)

    def random_next(self, node):
        random = randint(1,2)
        if random == 1:
            return node.get_left_child()
        else:
            return node.get_right_child()

    def random_path(self):
        index = 0
        node = self.__root
        # We stop applying random 1 level before last level.
        # The random next of that level give us the node on last level
        # nodes of last level are index of horizontal position
        # levels = total number of levels
        for l in xrange(0, self.__levels - 1):
            node = self.random_next(node)
        index = node.get_index()
        return index
