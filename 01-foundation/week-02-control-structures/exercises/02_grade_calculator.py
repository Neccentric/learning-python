# Exercise 2: Grade Calculator
# TODO: Create a grade calculator that converts numerical scores to letter grades

# Get the numerical score from user
# score = float(input("Enter your numerical score (0-100): "))

# TODO: Convert score to letter grade:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

# TODO: Add validation:
# - Check if score is between 0 and 100
# - Handle invalid input

# TODO: Provide additional feedback:
# - "Excellent work!" for A
# - "Good job!" for B
# - "Satisfactory" for C
# - "Needs improvement" for D
# - "Please see instructor" for F

# Your code here:
try:
    score = float (input("Enter your numerical score (0-100): "))

    #Validate Score.
    if score < 0 and score > 100:
        print("Error: Score must be between 0 and 100!.")
    else:
        #Determine Letter grade and Feedback.
        if score >= 90:
            Letter_grade = "A"
            feedback = "Excellent work!"
            gpa_points = 4.0
        elif score >= 80:
            Letter_grade = "B"
            feedback = "Good job!"
            gpa_point = 3.0
        elif score >= 70:
            Letter_grade = "C"
            feedback = "Satisfactory"
            gpa_point = 2.0
        elif score >= 60:
            Letter_grade = "D"
            feedback = "Needs Improvement"
            gpa_point = 1.0
        elif score < 60:
            Letter_grade = "F"
            feedback = "Please see your Instructor"
            gpa_point = 0.0

        # Display results
        print(f"\n📊 GRADE REPORT")
        print(f"{'='*30}")
        print(f"Numerical Score: {score:.1f}")
        print(f"Letter Grade: {Letter_grade}")
        print(f"GPA Points: {gpa_point}")
        print(f"Feedback: {feedback}")

        # Additional insights
        if score >= 97:
            print("🌟 Outstanding performance!")
        elif score >= 93:
            print("⭐ Excellent work!")
        elif score == 100:
            print("🏆 Perfect score! Amazing!")
        
        # Grade boundary information
        if Letter_grade == "B" and score >= 87:
            points_to_A = 90 - score
            print(f"💡 You're only {points_to_A:.1f} points away from an A!")
        elif Letter_grade == "C" and score >= 77:
            points_to_B = 80 - score
            print(f"💡 You're only {points_to_B:.1f} points away from a B!")
        elif Letter_grade == "D" and score >= 67:
            points_to_C = 70 - score
            print(f"💡 You're only {points_to_C:.1f} points away from a C!")
        elif Letter_grade == "F" and score >= 55:
            points_to_D = 60 - score
            print(f"💡 You need {points_to_D:.1f} more points to pass!")
        
        # Percentage display
        print(f"📈 Percentage: {score}%")
        
        # Pass/Fail status
        if score >= 60:
            print("✅ Status: PASS")
        else:
            print("❌ Status: FAIL")
        
except ValueError:
    print("Error: Please Enter a valid Number!")
except Exception as e:
    print(f"An Unexpected error occured: {e}")