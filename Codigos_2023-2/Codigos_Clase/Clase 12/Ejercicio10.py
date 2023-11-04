def faren_a_celsius(faren):
    return 9/5 * (faren - 32)

def celsius_a_faren(celsius):
    return (9/5 * celsius) + 32


if __name__ == "__main__":
    faren = 32 
    print(f"{faren}°F a °C => {faren_a_celsius(faren)}°C")
    celsius = 0
    print(f" {celsius}°C a °F => {celsius_a_faren(celsius)}°F")
    