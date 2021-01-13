class Tesla:
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__model = model
        self.__color = color
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__autopilot = autopilot
        self.__efficiency = efficiency

    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def color(self) -> str:
        return self.__color

    @property
    def seats_count(self) -> int:
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, count: int):
        if count < 2:
            print("Number of seats cannot be lower than 2!")
        else:
            self.__seats_count = count

    def autopilot(self, obstacle: str) -> str:
        if self.__autopilot:
            return f"Tesla {self.__model} avoids {obstacle}"
        return "Autopilot is not available"

    def lock(self):
        self._is_locked = True

    def unlock(self):
        self._is_locked = False

    def open_doors(self) -> str:
        if self.__is_locked == False:
            return "Doors opens sideways"
        return "Car is locked!"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float) -> str:
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge -= battery_discharge_percent
        else:
            print("Battery charge level is too low!")
            return self.check_battery_level()


class ModelX(Tesla):
    def __init__(self, color: str, autopilot: bool = False):
        super().__init__("Model3", color, autopilot, 0.125)

    def open_doors(self):
        if self._is_locked == False:
            return "Doors opens towards roof"
        return "Car is locked!"

    def welcome(self) -> str:
        return "Hello from ModelX!"


tesla = Tesla("S", "red")
tesla.drive(100)

