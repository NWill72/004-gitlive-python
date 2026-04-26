#//////////////////////////////////////////////////////////////////////////////////////////////////////
#// OHMS LAW CALCULATOR IN PYTHON - DRAFT - Program Developed By Nigel A Williams                    //
#// This program is a simple Ohm's Law calculator written in Python.                                 //
#// It allows the user to calculate voltage, current, and resistance based on Ohm's Law (V = I * R). //
#// It provides a simple menu interface for the user to select which calculation to perform.         //
#////////////////////////////////////////////////////////////////////////////////////////////////////// 

#// OhmsLawPython - OhmsLawPython.py
#// A simple Ohm's Law calculator in Python
#// Developed by Nigel A Williams
#// Copyright (c) 2025

import sys
import msvcrt  # Only works on Windows for keyboard input like getch()

def calculate_voltage():
    print("\n")
    print("CALCULATE VOLTAGE")
    try:
        amps = float(input("Enter The Current Value in Amps: "))
        if amps < 0:
            raise ValueError
        ohms = float(input("Enter The Resistance Value in Ohms: "))
        if ohms < 0:
            raise ValueError
        print(f"The Voltage is: {amps * ohms} Volts.")
    except ValueError:
        print("Invalid input! Please enter a valid positive number.")

def calculate_current():
    print("\n")
    print("CALCULATE CURRENT")
    try:
        volts = float(input("Enter The Voltage Value in Volts: "))
        if volts < 0:
            raise ValueError
        ohms = float(input("Enter The Resistance Value in Ohms: "))
        if ohms <= 0:
            raise ValueError
        print(f"The Current is: {volts / ohms} Amps.")
    except ValueError:
        print("Invalid input! Please enter a valid positive number.")

def calculate_resistance():
    print("\n")
    print("CALCULATE RESISTANCE")
    try:
        volts = float(input("Enter The Voltage Value in Volts: "))
        if volts < 0:
            raise ValueError
        amps = float(input("Enter The Current Value in Amps: "))
        if amps <= 0:
            raise ValueError
        print(f"The Resistance is: {volts / amps} Ohms.")
    except ValueError:
        print("Invalid input! Please enter a valid positive number.")

def main():
    print("=" * 30)
    print("A BASIC OHMS LAW CALCULATOR IN PYTHON")
    print("=" * 30)
    print("SELECT CHOICE FROM MENU ITEMS")
    print("1. CALCULATE VOLTAGE")
    print("2. CALCULATE CURRENT")
    print("3. CALCULATE RESISTANCE")
    print("=" * 30)
    print("\nPress ESC to stop")

    while True:
        key = msvcrt.getch()
        if key == b'\x1b':  # ESC key
            print("\n")
            print("Escape Key Pressed ... !!!")
            print("Exiting Application ... !!!")
            break
        elif key == b'1':
            calculate_voltage()
        elif key == b'2':
            calculate_current()
        elif key == b'3':
            calculate_resistance()
        else:
            print("Invalid Selection! Try Again.")

if __name__ == "__main__":
    main()


# Python switch ... case
# def switch_example(value):
#   match value:
#       case 1:
#           return "Option 1 selected"
#       case 2:
#           return "Option 2 selected"
#       case 3:
#           return "Option 3 selected"
#       case _:
#           return "Default case"
#
# print(switch_example(2))  # Output: Option 2 selected

