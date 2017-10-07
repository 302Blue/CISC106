def gravity():
    Mass1 = float(input('Input first mass in kg'))
    Mass2 = float(input('Input second mass in kg'))
    Distance = float(input('How far apart are the two masses in meters?')
    F = (6.673e-11)*((Mass1*Mass2)/Distance**2)
    return F
