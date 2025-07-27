""" simple_api_practice.py by Garrett Rohde
    07/25/2025
    Assignment 9.2
    practice using haveibeenpwned API
"""

import requests
import json
import sys


def jprint(obj):
    """ print json in pretty-formatting """
    text = json.dumps(obj, indent=4, sort_keys=True)
    print(text)


def get_breaches():
    """ gets all website breaches from the API """
    response = requests.get("https://haveibeenpwned.com/api/v3/breaches")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} | {response.reason}")
        return []


def main():
    breachs = get_breaches()

    # print without formatting
    print(breachs)

    print("\nType a year to search for website breaches, or type 'exit' to exit")

    while True:
        year = input("\nYear: ").strip()
        if year.lower() == "exit":
            sys.exit()
        elif not year.isdigit() or len(year) != 4:
            print("Year must be four digits and numerical")
            continue


        # filter the breaches by year
        filtered = [b for b in breachs if b.get("BreachDate").startswith(year)]

        if filtered:
            print(f"Found {len(filtered)} breaches for {year}")
            jprint(filtered)
        else:
            print(f"No breaches in this API for {year}")


if __name__ == "__main__":
    main()