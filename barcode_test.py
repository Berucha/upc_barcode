from barcode_draw import *
import sys

def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def a7_test_suite():
    testit(is_valid_input("1") == False)
    testit(is_valid_input("121212121212212") == False)
    testit(is_valid_input("121212121212") == True)
    testit(is_valid_input("11212sqw1212") == False)
    testit(is_valid_input("asdfghjklqwe") == False)

a7_test_suite()
