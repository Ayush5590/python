def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273

def convert_temperature(celsius, scale):
    scale = scale.upper()
    if scale == 'F':
        return celsius_to_fahrenheit(celsius)
    elif scale == 'K':
        return celsius_to_kelvin(celsius)
    else:
        return None

try:
    temp_input = float(input("Enter temperature in Celsius: "))
    scale_input = input("Convert to Fahrenheit or Kelvin? (F/K): ").strip()

    result = convert_temperature(temp_input, scale_input)

    if result is None:
        print("Invalid scale entered. Please enter 'F' or 'K'.")
    else:
        print(f"{temp_input}°C is {result:.2f}°{scale_input.upper()}")

except ValueError:
    print("Invalid temperature entered. Please enter a numeric value.")