import getpass
import string

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "iloveyou",
}


def analyze_password(password):
    """Evaluate password characteristics and return feedback."""

    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, [
            "This is a commonly used password.",
            "Choose a unique password instead."
        ]

    # Evaluate password length.
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Consider using 12 or more characters.")

    # Evaluate character variety.
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Consider including numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Consider including special characters.")

    return score, feedback


def main():
    print("=" * 40)
    print("     PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = getpass.getpass(
        "Enter a test password (input hidden): "
    )

    score, feedback = analyze_password(password)

    print("\nAnalysis complete.")
    print(f"Score: {score}/6")

    if score <= 2:
        print("Assessment: WEAK")
    elif score <= 4:
        print("Assessment: MODERATE")
    else:
        print("Assessment: STRONGER CHARACTERISTICS")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nNo basic character-variety recommendations.")

    print("\nNote: This is a basic educational assessment.")
    print("It does not calculate real-world crack time.")


if __name__ == "__main__":
    main()
