base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):


    def totaltrip():
        global total_trip
        total_trip+=1
        return total_trip

    total=totaltrip()
    price=base_rate+price_per_km*path
    return f'Price taxi {price}, total trip: {total}'

print(trip_price(235))
print(trip_price(48))
print(trip_price(23))