import numpy as np

def simulate_race():
    num_cars = 10
    num_laps = 90
    mean_lap_time = 90  # mean lap time in seconds
    std_dev_lap_time = 0.8  # standard deviation of lap time in seconds

    # Initialize an array to store total time for each car
    total_times = np.zeros(num_cars)

    for car in range(num_cars):
        # Generate lap times for the current car
        lap_times = np.random.normal(mean_lap_time, std_dev_lap_time, num_laps)
        # Calculate total time for this car
        total_times[car] = np.sum(lap_times)

    return total_times

def run_simulation(num_races=10000):
    num_cars = 10
    wins_by_7th_car = 0

    for _ in range(num_races):
        total_times = simulate_race()
        # Car 7 is indexed as 6 (zero-based index)
        if np.argmin(total_times) == 6:
            wins_by_7th_car += 1

    # Calculate the winning percentage for the 7th car
    win_percentage = (wins_by_7th_car / num_races) * 100
    return win_percentage

if __name__ == "__main__":
    win_percentage = run_simulation()
    print(f"The car that leaves 7th wins {win_percentage:.2f}% of the time.")
