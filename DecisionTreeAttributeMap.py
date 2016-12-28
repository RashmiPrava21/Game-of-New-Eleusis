"""
CMSC671: Artificial Intelligence Project Phase 2
12 December 2016
Rule Breakers:
    Vikramaditya Battina
    Sri Konuru
    Nikhil Kumar Mengani
    Alexander Spizler
"""


class DecisionTreeAttributeMap:

    """
    Map from DecisionTreeNode name to tuple of (function name, function outputs list, function, function var list)
    """

    def __init__(self):
        self.attribute_map = {}

    def add(self, name, func_name, output_list,  func, func_var_list):
        self.attribute_map[name] = (func_name, output_list, func, func_var_list)

    def get(self, name):
        return self.attribute_map[name]
