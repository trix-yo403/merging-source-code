print("     >>>>PERFORMANCE ANALYSIS<<<<")
def calculate_average(subject):
    print(f"\n----Enter the marks for {subject} below----")
    assignment = float(input("    1.Assignment: "))
    course_work = float(input("    2.Course-Work: "))
    mid_term = float(input("    3.Mid-Term: "))
    eot = float(input("    4.EOT: "))
    
    subject_average = (assignment+course_work+mid_term+eot) / 4
    return subject_average  
 
physic_average = calculate_average("Physics")
economics_average = calculate_average("Econcmics")
math_average = calculate_average("Math")

total_average = ((physic_average+economics_average+math_average)/3)

print("\n----Student's Performance----")
print(f"    i.Physics Avg: {physic_average:.2f}")
print(f"    ii.Economics Avg: {economics_average:.2f}")
print(f"    iii.Math Avg: {math_average:.2f}")
print(f"\n      Total Average: {total_average:.2f}")

    