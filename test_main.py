from main import handler

def test_handler():
    response = handler()
    assert response["message"] == "Hello from DevOps pipeline!"
