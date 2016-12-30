"""
CMSC671: Artificial Intelligence Project Phase 2
12 December 2016
Rule Breakers:
    Vikramaditya Battina
    Sri Konuru
    Nikhil Kumar Mengani
    Alexander Spizler
"""


class DecisionTreeNode:

    """
    Decision Tree Node
    Attributes: Name, List of Child Pointers
    Special Attribute Name: "True", "False" which says its a leaf.
    """

    def __init__(self, name="", child_list=None):
        if child_list is None:
            child_list = []
        self.name = name
        self.childList = child_list

    def child_list(self):
        return self.childList

    def set_child_list(self, child_list):
        self.childList = child_list

    def name(self):
        return self.name

    def set_name(self, name):
        self.name = name
