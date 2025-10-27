# Create an empty dictionary
student_data = {}

# Get number of students
num_students = int(input("no_students: "))

# Loop to get data for each student

for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    percentage = float(input(f"Enter percentage marks for {name}: "))
    student_data[name] = percentage






    
print("\n--- Student Information ---")
for name, percentage in student_data.items():
    print(f"Name: {name}, Percentage: {percentage}%")
