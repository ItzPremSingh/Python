latitude = 28.630
longitude = 77.411

BASE_URL = "https://api.open-meteo.com/v1/"
API_URL = "forecast?"
URL_BASE_PARAMS = {"latitude": str(latitude), "longitude": str(longitude)}


def full_url(URL_PARAMS: dict[str, str | list[str] | tuple[str]]) -> str:
    PARAMS: list[str] = []

    for key, value in {**URL_BASE_PARAMS, **URL_PARAMS}.items():
        if isinstance(value, (list, tuple)):
            value = ",".join(value)

        PARAMS.append(f"{key}={value}")

    return BASE_URL + API_URL + "&".join(PARAMS)
