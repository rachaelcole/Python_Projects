def calcWeeklyWages(totalHours, hourlyWage):
    if totalHours <= 40:
        totalWages = totalHours * hourlyWage
    else:
        overtime = totalHours - 40
        totalWages = (hourlyWage * 40) + ((1.5 * hourlyWage) * overtime)
    return totalWages


def main():
    hours = float(input('Enter hours worked: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calcWeeklyWages(hours, wage)
    print(f'Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.')


main()
