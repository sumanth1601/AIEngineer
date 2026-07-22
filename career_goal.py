def calculate_grade(percentage):
    """
    Assigns a descriptive grade based on the percentage score.
    Logic based on user requirements:
    90-100: Excellent
    75-89: Good
    50-74: Average
    Below 50: Need Improvement
    """
    if 90 <= percentage <= 100:
        return "Excellent"
    elif 75 <= percentage < 90:
        return "Good"
    elif 50 <= percentage < 75:
        return "Average"
    else:
        return "Need Improvement"


def main():
    print("--- Student Marks Program ---")
    subjects = []

    # Define how many subjects to input
    try:
        num_subjects = int(input("How many subjects would you like to enter? "))
        if num_subjects <= 0:
            print("Please enter a valid number of subjects.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    # Collect marks
    for i in range(num_subjects):
        while True:
            try:
                score = float(input(f"Enter marks for subject {i + 1} (0-100): "))
                if 0 <= score <= 100:
                    subjects.append(score)
                    break
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a numeric value.")

    # Calculations
    total_marks = sum(subjects)
    average_percentage = total_marks / num_subjects
    final_grade = calculate_grade(average_percentage)

    # Output results
    print("\n" + "=" * 30)
    print(f"RESULTS SUMMARY")
    print("=" * 30)
    print(f"Total Marks:       {total_marks:.2f}")
    print(f"Average:           {average_percentage:.2f}%")
    print(f"Final Performance: {final_grade}")
    print("=" * 30)


if __name__ == "__main__":
    main()
