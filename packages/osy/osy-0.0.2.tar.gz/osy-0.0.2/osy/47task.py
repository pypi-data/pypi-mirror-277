""""Создать класс Профиль местности, который хранит последовательность
высот, вычисленных через равные промежутки по горизонтали. Методы:
наибольшая высота, наименьшая высота, перепад высот (наибольший,
суммарный), крутизна (тангенс угла наклона; наибольшая, средняя), сравнение
двух профилей одинаковой длины (по перепаду, по крутизне)."""
import math


class MapProfile:
    def __init__(self, list_h):
        self.heights = list_h

    def highest(self):
        return max(self.heights)

    def lowest(self):
        return min(self.heights)

    def max_drop(self):
        max_drop = 0
        for i in range(len(self.heights) - 1):
            for j in range(i + 1, len(self.heights)):
                drop = abs(self.heights[j] - self.heights[i])
                if drop > max_drop:
                    max_drop = drop
        return max_drop

    def total_drop(self):
        total = 0
        for i in range(len(self.heights) - 1):
            total += abs(self.heights[i] - self.heights[i + 1])
        return total

    def max_slope(self, horizontal_distance):
        max_slope = 0
        for i in range(len(self.heights) - 1):
            slope = abs(self.heights[i + 1] - self.heights[i]) / horizontal_distance
            if slope > max_slope:
                max_slope = slope
        return max_slope

    def average_slope(self, horizontal_distance):
        total_slope = 0
        for i in range(len(self.heights) - 1):
            total_slope += abs(self.heights[i + 1] - self.heights[i]) / horizontal_distance
        return total_slope / (len(self.heights) - 1)

    @staticmethod
    def compare_profiles(profile1, profile2, horizontal_distance):
        if len(profile1.heights) != len(profile2.heights):
            raise ValueError("Profiles must be of the same length")

        comparison = {
            "max_drop": profile1.max_drop() > profile2.max_drop(),
            "total_drop": profile1.total_drop() > profile2.total_drop(),
            "max_slope": profile1.max_slope(horizontal_distance) > profile2.max_slope(horizontal_distance),
            "average_slope": profile1.average_slope(horizontal_distance) > profile2.average_slope(horizontal_distance)
        }

        return comparison


# Пример использования:
profile1 = MapProfile([100, 200, 150, 300, 250])
profile2 = MapProfile([120, 180, 160, 280, 240])

print("Наибольшая высота профиля 1:", profile1.highest())
print("Наименьшая высота профиля 1:", profile1.lowest())
print("Наибольший перепад высот профиля 1:", profile1.max_drop())
print("Суммарный перепад высот профиля 1:", profile1.total_drop())
print("Наибольшая крутизна профиля 1:", profile1.max_slope(10))
print("Средняя крутизна профиля 1:", profile1.average_slope(10))

comparison = MapProfile.compare_profiles(profile1, profile2, 10)
print("Сравнение профилей (profile1 > profile2):", comparison)