import models
import unittest

class TestGephiEdges(unittest.TestCase):

    #Managers
    def test_model_filter(self):
        source = len(models.GephiNode.objects.all()) + 5
        target = len(models.GephiNode.objects.all()) + 10
        self.assertEqual(len(models.GephiEdge.objects.filter(target=source, source=target)), 0)
        self.assertEqual(len(models.GephiEdge.objects.filter(target=1, source=1)), 0)


if __name__ == '__main__':
    unittest.main()
