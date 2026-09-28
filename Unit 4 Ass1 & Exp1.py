# Scenario 
import numpy as np

heart_rates = np.random.randint(80, 151, size=10)

print("Heart rates:", heart_rates)

first_5_minutes = heart_rates[:5]
print("First 5 minutes:", first_5_minutes)

maximum = np.max(heart_rates)
minimum = np.min(heart_rates)
average = np.mean(heart_rates)

print("Maximum heart rate:", maximum, "bpm")
print("Minimum heart rate:", minimum, "bpm")
print("Average heart rate:", average, "bpm")

minutes_exceeded = np.where(heart_rates > 120)[0] + 1

print("Minutes where heart rate exceeded 120 bpm:", minutes_exceeded)

#Create a one-dimensional NumPy array containing the numbers from 1 to 10 
import numpy as np

arr = np.arange(1, 11)
print(arr)