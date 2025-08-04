from deepfocus import timer

def test_countdown_runs_without_error():
    try:
        timer.countdown(0.01, "Test Phase")  # ~1 sec
        assert True
    except Exception as e:
        assert False, f"Timer failed: {e}"
