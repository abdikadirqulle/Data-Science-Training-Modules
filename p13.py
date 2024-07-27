import numpy as np

# Simulation parameters
num_cars = 10
num_laps = 90
num_races = 10000
mean_lap_time = 90  # seconds
std_dev_lap_time = 0.8  # seconds

# Initialize a counter for the number of wins by the 7th car
seventh_car_wins = 0

# Run the simulation for num_races
for race in range(num_races):
    # Generate lap times for each car
    lap_times = np.random.normal(mean_lap_time, std_dev_lap_time, (num_cars, num_laps))
    
    # Calculate total race time for each car
    total_times = lap_times.sum(axis=1)
    
    # Determine the winner (car with the minimum total race time)
    winner = np.argmin(total_times)
    
    # Check if the winner is the 7th car (index 6)
    if winner == 6:
        seventh_car_wins += 1

# Calculate the probability that the 7th car wins
probability_seventh_car_wins = seventh_car_wins / num_races

print(f"Daadaa :: The 7th car wins approximately {probability_seventh_car_wins:.4f} of the races.")
