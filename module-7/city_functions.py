""" city_functions.py by Garrett Rohde
    07/13/2025
    Assignment 7.2
    Function to test with unit cases
"""

def city_country(city, country, population=None, language=None):
    output = f"{city.title()}, {country.title()}"

    if population:
        output += f" - population: {int(population)}"

    if language:
        output += f", language: {language.title()}"

    return output


def main():
    print(city_country("milan", "italy"))
    print(city_country("london", "england", 8950000))
    print(city_country("paris", "france", 2005000, "french"))


if __name__ == '__main__':
    main()