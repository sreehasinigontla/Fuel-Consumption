
# Fuel Consumption and Route Comparison System

def get_positive_number(message):
    """Accept only positive numeric values."""
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a value greater than zero.")

        except ValueError:
            print("Invalid input! Enter a numeric value.")


def get_percentage(message):
    """Accept a valid reserve percentage."""
    while True:
        try:
            value = float(input(message))

            if 0 <= value <= 100:
                return value

            print("Enter a percentage between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter a number.")


def calculate_fuel(distance, mileage):
    """Calculate fuel required for the journey."""
    return distance / mileage


def compare_vehicles(distance, reserve_percentage, vehicles):

    results = []

    print("\n========== VEHICLE COMPARISON ==========")

    for vehicle in vehicles:

        name = vehicle["name"]
        mileage = vehicle["mileage"]
        price = vehicle["price"]
        tank_capacity = vehicle["tank_capacity"]

        # Calculate journey fuel
        fuel_required = calculate_fuel(
            distance, mileage
        )

        # Calculate reserve fuel
        reserve_fuel = (
            fuel_required * reserve_percentage / 100
        )

        # Total fuel needed including reserve
        total_fuel = fuel_required + reserve_fuel

        # Calculate journey cost
        journey_cost = fuel_required * price

        # Check vehicle feasibility
        feasible = total_fuel <= tank_capacity

        result = {
            "name": name,
            "mileage": mileage,
            "fuel": fuel_required,
            "reserve": reserve_fuel,
            "total_fuel": total_fuel,
            "cost": journey_cost,
            "feasible": feasible
        }

        results.append(result)

        print("\nVehicle:", name)
        print(f"Mileage: {mileage:.2f} km/l")
        print(f"Journey Fuel: {fuel_required:.2f} litres")
        print(f"Reserve Fuel: {reserve_fuel:.2f} litres")
        print(f"Total Fuel Needed: {total_fuel:.2f} litres")
        print(f"Tank Capacity: {tank_capacity:.2f} litres")
        print(f"Journey Cost: Rs. {journey_cost:.2f}")

        if feasible:
            print("Status: FEASIBLE")
        else:
            print("Status: NOT FEASIBLE")

    # Select feasible vehicles
    feasible_vehicles = [
        vehicle for vehicle in results
        if vehicle["feasible"]
    ]

    print("\n========== FINAL RESULT ==========")

    if feasible_vehicles:

        # Find lowest-cost feasible vehicle
        best_vehicle = min(
            feasible_vehicles,
            key=lambda vehicle: vehicle["cost"]
        )

        print("Lowest-Cost Feasible Vehicle:",
              best_vehicle["name"])

        print(f"Fuel Required: {best_vehicle['fuel']:.2f} litres")
        print(f"Journey Cost: Rs. {best_vehicle['cost']:.2f}")

    else:
        print("No vehicle is feasible for this journey.")
        print("Consider vehicles with larger tank capacity.")


def main():

    print("=" * 50)
    print(" FUEL CONSUMPTION AND ROUTE COMPARISON")
    print("=" * 50)

    # Input journey details
    distance = get_positive_number(
        "\nEnter journey distance (km): "
    )

    reserve_percentage = get_percentage(
        "Enter required fuel reserve (%): "
    )

    # Input number of vehicles
    while True:
        try:
            n = int(input("\nEnter number of vehicles: "))

            if n > 0:
                break

            print("Enter at least one vehicle.")

        except ValueError:
            print("Please enter a valid whole number.")

    vehicles = []

    # Collect vehicle information
    for i in range(n):

        print(f"\n--- Vehicle {i + 1} Details ---")

        while True:
            name = input("Enter vehicle name: ").strip()

            if name:
                break

            print("Vehicle name cannot be empty.")

        mileage = get_positive_number(
            "Enter mileage (km/l): "
        )

        price = get_positive_number(
            "Enter fuel price per litre (Rs.): "
        )

        tank_capacity = get_positive_number(
            "Enter fuel tank capacity (litres): "
        )

        vehicles.append({
            "name": name,
            "mileage": mileage,
            "price": price,
            "tank_capacity": tank_capacity
        })

    # Compare all vehicles
    compare_vehicles(
        distance,
        reserve_percentage,
        vehicles
    )


if __name__ == "__main__":
    main()
