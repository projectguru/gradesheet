def add(scores):
  name = input("Enter name: ")
  try:
    score = int(input("Enter score (0-100): "))
    if 0 <= score <= 100:
      scores[name] = score
      print(f"Score for {name} added successfully!")
    else:
      print("Invalid input. Please enter a number between 0 and 100.")
  except ValueError:
    print("Invalid input. Please enter a number.")


def report(scores):
  if not scores:
    print("No scores entered yet.")
  else:
    print("\nStudent Scores:")
    for student, score in scores.items():
      print(f"{student}: {score}")

def average(scores):
  if not scores:
    print("No scores entered yet.")
  else:
    average_score = sum(scores.values()) / len(scores)
    print(f"Average score: {average_score:.2f}")

def save(scores):
  filename = input("Enter filename to save scores: ")
  try:
    with open(filename, 'w') as file:
      for student, score in scores.items():
        file.write(f"{student},{score}\n")
    print(f"Scores saved to {filename}")
  except Exception as e:
    print(f"Error saving scores: {e}")

def openFrom(scores):
  filename = input("Enter filename to load scores from:")
  try:
    with open(filename, 'r') as file:
      scores.clear()  # Clear existing scores before loading
      for line in file:
        student, score = line.strip().split(',')
        scores[student] = int(score)
    print(f"Scores loaded from {filename}")
  except FileNotFoundError:
    print(f"File '{filename}' not found.")
  except Exception as e:
    print(f"Error loading scores: {e}")


def load():
    scores = {}

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
            add(scores)
          case "2":
            report(scores)
          case "3":
            average(scores)
          case "4":
            save(scores)
          case "5":
            openFrom(scores)
          case "6":
            print("Exiting the program...")
            break
          case _:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Start the program
load()
