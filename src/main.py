from planet_data import mars, earth, ancient_mars
from scoring import habitability_score
from simulation import migration_analysis
from visualization import plot_scores, plot_factor_comparison

def get_user_inputs():
    print("=== CUSTOMIZE ANCIENT MARS CONDITIONS ===")

    temp = float(input("Enter temperature (°C): "))
    oxygen = float(input("Enter oxygen (%): "))
    water = float(input("Enter water availability (0-1): "))
    magnetic_field = float(input("Enter magnetic field strength (0-1): "))
    
    custom_mars = {
        "name" : "Custom Mars",
        "temperature" : temp,
        "oxygen" : oxygen,
        "co2" : 80,
        "gravity" : 3.7,
        "water" : water,
        "magnetic_field" : magnetic_field
    }

    return custom_mars

choice = input("Enter choice (1 or 2): ")
if choice == "2":
    mars_data = get_user_inputs()
else:
    mars_data = ancient_mars

def safe_input(prompt, min_val, max_val):
    value = float(input(prompt))
    if value < min_val or value > max_val:
        print("Invalid range, using default value")
        return (min_val + max_val) / 2
    return value


mars_score, mars_details = habitability_score(mars)
earth_score, earth_details = habitability_score(earth)

print("=== PRINT SIMULATION RESULT ===\n")
print(f"{mars_data['name']} Score: {mars_score}/10")
print("Mars Details:", mars_details,"\n")

print(f"Earh Score: {earth_score}/10")
print("Earth Details: ", earth_details, "\n")

print("=== HYPOTHESIS RESULT ===")
print(migration_analysis(mars_score, earth_score))

plot_scores(mars_score, earth_score, mars_data["name"])
plot_factor_comparison(mars_details, earth_details, mars_data["name"])
