__author__ = 'lenovo'
import unittest
import HTMLTestRunner


def all_cases():
    # 待执行的用例目录
    case_dir = 'C:\\Users\\lenovo\\PycharmProjects\\untitled1\\app_auto_project\\cases'
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='test*.py',
                                                   top_level_dir=None)

    for i in discover:
        test_suit.addTest(i)
    print(test_suit)
    return test_suit
if __name__ == "__main__":
    report_path = 'C:\\Users\\lenovo\\PycharmProjects\\untitled1\\app_auto_project\\reports\\report.html'
    fp = open(report_path, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="My report",
                                           description="Detail")
    runner.run(all_cases())

    fp.close()



