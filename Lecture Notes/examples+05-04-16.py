from cisc106_34 import assertEqual

def convert_F_to_C(fahrenheit):
    ''' This function converts temperature from °F to °C.
    Paameters:
        fahrenheit (number) - temperature in °F
    Returns:
        celsius (float)- temperature converted to °C
    '''
    # Convert from °F to °C
    celsius = ((fahrenheit - 32.0) * 5.0 / 9.0)
    return celsius

assertEqual(convert_F_to_C(212), 100)
assertEqual(convert_F_to_C(32), 0)
assertEqual(convert_F_to_C(-40), -40)
assertEqual(convert_F_to_C(176), 80)






















