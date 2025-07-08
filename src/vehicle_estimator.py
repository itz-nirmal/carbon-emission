# Vehicle-wise Carbon Footprint Estimator

class VehicleEstimator:
    
    def __init__(self, vehicle_type, fuel_type, engine_size, fuel_economy, distance_traveled, vehicle_age):
        self.vehicle_type = vehicle_type
        self.fuel_type = fuel_type
        self.engine_size = engine_size
        self.fuel_economy = fuel_economy
        self.distance_traveled = distance_traveled
        self.vehicle_age = vehicle_age
        self.emission_factors = {
            'Petrol': 2.31,
            'Diesel': 2.68,
            'CNG': 2.75,
            'Electric': 0.0,
            'Hybrid': 1.5
        }
        self.age_factor = 1 + (self.vehicle_age * 0.01)

    def calculate_lifetime_emissions(self):
        if self.fuel_type in self.emission_factors:
            co2_emissions = (
                self.distance_traveled / self.fuel_economy *
                self.emission_factors[self.fuel_type] *
                self.age_factor
            )
            return co2_emissions
        return None

    def calculate_next_trip_emissions(self, distance_to_travel, fuel_available):
        if self.fuel_type in self.emission_factors and distance_to_travel > 0:
            co2_emissions = (
                distance_to_travel / self.fuel_economy *
                self.emission_factors[self.fuel_type] *
                self.age_factor
            )
            return co2_emissions
        return None

# Example usage
if __name__ == '__main__':
    ve = VehicleEstimator('Car', 'Petrol', 1500, 15, 50000, 5)
    lifetime_emissions = ve.calculate_lifetime_emissions()
    next_trip_emissions = ve.calculate_next_trip_emissions(100, 10)
    print(f'Lifetime Emissions: {lifetime_emissions} kg CO2')
    print(f'Next Trip Emissions: {next_trip_emissions} kg CO2')
