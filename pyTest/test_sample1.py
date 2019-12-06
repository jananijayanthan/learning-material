import pytest

def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed" 
	assert x == y,"test failed"

def test_file1_method3():
    a = 2
    b = 3
    assert a == 2, "test failed "

# assert essentially means this IS this. so by saying assert a == 2 you are declaring this is true. It will then return
# boolean true or false. 
# the string after assert is the failure message - this will be displayed when the test is run and highlighted if the test 
# fails. 