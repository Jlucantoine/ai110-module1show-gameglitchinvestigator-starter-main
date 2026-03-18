from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Regression tests for the string-comparison bug:
# The original app.py cast secret to str on even attempts, causing
# lexicographic ordering instead of numeric. For example, "9" > "50"
# is True lexicographically, so check_guess(9, "50") wrongly returned
# "Too High" instead of "Too Low".

def test_check_guess_uses_numeric_not_string_ordering_too_low():
    # 9 < 50 numerically → "Too Low"
    # but "9" > "50" lexicographically → buggy code returned "Too High"
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low", (
        "check_guess must compare integers numerically, not as strings"
    )


def test_check_guess_uses_numeric_not_string_ordering_too_high():
    # 10 > 9 numerically → "Too High"
    # but "10" < "9" lexicographically → buggy code returned "Too Low"
    outcome, _ = check_guess(10, 9)
    assert outcome == "Too High", (
        "check_guess must compare integers numerically, not as strings"
    )
