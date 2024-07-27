import numpy as np

def simulate_race_with_overtakes():
    num_cars = 10
    num_laps = 90
    mean_lap_time = 90  # mean lap time in seconds
    std_dev_lap_time = 0.8  # standard deviation of lap time in seconds
    overtake_penalty = 0.8  # penalty for being overtaken in seconds

    # Initialize arrays for lap times and total times
    lap_times = np.zeros((num_cars, num_laps))
    total_times = np.zeros(num_cars)
    
    # Generate initial lap times
    for car in range(num_cars):
        lap_times[car] = np.random.normal(mean_lap_time, std_dev_lap_time, num_laps)
    
    # Determine overtakes
    for lap in range(num_laps):
        # Sort lap times to determine relative positions
        sorted_indices = np.argsort(lap_times[:, lap])
        
        # Apply penalties for being overtaken
        for rank in range(num_cars):
            car = sorted_indices[rank]
            for ahead_rank in range(rank):
                ahead_car = sorted_indices[ahead_rank]
                # Apply penalty if the car is overtaken
                lap_times[car, lap] += overtake_penalty
    
    # Calculate total time for each car
    total_times = np.sum(lap_times, axis=1)
    
    return total_times

def run_simulation_with_overtakes(num_races=10000):
    num_cars = 10
    wins_by_7th_car = 0

    for _ in range(num_races):
        total_times = simulate_race_with_overtakes()
        # Car 7 is indexed as 6 (zero-based index)
        if np.argmin(total_times) == 6:
            wins_by_7th_car += 1

    # Calculate the winning percentage for the 7th car
    win_percentage = (wins_by_7th_car / num_races) * 100
    return win_percentage

if __name__ == "__main__":
    win_percentage = run_simulation_with_overtakes()
    print(f"The car that leaves 7th wins {win_percentage:.2f}% of the time.")
