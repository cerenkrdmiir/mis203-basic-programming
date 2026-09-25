total_score = 0
student_count = 0

while True:
    name= input("Enter student name (or q to quit): ")
    
    if name.lower() =='q':
        break
        
    score_input = float(input("Enter score: "))
    
    if score_input <0 or score_input > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue
        
    if score_input >= 90:
        grade= "A"
    elif score_input >= 80:
        grade= "B"
    elif score_input >= 70:
        grade= "C"
    elif score_input >= 60:
        grade= "D"
    else:
        grade= "F"
        
    print(f"{name}: {score_input:.0f} -> {grade}")
    
    total_score += score_input
    student_count += 1

if student_count> 0:
    avg_score =total_score/ student_count
    print(f"total students:{student_count}")
    print(f"average score: {avg_score:.2f}")
else:
    print("no students entered.")
