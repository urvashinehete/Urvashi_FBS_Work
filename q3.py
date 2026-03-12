#input distance
feet = float(input("Enter distance in feet:"))
inches = float(input("Enter distance in inches:"))

#convert feet to inches
total_inches = (feet * 12) + inches

#convert inches to meters
meters = total_inches * 0.0254

#convert meters to centimeters 
centimeters = meters * 100

#display result
print("Distance in meters", meters)
print("Distance in centimeters =",centimeters)