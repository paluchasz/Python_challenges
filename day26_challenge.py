day, month, year = 24, 12, 1898
due_day, due_month, due_year = 18, 9, 1898

fine = 0
if year == due_year:
    #if returned within the same year
    if month == due_month:

        if day == due_day:
            fine = 0

        elif day > due_day:
            days_late = int(day) - int(due_day)
            fine = 15 * days_late #If not on the same day then there is a fine

    elif month > due_month:
        months_late = int(month) - int(due_month)
        fine = 500 * months_late  #If not in the same month
elif year > due_year:
    fine = 10000
print(fine)
