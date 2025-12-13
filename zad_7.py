from typing import List
import requests


class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        city: str,
        country: str,
        website_url: str | None,
    ):
        self.brewery_id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        website = self.website_url or "no website"
        return (
            f"Brewery(id={self.brewery_id}, name={self.name}, "
            f"type={self.brewery_type}, city={self.city}, "
            f"country={self.country}, website={website})"
        )


def get_breweries_from_api() -> list:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def brewery_factory(breweries: list) -> List[Brewery]:
    result: List[Brewery] = []
    for b in breweries:
        brewery = Brewery(
            brewery_id=b["id"],
            name=b["name"],
            brewery_type=b["brewery_type"],
            city=b["city"],
            country=b["country"],
            website_url=b.get("website_url"),
        )
        result.append(brewery)
    return result


def main():
    breweries_data = get_breweries_from_api()
    breweries = brewery_factory(breweries_data)

    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
