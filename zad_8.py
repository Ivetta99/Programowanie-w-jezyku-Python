from __future__ import annotations
from typing import List, Optional
import argparse
import requests


class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        city: str,
        country: str,
        website_url: Optional[str],
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


def get_breweries_from_api(city: Optional[str] = None) -> list:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params: dict[str, str | int] = {"per_page": 20}
    if city:
        params["by_city"] = city

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Pobieranie browarów z OpenBreweryDB")
    parser.add_argument(
        "--city",
        type=str,
        help="Nazwa miasta, z którego mają być pobierane browary (np. --city=Berlin)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    breweries_data = get_breweries_from_api(city=args.city)
    breweries = brewery_factory(breweries_data)

    if not breweries:
        if args.city:
            print(f"Brak browarów dla miasta: {args.city}")
        else:
            print("Brak danych z API.")
        return

    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
