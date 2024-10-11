# from json import load

# with open("data.json") as f:
#     data = load(f)

# current_units: dict[str, str] = data["current_units"]
# current: dict[str, str] = data["current"]

# for key, value in current.items():
#     print(f"{key}: {value} {current_units[key]}")


def degree_to_word(degrees) -> tuple[str, str]:
    # Define direction words for each 45-degree sector
    directions = {
        0: "North",
        45: "Northeast",
        90: "East",
        135: "Southeast",
        180: "South",
        225: "Southwest",
        270: "West",
        315: "Northwest",
        360: "North",  # Handle wrap-around
    }

    # Check if the given degrees are within range
    if degrees < 0 or degrees > 360:
        raise Exception

    # Calculate the nearest 45-degree sector
    sector = round(degrees / 45) * 45

    # Calculate the opposite direction
    opposite_sector = (sector + 180) % 360

    # Return both directions
    return directions[sector], directions[opposite_sector]


# Test the function
degrees =664545
coming_direction, going_direction = degree_to_word(degrees)
print("Wind direction (coming):", coming_direction)
print("Wind direction (going):", going_direction)