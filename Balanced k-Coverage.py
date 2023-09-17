#Python implementation of the Balanced k-Coverage Algorithm:

import math
import random

# Function to calculate the distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to calculate the coverage of a sensor given its position and coverage radius
def calculate_coverage(sensor, sensors):
    coverage = set()
    for other_sensor in sensors:
        if distance(sensor['position'], other_sensor['position']) <= sensor['radius']:
            coverage.add(other_sensor['position'])
    return coverage

# Function to calculate the unbalancedness of coverage given a set of sensors
def calculate_unbalancedness(selected_sensors, sensors):
    max_coverage = 0
    min_coverage = float('inf')

    for sensor in selected_sensors:
        coverage = calculate_coverage(sensor, sensors)
        coverage_size = len(coverage)
        max_coverage = max(max_coverage, coverage_size)
        min_coverage = min(min_coverage, coverage_size)

    return max_coverage - min_coverage

# Balanced k-Coverage Algorithm
def balanced_k_coverage(sensors, k):
    selected_sensors = []
    remaining_sensors = sensors.copy()

    while len(selected_sensors) < k:
        max_unbalancedness = -1
        best_sensor = None

        for sensor in remaining_sensors:
            temp_selected_sensors = selected_sensors + [sensor]
            unbalancedness = calculate_unbalancedness(temp_selected_sensors, sensors)

            if unbalancedness > max_unbalancedness:
                max_unbalancedness = unbalancedness
                best_sensor = sensor

        if best_sensor is None:
            break

        selected_sensors.append(best_sensor)
        remaining_sensors.remove(best_sensor)

    return selected_sensors

# Example usage:
if __name__ == "__main__":
    # Define sensor nodes with their positions and coverage radii
    sensors = [
        {'position': (0, 0), 'radius': 1},
        {'position': (1, 1), 'radius': 1},
        {'position': (2, 0), 'radius': 1},
        {'position': (0, 2), 'radius': 1}
    ]

    k = 2  # Number of sensors to select
    selected_sensors = balanced_k_coverage(sensors, k)

    print("Selected sensors:")
    for sensor in selected_sensors:
        print(f"Sensor at {sensor['position']} with radius {sensor['radius']}")
