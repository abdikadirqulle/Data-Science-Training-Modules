import numpy as np

# Simulation parameters
num_cars = 10
num_laps = 90
num_races = 10000
mean_lap_time = 90  # seconds
std_dev_lap_time = 0.8  # seconds
overtake_penalty = 0.8  # seconds
crash_probability = 0.001  # 0.1%

# Initialize a counter for the number of wins by the 7th car
seventh_car_wins = 0

# Run the simulation for num_races
for race in range(num_races):
    # Generate lap times for each car
    lap_times = np.random.normal(mean_lap_time, std_dev_lap_time, (num_cars, num_laps))
    
    # Initialize a boolean array to keep track of crashed cars
    crashed_cars = np.zeros(num_cars, dtype=bool)
    
    # Simulate the race lap by lap
    for lap in range(num_laps):
        # Sort cars by their cumulative time to simulate overtaking
        cumulative_times = lap_times[:, :lap+1].sum(axis=1)
        sorted_indices = np.argsort(cumulative_times)
        
        # Apply overtake penalties and check for crashes
        for i in range(1, num_cars):
            current_car = sorted_indices[i]
            
            # Skip if the car has already crashed
            if crashed_cars[current_car]:
                continue
            
            overtakes = i
            lap_times[current_car, lap] += overtakes * overtake_penalty
            
            # Check for crash
            if np.random.rand() < crash_probability * overtakes:
                crashed_cars[current_car] = True
    
    # Calculate total race time for each car that has not crashed
    total_times = np.where(crashed_cars, np.inf, lap_times.sum(axis=1))
    
    # Determine the winner (car with the minimum total race time)
    winner = np.argmin(total_times)
    
    # Check if the winner is the 7th car (index 6)
    if winner == 6:
        seventh_car_wins += 1

# Calculate the probability that the 7th car wins
probability_seventh_car_wins = seventh_car_wins / num_races

print(f"The 7th car wins approximately {probability_seventh_car_wins:.4f} of the races.")




import numpy as np

def simulate_race_with_overtakes_and_crashes():
    num_cars = 10
    num_laps = 90
    mean_lap_time = 90  # mean lap time in seconds
    std_dev_lap_time = 0.8  # standard deviation of lap time in seconds
    overtake_penalty = 0.8  # penalty for being overtaken in seconds
    crash_probability = 0.001  # probability of crashing when overtaken

    # Initialize arrays for lap times, total times, and crash status
    lap_times = np.zeros((num_cars, num_laps))
    total_times = np.zeros(num_cars)
    crashed = np.zeros(num_cars, dtype=bool)  # Array to keep track of crashes
    
    # Generate initial lap times
    for car in range(num_cars):
        lap_times[car] = np.random.normal(mean_lap_time, std_dev_lap_time, num_laps)
    
    # Determine overtakes and crashes
    for lap in range(num_laps):
        if np.any(crashed):  # Skip processing for cars that have crashed
            continue

        # Sort lap times to determine relative positions
        sorted_indices = np.argsort(lap_times[:, lap])
        
        # Apply penalties and check for crashes
        for rank in range(num_cars):
            car = sorted_indices[rank]
            if crashed[car]:
                continue
            for ahead_rank in range(rank):
                ahead_car = sorted_indices[ahead_rank]
                # Apply penalty if the car is overtaken
                lap_times[car, lap] += overtake_penalty
                # Check if the car crashes
                if np.random.rand() < crash_probability:
                    crashed[car] = True
                    lap_times[car, lap:] = np.nan  # Mark remaining laps as invalid
    
    # Calculate total time for each car (excluding crashed cars)
    total_times[~crashed] = np.nansum(lap_times[~crashed], axis=1)
    
    return total_times

def run_simulation_with_overtakes_and_crashes(num_races=10000):
    num_cars = 10
    wins_by_7th_car = 0

    for _ in range(num_races):
        total_times = simulate_race_with_overtakes_and_crashes()
        # Check if car 7 (index 6) is still in the race and wins
        if np.argmin(total_times) == 6 and not np.isnan(total_times[6]):
            wins_by_7th_car += 1

    # Calculate the winning percentage for the 7th car
    win_percentage = (wins_by_7th_car / num_races) * 100
    return win_percentage

if __name__ == "__main__":
    win_percentage = run_simulation_with_overtakes_and_crashes()
    print(f"The car that leaves 7th wins {win_percentage:.2f}% of the time.")
