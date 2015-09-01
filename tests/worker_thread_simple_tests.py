import unittest

from worker import WorkerThread, Task

class TestCreateWorkerThreads(unittest.TestCase):
    
    def test_simple_creation_equality(self):
        wrk1 = WorkerThread('hello')
        wrk2 = WorkerThread('hello')
        self.assertEqual(wrk1._id, wrk2._id)
