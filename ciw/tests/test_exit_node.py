import unittest
import ciw

class TestExitNode(unittest.TestCase):

    def test_init_method(self):
        n = ciw.ExitNode()
        self.assertEqual(n.id_number, -1)
        self.assertEqual(n.all_individuals, [])
        self.assertEqual(n.next_event_date, float('Inf'))
        self.assertEqual(n.node_capacity, float('Inf'))

        n = ciw.ExitNode()
        self.assertEqual(n.id_number, -1)
        self.assertEqual(n.all_individuals, [])
        self.assertEqual(n.next_event_date, float('Inf'))
        self.assertEqual(n.node_capacity, float('Inf'))

    def test_repr_method(self):
        n = ciw.ExitNode()
        self.assertEqual(str(n), 'Exit Node')

        n = ciw.ExitNode()
        self.assertEqual(str(n), 'Exit Node')

    def test_accept_method(self):
        n = ciw.ExitNode()
        i1 = ciw.Individual(3)
        i2 = ciw.Individual(8)
        self.assertEqual(n.all_individuals, [])
        n.accept(i1, 42.1)
        self.assertEqual(n.all_individuals, [i1])
        n.accept(i2, 51.8)
        self.assertEqual(n.all_individuals, [i1, i2])

    def test_update_next_event_date_method(self):
        n = ciw.ExitNode()
        self.assertEqual(n.id_number, -1)
        self.assertEqual(n.all_individuals, [])
        self.assertEqual(n.next_event_date, float('Inf'))
        self.assertEqual(n.node_capacity, float('Inf'))

        n.update_next_event_date()

        self.assertEqual(n.id_number, -1)
        self.assertEqual(n.all_individuals, [])
        self.assertEqual(n.next_event_date, float('Inf'))
        self.assertEqual(n.node_capacity, float('Inf'))

