import math

# Function to calculate the distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to find the sensor with maximum uncovered area
def find_max_uncovered_sensor(sensors, covered_area):
    max_uncovered_sensor = None
    max_uncovered_area = 0

    for sensor in sensors:
        uncovered_area = 0
        for point in sensor['coverage']:
            if point not in covered_area:
                uncovered_area += 1
        if uncovered_area > max_uncovered_area:
            max_uncovered_area = uncovered_area
            max_uncovered_sensor = sensor

    return max_uncovered_sensor

# Central Greedy k-Coverage Algorithm
def central_greedy_k_coverage(sensors, k):
    selected_sensors = []
    covered_area = set()

    while len(selected_sensors) < k:
        max_uncovered_sensor = find_max_uncovered_sensor(sensors, covered_area)
        if max_uncovered_sensor is None:
            break
        selected_sensors.append(max_uncovered_sensor)
        for point in max_uncovered_sensor['coverage']:
            covered_area.add(point)

    return selected_sensors

# Example usage:
if __name__ == "__main__":
    # Define sensor nodes with their positions and coverage areas
    sensors = [
        {'position': (0, 0), 'coverage': [(0, 0), (1, 0), (0, 1)]},
        {'position': (1, 1), 'coverage': [(1, 1), (2, 1), (1, 2)]},
        {'position': (2, 0), 'coverage': [(2, 0), (3, 0), (2, 1)]},
        {'position': (0, 2), 'coverage': [(0, 2), (1, 2), (0, 3)]}
    ]

    k = 2  # Number of sensors to select
    selected_sensors = central_greedy_k_coverage(sensors, k)

    print("Selected sensors:")
    for sensor in selected_sensors:
        print(f"Sensor at {sensor['position']}")

