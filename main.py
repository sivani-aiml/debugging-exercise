# Find and fix the bugs

def calculate_average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    average = total / len(numbers)
    return average

scores = [85, 90, 78, 92, 88]

avg = calculate_average(scores)

print("Average score:", avg)

if avg > 90:
    print("Excellent!")
elif avg > 80:
    print("Good Job!")
else:
    print("Keep Practicing!")