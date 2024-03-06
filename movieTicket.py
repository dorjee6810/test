print("Movie Ticket discount")
# Step 1: Ask user to input their age
age = int(input("Please enter your age: "))

# Step 2: Ask user if they are a student
student_status = input("Are you a student? (yes/no): ")

# Step 3: Use logical operators to determine eligibility
if age <= 12:
    print("You are eligible for a discount on the movie ticket!")
elif 13 <= age <= 18 and student_status.lower() == 'yes':
    print("You are eligible for a discount on the movie ticket!")
else:
    print("You are not eligible for a discount on the movie ticket.")
    