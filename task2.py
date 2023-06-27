answer=input("Would you like to convert hours to minutes or minutes to hours? ")
if answer == "hours to minutes":
    hrs=input("How many hours would you like to convert?")
    min=int(hrs)*60
    print(min)
elif answer == "minutes to hours":
    min=input("How many minutes would you like to convert?")
    hrs=int(min)/60
    print(hrs)