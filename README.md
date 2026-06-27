# ZODIAC app -A zodiac application that provides horoscope information based on zodiac sign
## Overview

The Zodiac Prediction App is a simple Python console application that provides a basic horoscope prediction based on the user's zodiac sign. The application prompts the user to enter their name and zodiac sign, then displays a personalized prediction.

This project is designed as a beginner-friendly Python application to demonstrate the use of user input, conditional statements, string handling, and formatted output.

---

## Features

* Accepts the user's name.
* Accepts the user's zodiac sign.
* Displays a personalized prediction.
* Simple command-line interface.
* Beginner-friendly Python project.

---

## Technologies Used

* Python 3

---

## Project Structure

```text
Zodiac-Prediction-App/
│
├── zodiac.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Zodiac-Prediction-App.git
```

Navigate to the project directory:

```bash
cd Zodiac-Prediction-App
```

---

## Run the Application

Execute the following command:

```bash
python zodiac.py
```

or

```bash
python3 zodiac.py
```

---

## Example

### Input

```text
What is your name?
Nek

Enter your zodiac sign:
Aries
```

### Output

```text
Hello, Nek!

Here is your fortune:

Complete your long pending task.
```

---

## Supported Zodiac Signs

* Aries
* Taurus
* Gemini

Additional zodiac signs can be added by extending the conditional statements in the source code.

---

## Learning Objectives

This project demonstrates:

* User input using `input()`
* Conditional statements (`if`, `elif`, `else`)
* String formatting using f-strings
* Basic Python program structure

---

## Future Improvements

* Support all 12 zodiac signs.
* Randomized daily horoscope predictions.
* Graphical User Interface (GUI).
* Date-based zodiac sign detection.
* Multiple prediction categories (Career, Love, Health, Finance).
* Colorful terminal output.

---

## Author

Nek Sandha

Python | AI | Automation | Generative AI



print("welcome to zodiac based prediction")
name=input("what is your name?")
zodiac=input("enter your zodiac sign(eg: aries etc...)")
print(f"\n {name} ! Here is your fortune")

if zodiac=="aries":
    print("complete long pending task")
elif zodiac=="taurus":
    print("patience will bring you success")
elif zodiac=="gemini":
    print("you will meet someone new")
else:
    print("not able to recognise your zodiac ")



