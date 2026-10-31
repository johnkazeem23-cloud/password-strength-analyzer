# Password Strength Analyzer

A lightweight Python-based cybersecurity tool that evaluates password characteristics using predefined security rules and provides recommendations for improving password quality.

## Project Overview

The Password Strength Analyzer is an educational cybersecurity project developed to demonstrate how Python can be applied to basic password security assessment.

It evaluates password length, character diversity and the presence of commonly used passwords. Based on these checks, it generates a score, assigns a strength category and provides recommendations.

## Project Objectives

- Assess basic password characteristics.
- Identify passwords included in a predefined common-password list.
- Evaluate password length and character diversity.
- Generate a rule-based strength score.
- Provide recommendations for improving password quality.
- Practise modular Python programming and secure input handling.

## Features

- **Hidden password input:** Uses Python's `getpass` module to prevent passwords from appearing on the terminal during interactive input.
- **Common-password detection:** Checks against a small predefined list of commonly used passwords.
- **Length assessment:** Evaluates password length against configured thresholds.
- **Character diversity:** Checks for lowercase letters, uppercase letters, digits and punctuation.
- **Scoring:** Assigns a score out of six based on implemented rules.
- **Classification:** Categorises results as weak, moderate or stronger characteristics.
- **Recommendations:** Identifies characteristics that could be improved.

## Technologies Used

- Python 3
- `getpass`
- `string`
- Pytest for automated testing

The application itself uses Python's standard library and does not require third-party runtime packages.

## Project Structure

```text
password-analyzer/
├── password_analyzer.py
├── README.md
├── .gitignore
├── tests/
│   └── test_password_analyzer.py
└── .venv/                 # Local environment; not uploaded
```

## Installation

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
```

Navigate into the project:

```bash
cd password-analyzer
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

Install the testing dependency:

```bash
python -m pip install pytest
```

## Usage

Run the application:

```bash
python password_analyzer.py
```

Enter a fictional test password when prompted. The application will display its score, classification and recommendations.

## Running Tests

Run the automated tests with:

```bash
python -m pytest -v
```

The tests cover common-password detection, short passwords, character diversity and recommendation behaviour.

## Assessment Logic

The application uses six rule-based checks:

1. Password length of at least eight characters.
2. Password length of at least twelve characters.
3. Presence of lowercase letters.
4. Presence of uppercase letters.
5. Presence of digits.
6. Presence of punctuation characters.

Each satisfied check contributes one point, except that a password matching the predefined common-password list immediately receives zero.

## Limitations

This is a basic educational assessment tool, not a comprehensive password-strength estimator.

- The common-password list is limited.
- The scoring model is rule-based and does not measure actual password entropy.
- It does not estimate real-world password-cracking time.
- It does not detect all predictable patterns or dictionary-based variations.
- A high score does not guarantee that a password is secure.

For real accounts, use unique passwords, a reputable password manager and multifactor authentication.

## Ethical Use

This project is intended for educational purposes and defensive password-security awareness.

Use fictional test passwords. Never enter real account passwords or sensitive credentials into this demonstration tool.

## Author

**Nureni John**

Cybersecurity Learner | Criminology and Security Studies Graduate

*Building. Learning. Securing.*
