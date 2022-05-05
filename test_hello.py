from hello import add, toyou, substract


def setup_function(function):
	print(f"Running Setup: {function.__name__}")
	function.x = 10

def teardown_function(function):
	print(f"Running Teardown: {function.__name__}")
	del function.x


def test_hello_substract():
    assert substract(test_hello_substract.x) == 9
