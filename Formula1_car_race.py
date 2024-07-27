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
print(+f"Scenario 1: Car starting 7th wins {car_7_wins} times out of {num_races} races.")

# Simulation with overtakes but no crashes
def simulate_race_with_overtakes():
    lap_times = np.random.normal(mean_lap_time, std_dev_lap_time, (num_cars, num_laps))
    for i in range(num_cars):
        lap_times[i] += i

    for lap in range(num_laps):
        lap_order = np.argsort(lap_times[:, lap])
        for pos in range(1, num_cars):
            overtaken_car = lap_order[pos - 1]
            lap_times[overtaken_car, lap] += 0.8

    total_times = lap_times.sum(axis=1)
    winner = np.argmin(total_times)
    return winner

winners_with_overtakes = [simulate_race_with_overtakes() for _ in range(num_races)]
car_7_wins_with_overtakes = winners_with_overtakes.count(6)
print(f"Scenario 2: Car starting 7th wins {car_7_wins_with_overtakes} times out of {num_races} races.")

# Simulation with overtakes and crashes
def simulate_race_with_overtakes_and_crashes():
    lap_times = np.random.normal(mean_lap_time, std_dev_lap_time, (num_cars, num_laps))
    for i in range(num_cars):
        lap_times[i] += i

    for lap in range(num_laps):
        lap_order = np.argsort(lap_times[:, lap])
        for pos in range(1, num_cars):
            overtaken_car = lap_order[pos - 1]
            lap_times[overtaken_car, lap] += 0.8
            if np.random.rand() < 0.001:
                lap_times[overtaken_car, lap:] = np.inf

    total_times = lap_times.sum(axis=1)
    winner = np.argmin(total_times)
    return winner

winners_with_overtakes_and_crashes = [simulate_race_with_overtakes_and_crashes() for _ in range(num_races)]
car_7_wins_with_overtakes_and_crashes = winners_with_overtakes_and_crashes.count(6)
print(f"Scenario 3: Car starting 7th wins {car_7_wins_with_overtakes_and_crashes} times out of {num_races} races.")
