# prompt: create a function that creates a menu and waits for user input for the following options: Add a student grade.
# View all scores.
# Calculate the average grade.
# Save scores to a file.
# Load scores from a file.
# Exit the program.

import os

def add(grades):
  name = input("Enter student name: ")
  while True:
    try:
      grade = int(input("Enter student score (0-100): "))
      if 0 <= grade <= 100:
        grades[name] = grade
        print(f"Grade for {name} added successfully!")
        break
      else:
        print("Invalid input. Please enter a number between 0 and 100.")
    except ValueError:
      print("Invalid input. Please enter a number.")


def report(grades):
  if not grades:
    print("No scores entered yet.")
  else:
    print("\nStudent Scores:")
    for student, grade in grades.items():
      print(f"{student}: {grade}")

def average(grades):
  if not grades:
    print("No grades entered yet.")
  else:
    average_grade = sum(grades.values()) / len(grades)
    print(f"Average score: {average_grade:.2f}")

def save(grades):
  filename = input("Enter filename to save scores: ")
  try:
    with os.open(filename, 'w') as file:
      for student, grade in grades.items():
        file.write(f"{student},{grade}\n")
    print(f"Grades saved to {filename}")
  except Exception as e:
    print(f"Error saving scores: {e}")

def openFrom(grades):
  filename = input("Enter filename to load scores from:")
  try:
    with os.open(filename, 'r') as file:
      grades.clear()  # Clear existing grades before loading
      for line in file:
        student, grade = line.strip().split(',')
        grades[student] = int(grade)
    print(f"Scores loaded from {filename}")
  except FileNotFoundError:
    print(f"File '{filename}' not found.")
  except Exception as e:
    print(f"Error loading scores: {e}")


def load():
    grades = {}

    while True:
        print("\nMenu:")
        print("1. Add scores")
        print("2. View all scores")
        print("3. Calculate the average scores")
        print("4. Save scores to a file")
        print("5. Load scores from a file")
        print("6. Exit the program")

        choice = input("Enter your choice (1-6): ")

        match choice:
          case "1":
            add(grades)
          case "2":
            report(grades)
          case "3":
            average(grades)
          case "4":
            save(grades)
          case "5":
            openFrom(grades)
          case "6":
            print("Exiting the program...")
            break
          case _:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Start the program
load()