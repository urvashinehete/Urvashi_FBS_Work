# Input time from user 
hours = int(input("Enter hours:"))
minutes = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))

#Convert into total second
total_seconds = hours*3600 + minutes*60 + seconds

#output result
print("Total seconds =",total_seconds)