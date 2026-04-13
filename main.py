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
    suite = loader.make_suite(TestLoaderTest)

    runner = TestRunner()
    runner.run(suite)