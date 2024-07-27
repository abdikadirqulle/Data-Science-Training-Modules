import numpy as np

# Constants
num_cars = 10
num_laps = 90
mean_lap_time = 90  # seconds
std_dev_lap_time = 0.8  # seconds
num_races = 10000

# Simulation without overtakes and crashes
def simulate_race():
    lap_times = np.random.normal(mean_lap_time, std_dev_lap_time, (num_cars, num_laps))
    for i in range(num_cars):
        lap_times[i] += i
    total_times = lap_times.sum(axis=1)
    winner = np.argmin(total_times)
    return winner

winners = [simulate_race() for _ in range(num_races)]
car_7_wins = winners.count(6)
print(f"Scenario 1: Car starting 7th wins {car_7_wins} times out of {num_races} races.")
