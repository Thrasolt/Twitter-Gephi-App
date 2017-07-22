import dbMethods

class GephiNode:
    """ The Class for the nodes of the twitter network
    """
    def __init__(self, id, label, fan_count, category):
        self.id = id
        self.label = label
        self.fan_count = fan_count
        self.category = category
        dbMethods.dynamic_data_entry_Nodes(self.id, self.label, self.fan_count, self.category)


class GephiEdge:
        """ The Class for the edge of the twitter network
        """
    def __init__(self, source, target, type, id, weight):
        self.source = source
        self.target = target
        self.type = type
        self.id = id
        self.weight = weight
        dbMethods.dynamic_data_entry_Edges(self.source, self.target, self.type, self.id, self.weight)
