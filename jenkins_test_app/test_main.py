from jenkins_test_app.main import message


def test_message():
    assert message() == "Hallo Welt!"

