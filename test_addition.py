def test_addition():
    assert 1 + 1 == 2

if __name__ == "__main__":
    with open("test_output.txt", "w") as f:
        try:
            test_addition()
            f.write("Test Passed: 1 + 1 == 2\n")
        except AssertionError:
            f.write("Test Failed: 1 + 1 != 2\n")
            raise
