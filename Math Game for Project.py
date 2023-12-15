import random

def generate_math_problem():
    """Generate a random math problem."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    problem = f"{num1} {operator} {num2}"
    return problem

def evaluate_math_problem(problem):
    """Evaluate the solution to a math problem."""
    try:
        solution = eval(problem)
        return solution
    except ZeroDivisionError:
        return None  # Handle division by zero

def play_math_game():
    score = 0
    rounds = 5  # You can adjust the number of rounds

    for _ in range(rounds):
        math_problem = generate_math_problem()
        print("Solve the math problem:", math_problem)

        user_answer = input("Your answer: ")

        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        correct_answer = evaluate_math_problem(math_problem)

        if correct_answer is None:
            print("Error: Division by zero. Skipping this problem.")
            continue

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    print(f"Game Over. Your score: {score}/{rounds}")

if __name__ == "__main__":
    print("Welcome to the Math Problems Game!")
    play_math_game()
