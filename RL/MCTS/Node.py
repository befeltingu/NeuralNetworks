'''
    Node class module used as part of a tree data structure

'''



class Node(object):

    '''
        General Tree structure:
                A
                |
              / | |
            A1 A2 A3

        Each node is itself a Tree
        whith attributes player,pot
    '''

    def __init__(self,player,pot,parent=None,action=None,node_index=None):

        self.node_index = node_index

        self.player = player

        self.pot = pot

        self.action = action

        self.children = []

        self.parent = parent

        self.visit_count = 0 # number of times the node has been visited in MCTS

        self.current_value = 0 # value of node for current player