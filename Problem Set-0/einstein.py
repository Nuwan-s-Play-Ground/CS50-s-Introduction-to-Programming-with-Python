def calculate_energy_equivalence(mass_kg):
    # Speed of light in meters per second
    speed_of_light = 300000000

    # Energy-mass equivalence formula: E = mc^2
    energy_joules = mass_kg * speed_of_light ** 2

    return energy_joules

def main():
    # Prompt the user for mass as an integer (in kilograms)
    mass_input_str = input("Enter mass (in kilograms): ")

    # Convert the input to an integer
    mass_kg = int(mass_input_str)

    # Calculate the equivalent energy in Joules
    energy_joules = calculate_energy_equivalence(mass_kg)

    # Output the result
    print(f"The equivalent energy for a mass of {mass_kg} kg is {energy_joules} Joules.")

if __name__ == "__main__":
    main()
