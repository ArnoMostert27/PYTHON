# 8-14 Cars (*kwargs)

def make_car(manufacturer, model, **features):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    for key, value in features.items():
        car[key] = value

    return car

car = make_car("subaru", "outback", color="blue", tow_package=True)

print(car)