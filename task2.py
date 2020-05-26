def make_country(country_name, capital):
    country = {
        'Name': country_name,
        'Capital': capital
    }
    return country


country = make_country('Austria', 'Vienna')

print(country.values())
