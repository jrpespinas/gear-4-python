import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand: str, catalogue_price: int, electric: bool):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id: str, license_plate: str, info: VehicleInfo):
        self.id = id
        self.license_plate = license_plate
        self.info = info


class VehicleRegistry:
    vehicle_info = {}

    def __init__(self):
        self.create_vehicle_info("Tesla Model 3", True, 60000)
        self.create_vehicle_info("Volkswagen ID3", True, 35000)
        self.create_vehicle_info("BMW 5", False, 45000)

    def create_vehicle_info(self, brand: str, electric: bool, catalogue_price: int):
        self.vehicle_info[brand] = VehicleInfo(
            brand=brand, electric=electric, catalogue_price=catalogue_price
        )

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return (
            f"{id[:2]}"
            f"-{''.join(random.choices(string.digits, k=2))}"
            f"-{''.join(random.choices(string.ascii_uppercase, k=2))}"
        )

    def create_vehicle(self, brand) -> Vehicle:
        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(
            id=vehicle_id, license_plate=license_plate, info=self.vehicle_info[brand]
        )


class Application:
    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # create a vehicle
        vehicle = registry.create_vehicle(brand)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 68000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage [default 5% of the catalogue price, except for electric cars where it is 2%]
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle.id}")
        print(f"License plate: {vehicle.license_plate}")
        print(f"Payable tax: {payable_tax}")


app = Application()
app.register_vehicle("BMW 5")
