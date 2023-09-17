import math

class Sensor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.covered = False

def distance(sensor1, sensor2):
    return math.sqrt((sensor1.x - sensor2.x) ** 2 + (sensor1.y - sensor2.y) ** 2)

def central_greedy_k_coverage(sensors, k):
    selected_sensors = []
    
    while k > 0:
        best_sensor = None
        best_coverage = 0
        
        for sensor in sensors:
            if not sensor.covered:
                coverage = 0
                for other_sensor in sensors:
                    if not other_sensor.covered and distance(sensor, other_sensor) <= sensor.radius:
                        coverage += 1
                if coverage > best_coverage:
                    best_coverage = coverage
                    best_sensor = sensor
        
        if best_sensor is not None:
            best_sensor.covered = True
            selected_sensors.append(best_sensor)
            k -= 1
        else:
            break
    
    return selected_sensors

# Example usage
if __name__ == "__main__":
    sensors = [
        Sensor(0, 0, 5),
        Sensor(1, 1, 4),
        Sensor(2, 2, 3),
        Sensor(3, 3, 2),
        Sensor(4, 4, 1)
    ]
    
    k = 3
    selected_sensors = central_greedy_k_coverage(sensors, k)
    
    print("Selected Sensors:")
    for sensor in selected_sensors:
        print(f"Sensor at ({sensor.x}, {sensor.y}) with radius {sensor.radius}")
