from MyTest import MyTest
from TestCaseTest import TestCaseTest
from TestLoader import TestLoader
from TestLoaderTest import TestLoaderTest
from TestResult import TestResult
from TestRunner import TestRunner
from TestSuite import TestSuite
from TestSuiteTest import TestSuiteTest

if __name__ == "__main__":
    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)