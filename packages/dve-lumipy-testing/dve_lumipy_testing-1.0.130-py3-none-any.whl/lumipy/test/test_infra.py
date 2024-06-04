import io
import json
import os
import sys
import traceback as tb
import unittest
from contextlib import redirect_stdout, redirect_stderr
from multiprocessing import Process, Queue
from unittest import TestLoader, TestSuite, TextTestRunner
from unittest.suite import _ErrorHolder

import lumipy as lm

class BaseIntTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = lm.get_client()


class BaseIntTestWithAtlas(BaseIntTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.atlas = lm.get_atlas()


class LumipyTestWorker(Process):

    def __init__(self, manifest, verbosity, queue: Queue):
        super().__init__()
        self.manifest = manifest
        self.verbosity = verbosity
        self.queue = queue

    def run(self):
        loader = TestLoader()
        suite = TestSuite(map(loader.loadTestsFromTestCase, self.manifest))

        stream = io.StringIO()
        sys.stdout = stream
        sys.stderr = stream

        runner = TextTestRunner(verbosity=self.verbosity, stream=stream).run(suite)

        try:
            def test_name(c):
                if isinstance(c, _ErrorHolder):
                    method, cls = c.description.split()
                    cls = cls.split('.')[-1].strip(')')
                    return f'{cls}.{method}'

                return f'{type(c).__name__}.{c._testMethodName}'

            result = [
                runner.testsRun,
                [(f'{test_name(case)}', trace) for case, trace in runner.errors],
                [(f'{test_name(case)}', trace) for case, trace in runner.failures],
            ]

            stream.seek(0)
            for line in stream.readlines():
                self.queue.put((self.name, 'log_line', line))

            self.queue.put((self.name, 'result', result))

        except Exception as e:
            self.queue.put((self.name, 'exception', ''.join(tb.format_exception(*sys.exc_info()))))


def get_logs(func):
    """
    Helper function which runs a func and captures its stdout and stderr for testing
    """
    stdout = io.StringIO()
    stderr = io.StringIO()

    with redirect_stdout(stdout), redirect_stderr(stderr):
        func()

    return stdout.getvalue(), stderr.getvalue()
