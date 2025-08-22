#Q3. Convert Feet & Inches to Meter & Centimeter
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

# 1 foot = 0.3048 m, 1 inch = 0.0254 m
# Convert to meters
meters = (feet * 0.3048) + (inches * 0.0254)

# Convert to centimeters
centimeters = meters * 100

print(f"Distance in meters: {meters}")
print(f"Distance in centimeters: {centimeters}")