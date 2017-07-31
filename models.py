import dbMethods
import managers

class GephiNode:
    """ The Class for the nodes of the twitter network
    """
    def __init__(self, id, label, fan_count, handle):
        self.id = id
        self.label = label
        self.fan_count = fan_count
        self.handle = handle

    def create(self):
        if len(GephiNode.objects.filter(handle=self.handle)) == 0:
            dbMethods.dynamic_data_entry_Nodes(
                self.id,
                self.label,
                self.fan_count,
                self.handle
            )
        else:
            print('Already exists')

    objects = managers.GephiNodeManager()

class GephiEdge:
    """ The Class for the edge of the twitter network
    """
    def __init__(self, source, target, type, id, weight):
        self.source = source
        self.target = target
        self.type = type
        self.id = id
        self.weight = weight

    def create(self):
        if len(GephiEdge.objects.filter(source=self.source, target=self.target)) == 0:
            dbMethods.dynamic_data_entry_Edges(
                self.source,
                self.target,
                self.type,
                self.id,
                self.weight
            )
        else:
            print('Already exists')

    objects = managers.GephiEdgeManager()
