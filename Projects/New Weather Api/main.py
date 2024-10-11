from urllib.request import urlopen

from setting import full_url

# def time_formatter(datetime_obj: datetime) -> str:
#     return f"{datetime_obj.day} {datetime_obj.hour}h"


# with open("data.json") as f:
#     data = load(f)

# for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]):
#     print(time_formatter(datetime.fromisoformat(time)), temp)


with urlopen(
    full_url(
        {
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m",
            "timezone": "auto",
        }
    )
) as r:
    print(r.read().decode())
