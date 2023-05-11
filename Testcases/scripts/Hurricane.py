from .Storm import Storm


class Hurricane(Storm):
    def __init__(self, name, wind_speed):
        super().__init__(name, wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed >= 74:
            return "Category two"
        elif self.wind_speed >= 95:
            return "Category three"
        elif self.wind_speed >= 110:
            return "Category four"
        elif self.wind_speed >= 156:
            return "F5"
        return "Tropical Storm"


    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification == "Category two":
            return "Coastal regions are encouraged to evacuate"
        elif classification == "Category three":
            return "All coastal regions must evacuate"
        elif classification == "Category four":
            return "All coastal regions must evacuate, and inland residents should take shelter"
        elif classification == "F5":
            return "All residents must take shelter immediately"

        return "Take care and avoid travel if possible."
