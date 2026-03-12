#Input basic salary
basic = float(input("Enter basic salary:"))

#calculate allowances
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

#calculate total salary
total_salary = basic + da + ta + hra

#Display result
print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)