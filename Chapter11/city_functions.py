# 11-1 City Function

def city_country(city, country):
    return f"{city.title()}, {country.title()}"



# 11-2 City Function with Population

def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"