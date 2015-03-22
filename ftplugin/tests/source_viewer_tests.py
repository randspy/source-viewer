import os
import sys
import inspect

from unittest import TestCase, TestLoader, TextTestRunner, TestSuite

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import source_viewer as viewer

class ExtractFileNameTest(TestCase):

    def test_when_file_name_exists_return_it(self):

        self.assertEqual(viewer.extract_file_name('12:23:12 <main.cpp#3>'), "main.cpp")

    def test_when_file_name_exists_does_not_exists_return_empty_string(self):

        self.assertEqual(viewer.extract_file_name("12:23:12 ain.cpp#3>"), "")
        self.assertEqual(viewer.extract_file_name("12:23:12 <#3>"), "")

class ExtractLineNumber(TestCase):

    def test_when_line_number_exists_return_it(self):

        self.assertEqual(viewer.extract_line_number('12:23:12 <main.cpp#3>'), 3)

    def test_when_line_number_does_not_exist_return_empty_string(self):

        self.assertEqual(viewer.extract_line_number("12:23:12 ain.cpp#3>"), 0)
        self.assertEqual(viewer.extract_line_number("12:23:12 <main.cpp#>"), 0)


class SourceViewerTest(TestCase):


    def test_when_does_not_contain_file_signature_return_default_values(self):
        file_name, line_number = viewer.source_signature('', '')
        self.assertEqual(file_name, '')
        self.assertEqual(line_number, 0)

    def test_when_does_contain_file_signature_return_default_values(self):
        file_name, line_number = viewer.source_signature(\
            '12:23:12 <main.cpp#3>', '/home/sgluter/Programming/python/source_viewer/ftplugin/tests')

        self.assertEqual('/home/sgluter/Programming/python/source_viewer/ftplugin/tests/test_directory/matching_file/main.cpp', file_name)
        self.assertEqual(3, line_number)

    def test_when_path_is_empty_return_default_values(self):
        file_name, line_number = viewer.source_signature(\
            '12:23:12 <main.cpp#3>', '')

        self.assertEqual('', file_name)
        self.assertEqual(0, line_number)


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ExtractFileNameTest),
        loader.loadTestsFromTestCase(ExtractLineNumber),
        loader.loadTestsFromTestCase(SourceViewerTest),
        ))

    runner = TextTestRunner(verbosity = 2)
    runner.run(suite)