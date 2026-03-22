from logic_utils import check_guess

# ORIGINAL STARTER TESTS
# These were broken because check_guess returns a tuple (outcome, message)
# but the original tests compared result directly to a string like "Win".
# Fixed by unpacking the tuple: outcome, message = check_guess(...)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # Fixed: unpacked tuple instead of comparing result == "Win"
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # Fixed: unpacked tuple instead of comparing result == "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # Fixed: unpacked tuple instead of comparing result == "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Tests targeting bugs we fixed ---

def test_hint_direction_too_high():
    # BUG FIX: hints were swapped in check_guess — when guess > secret the message said
    # "Go HIGHER" but it should say "Go LOWER". Fixed in both the try and except branches.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_direction_too_low():
    # BUG FIX: hints were swapped in check_guess — when guess < secret the message said
    # "Go LOWER" but it should say "Go HIGHER". Fixed in both the try and except branches.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_out_of_range_guess_hint():
    # BUG FIX: typing a number way above the range (e.g. 1000) still goes through check_guess.
    # It should return "Too High" and tell the player to go lower, not higher.
    outcome, message = check_guess(1000, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
