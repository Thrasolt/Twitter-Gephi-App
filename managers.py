import dbMethods
import models

class GephiEdgeManager:

    def get(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(id=kwargs[id])[0]
            return models.GephiEdge(
                source = raw[0],
                target = raw[1],
                type = raw[2],
                weight = raw[3],
                id = raw[4],
            )
        if "source" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(source=kwargs[source])[0]
            return models.GephiEdge(
                source = raw[0],
                target = raw[1],
                type = raw[2],
                weight = raw[3],
                id = raw[4],
            )
        if "target" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(target=kwargs[target])[0]
            return models.GephiEdge(
                source = raw[0],
                target = raw[1],
                type = raw[2],
                weight = raw[3],
                id = raw[4],
            )

    def filter(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(id=kwargs[id])
            EdgeList = list()
            for row in raw:
                EdgeList.append(models.GephiEdge(
                    source = row[0],
                    target = row[1],
                    type = row[2],
                    weight = row[3],
                    id = row[4],
                ))
            return EdgeList

        if "source" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(source=kwargs[source])
            EdgeList = list()
            for row in raw:
                EdgeList.append(models.GephiEdge(
                    source = row[0],
                    target = row[1],
                    type = row[2],
                    weight = row[3],
                    id = row[4],
                ))
            return EdgeList

        if "target" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(target=kwargs[target])
            EdgeList = list()
            for row in raw:
                EdgeList.append(models.GephiEdge(
                    source = row[0],
                    target = row[1],
                    type = row[2],
                    weight = row[3],
                    id = row[4],
                ))
            return EdgeList

    def all(self):
        raw = dbMethods.read_from_db_GephiEdges()
        NodeList = list()
        for row in raw:
            NodeList.append(models.GephiEdge(
                source = row[0],
                target = row[1],
                type = row[2],
                weight = row[3],
                id = row[4],
            ))
        return NodeList

class GephiNodeManager:

    def get(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(id=kwargs[id])[0]
            return models.GephiNode(
                id = raw[0],
                label = raw[1],
                fan_count = raw[2],
                category = raw[3]
            )
        if "label" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(label=kwargs[label])[0]
            return models.GephiNode(
                id = raw[0],
                label = raw[1],
                fan_count = raw[2],
                category = raw[3]
            )

    def filter(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(id=kwargs[id])
            NodeList = list()
            for row in raw:
                NodeList.append(models.GephiNode(
                    id = row[0],
                    label = row[1],
                    fan_count = row[2],
                    category = row[3]
                ))
            return NodeList
        if "label" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(label=kwargs[label])
            NodeList = list()
            for row in raw:
                NodeList.append(models.GephiNode(
                    id = row[0],
                    label = row[1],
                    fan_count = row[2],
                    category = row[3]
                ))
            return NodeList

    def all(self):
        raw = dbMethods.read_from_db_GephiNodes()
        NodeList = list()
        for row in raw:
            NodeList.append(models.GephiNode(
                id = row[0],
                label = row[1],
                fan_count = row[2],
                category = row[3]
            ))
        return NodeList
