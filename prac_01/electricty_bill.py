
#Constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


print("Electricity bill calculator")
# price_rate = int(input("Enter price rate (c per kWh): "))
tariff_choice = int(input("Which tariff? 11 or 31: "))
daily_use = int(input("Enter daily use (kWh): "))
num_days = int(input("Enter the number of billing days in the billing period: "))

if tariff_choice == 11:
    estimated_bill = TARIFF_11 * daily_use * num_days / 100
    print(f"Estimated bill: ${estimated_bill:.2f}")
elif tariff_choice == 31:
    estimated_bill = TARIFF_31 * daily_use * num_days / 100
    print(f"Estimated bill: ${estimated_bill:.2f}")
else:
    print("Invalid tariff selection")

#estimated_bill = price_rate*daily_use*num_days/100
