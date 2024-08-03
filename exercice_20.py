def infect():
    infected = 1
    days = 1

    while infected < 20000:
        a = infected + infected * 2
        if a >= 20000:
            break
        infected = a
        days = days + 1
    
    return infected, days

print(infect())