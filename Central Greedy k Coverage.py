import math

# Function to calculate the distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to calculate the utility of a sensor based on incentive values
def calculate_utility(sensor, incentive_values):
    utility = 0
    for i in range(len(sensor['coverage'])):
        utility += incentive_values[i] * sensor['coverage'][i]
    return utility

# Function to select k sensors using the Greedy Linear algorithm
def greedy_linear(sensors, k, incentive_values):
    selected_sensors = []

    while len(selected_sensors) < k:
        max_utility_sensor = None
        max_utility = -float('inf')

        for sensor in sensors:
            if sensor not in selected_sensors:
                utility = calculate_utility(sensor, incentive_values)
                if utility > max_utility:
                    max_utility = utility
                    max_utility_sensor = sensor

        if max_utility_sensor is not None:
            selected_sensors.append(max_utility_sensor)

    return selected_sensors

# Function to select k sensors using the Greedy Quadratic algorithm
def greedy_quadratic(sensors, k, incentive_values):
    selected_sensors = []

    while len(selected_sensors) < k:
        max_utility_sensor = None
        max_utility = -float('inf')

        for sensor in sensors:
            if sensor not in selected_sensors:
                utility = calculate_utility(sensor, incentive_values)
                if utility > max_utility:
                    max_utility = utility
                    max_utility_sensor = sensor

        if max_utility_sensor is not None:
            selected_sensors.append(max_utility_sensor)
            incentive_values = [incentive_values[i] / 2 for i in range(len(incentive_values))]

    return selected_sensors

# Example usage:
if __name__ == "__main__":
    # Define sensor nodes with their positions and coverage areas
    sensors = [
        {'position': (0, 0), 'coverage': [1, 0, 0, 0]},
        {'position': (1, 1), 'coverage': [0, 1, 0, 0]},
        {'position': (2, 0), 'coverage': [0, 0, 1, 0]},
        {'position': (0, 2), 'coverage': [0, 0, 0, 1]}
    ]

    k = 3  # Number of sensors to select

    incentive_values_linear = [1, 1, 1, 0]
    selected_sensors_linear = greedy_linear(sensors, k, incentive_values_linear)

    print("Greedy Linear selected sensors:")
    for sensor in selected_sensors_linear:
        print(f"Sensor at {sensor['position']}")

    incentive_values_quadratic = [5, 3, 1, 0]
    selected_sensors_quadratic = greedy_quadratic(sensors, k, incentive_values_quadratic)

    print("\nGreedy Quadratic selected sensors:")
    for sensor in selected_sensors_quadratic:
        print(f"Sensor at {sensor['position']}")


