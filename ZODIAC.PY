# Zodiac App - A zodiac application that provides horoscope information

print("Welcome to Zodiac Based Prediction")

name = input("What is your name? ")
zodiac = input("Enter your zodiac sign (e.g., Aries): ").strip().lower()

print(f"\nHello, {name}! Here is your prediction:\n")

if zodiac == "aries":
    print("Complete your long-pending task. Today is a good day to finish it.")
elif zodiac == "taurus":
    print("Patience will bring you success.")
elif zodiac == "gemini":
    print("You may meet someone new today.")
elif zodiac == "cancer":
    print("Spend quality time with your family.")
elif zodiac == "leo":
    print("Your confidence will help you achieve your goals.")
elif zodiac == "virgo":
    print("Focus on planning before taking action.")
elif zodiac == "libra":
    print("Balance and harmony will lead to positive outcomes.")
elif zodiac == "scorpio":
    print("Trust your instincts while making important decisions.")
elif zodiac == "sagittarius":
    print("A new opportunity may come your way.")
elif zodiac == "capricorn":
    print("Hard work will bring rewarding results.")
elif zodiac == "aquarius":
    print("Your creativity will help solve a problem.")
elif zodiac == "pisces":
    print("Listen to your intuition and stay positive.")
else:
    print("Sorry, the zodiac sign entered is not recognized.")
