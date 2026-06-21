from logic_utils import check_guess


def test_correct_guess_returns_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high_returns_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low_returns_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_one_above_secret_is_too_high():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"


def test_guess_one_below_secret_is_too_low():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"


def test_high_hint_does_not_say_higher():
    # Regression: the original bug swapped the messages — "Too High" wrongly said "Go HIGHER"
    _, message = check_guess(99, 1)
    assert "HIGHER" not in message


def test_low_hint_does_not_say_lower():
    # Regression: mirror of the above — "Too Low" should never say "Go LOWER"
    _, message = check_guess(1, 99)
    assert "LOWER" not in message
