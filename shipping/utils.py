import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
# Nominatim's usage policy requires a descriptive User-Agent and max ~1 req/sec.
# For production traffic, switch to a paid provider (Mapbox, Google, LocationIQ)
# with your own API key.
GEOCODE_HEADERS = {"User-Agent": "RedCrossDeliveryApp/1.0 (contact@redcrossdelivery.org)"}


def geocode_address(address):
    """Return (latitude, longitude) as floats, or (None, None) if it can't be resolved."""
    if not address or not address.strip():
        return None, None
    try:
        response = requests.get(
            NOMINATIM_URL,
            params={"q": address, "format": "json", "limit": 1},
            headers=GEOCODE_HEADERS,
            timeout=5,
        )
        response.raise_for_status()
        results = response.json()
        if results:
            return float(results[0]["lat"]), float(results[0]["lon"])
    except (requests.RequestException, ValueError, KeyError, IndexError):
        pass
    return None, None