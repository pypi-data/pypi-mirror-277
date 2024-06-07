class Plane:
    def __init__(self, name, passengers, route):
        self.name = name
        self.passengers = passengers
        self.route = route

    @staticmethod
    def calculate_load(passengers):
        max_capacity = 200
        load_percentage = (passengers / max_capacity) * 100
        return load_percentage

    @staticmethod
    def same_route_planes(planes, route):
        same_route_planes = [plane.name for plane in planes if plane.route == route]
        return same_route_planes

    @staticmethod
    def average_load(planes):
        total_passengers = sum(plane.passengers for plane in planes)
        average_load = total_passengers / len(planes)
        return average_load

# Пример использования
plane1 = Plane("Boeing 747", 180, "New York - London")
plane2 = Plane("Airbus A380", 210, "Paris - Tokyo")
plane3 = Plane("Boeing 737", 150, "London - Dubai")

planes = [plane1, plane2, plane3]

print(f"Загрузка самолета {plane1.name}: {Plane.calculate_load(plane1.passengers)}%")
print(f"Самолеты, летящие по маршруту 'New York - London': {Plane.same_route_planes(planes, 'New York - London')}")
print(f"Средняя загрузка всех самолетов: {Plane.average_load(planes)} пассажиров")