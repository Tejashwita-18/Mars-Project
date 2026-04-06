def habitability_score(planet):
    score = 0
    details = {}

    # temperature
    if -20 <= planet["temperature"] <= 50:
        score += 2
        details["temperature"] = "suitable"
    else:
        details["temperature"] = "harsh"

    # oxygen
    if planet["oxygen"] > 10:
        score += 2
        details["oxygen"] = "sufficient"
    else:
        details["oxygen"] = "low"

    # co2
    if 0.01 <= planet["co2"] <= 1:
        score += 2
        details["co2"] = "balanced"
    else:
        details["co2"] = "too high/low"

    # water
    if planet["water"] > 0.5:
        score += 2
        details["water"] = "available"
    else:
        details["water"] = "scarce"

    # magnetic field
    if planet["magnetic_field"] > 0.5:
        score += 2
        details["magnetic_field"] = "protective"
    else:
        details["magnetic_field"] = "weak"

    # gravity
    if 5 <= planet["gravity"] <= 15:
        score += 2
        details["gravity"] = "stable"
    else:
        details["gravity"] = "low/high"

    return score, details


