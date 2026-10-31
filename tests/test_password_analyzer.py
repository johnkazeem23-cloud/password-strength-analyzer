from password_analyzer import analyze_password


def test_common_password_is_rejected():
    score, feedback = analyze_password("password123")

    assert score == 0
    assert "This is a commonly used password." in feedback


def test_short_password_receives_low_score():
    score, feedback = analyze_password("abc")

    assert score == 1
    assert "Use at least 8 characters." in feedback


def test_password_with_all_character_categories():
    score, feedback = analyze_password("Strong@Pass123")

    assert score == 6
    assert feedback == []


def test_password_without_uppercase():
    score, feedback = analyze_password("strongpass123!")

    assert "Include uppercase letters." in feedback


def test_password_without_special_characters():
    score, feedback = analyze_password("StrongPassword123")

    assert "Consider including special characters." in feedback
