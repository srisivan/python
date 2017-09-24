# Earnings

Basic = 10000
DA = 3000
HRA = 4500
CA = 1500
WA = 1000



# Deductions

PF = (Basic + DA) - (8.33 * 100)    # On Basic + DA
FPF = (Basic + DA) - (3.67 * 100)      # On Basic + DA
Salary_advance = 2500
Tex_Loan = 3000

Total_Earnings = PF + FPF + HRA + CA + WA

Total_Deductions = PF + FPF + Salary_advance + Tex_Loan

total_salary = Total_Earnings - Total_Deductions

print("Total Earnings = %s " % Total_Earnings)
print("Total Deductions = %s " % Total_Deductions)
print("Final_salary = %s " % total_salary)
print("PF = %s " % PF)
print("FPF = %s" % FPF)

one_day_salary = (total_salary / 30) 
Second_salary = one_day_salary * 28

print("Salary for one day = %s" % one_day_salary)

print("Salary for 28 days = %s " % Second_salary)





