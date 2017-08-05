import dbMethods
import models

class GephiEdgeManager:

    def get(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(id=kwargs["id"])[0]
            return models.GephiEdge(
                source = row[0],
                target = row[1],
                type = row[2],
                id = row[3],
                weight = row[4],
            )
        if "source" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(source=kwargs["source"])[0]
            return models.GephiEdge(
                source = row[0],
                target = row[1],
                type = row[2],
                id = row[3],
                weight = row[4],
            )
        if "target" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(target=kwargs["target"])[0]
            return models.GephiEdge(
                source = row[0],
                target = row[1],
                type = row[2],
                id = row[3],
                weight = row[4],
            )

    def filter(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(id=kwargs["id"])
            EdgeList = list()
            for row in raw:
                EdgeList.append(models.GephiEdge(
                    source = row[0],
                    target = row[1],
                    type = row[2],
                    id = row[3],
                    weight = row[4],
                ))
            return EdgeList

        if "source" in kwargs and "target" in kwargs:
            EdgeList = list()
            raw = dbMethods.read_from_db_GephiEdges(source=kwargs["source"])
            EdgeList_s = list()
            for row in raw:
                EdgeList_s.append(models.GephiEdge(
                    source = row[0],
                    target = row[1],
                    type = row[2],
                    id = row[3],
                    weight = row[4],
                ))
            raw = dbMethods.read_from_db_GephiEdges(target=kwargs["target"])
            EdgeList_t = list()
            for row in raw:
                EdgeList_t.append(models.GephiEdge(
                    source = row[0],
                    target = row[1],
                    type = row[2],
                    id = row[3],
                    weight = row[4],
                ))
            for s in EdgeList_s:
                for t in EdgeList_t:
                    if s.id == t.id:
                        EdgeList.append(s)
            return EdgeList


        if "source" in kwargs:
            raw = dbMethods.read_from_db_GephiEdges(source=kwargs["source"])
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
            raw = dbMethods.read_from_db_GephiEdges(target=kwargs["target"])
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
            raw = dbMethods.read_from_db_GephiNodes(id=kwargs["id"])[0]
            return models.GephiNode(
                id = raw[0],
                label = raw[1],
                fan_count = raw[2],
                handle = raw[3]
            )
        if "label" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(label=kwargs["label"])[0]
            return models.GephiNode(
                id = raw[0],
                label = raw[1],
                fan_count = raw[2],
                handle = raw[3]
            )
        if "handle" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(handle=kwargs["handle"])[0]
            return models.GephiNode(
                id = raw[0],
                label = raw[1],
                fan_count = raw[2],
                handle = raw[3],
            )


    def filter(self, **kwargs):
        if "id" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(id=kwargs["id"])
            NodeList = list()
            for row in raw:
                NodeList.append(models.GephiNode(
                    id = row[0],
                    label = row[1],
                    fan_count = row[2],
                    handle = row[3]
                ))
            return NodeList
        if "label" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(label=kwargs["label"])
            NodeList = list()
            for row in raw:
                NodeList.append(models.GephiNode(
                    id = row[0],
                    label = row[1],
                    fan_count = row[2],
                    handle = row[3]
                ))
            return NodeList
        if "handle" in kwargs:
            raw = dbMethods.read_from_db_GephiNodes(handle=kwargs["handle"])
            NodeList = list()
            for row in raw:
                NodeList.append(models.GephiNode(
                    id = row[0],
                    label = row[1],
                    fan_count = row[2],
                    handle = row[3]
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
                handle = row[3]
            ))
        return NodeList
