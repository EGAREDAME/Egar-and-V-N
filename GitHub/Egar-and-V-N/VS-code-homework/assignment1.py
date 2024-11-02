from datetime import datetime
"""
This method creates an interactable code in which it allow 
the user to input their name ad date of birth by subtacting 
it from today's date.
Args: date_today, birth_date: datetime needed for code
return: age
"""




def calculate_age(date_today, birth_date):
    days_in_year = 365.25
    age = (date_today - birth_date).days / days_in_year
    return age

,,,

if __name__ == "__main__":
    first_name=input("what is your first name? ")
    print(first_name)

    last_name=input("what is your last name ")
    print(last_name)

    birth_date_str=input("what is your birth date? (YYYY-MM-DD) ")

    date_today_str = input("what is the date today? (YYYY-MM-DD) ")

    birth_date = datetime.strptime(birth_date_str,'%Y-%m-%d')

    date_today = datetime.strptime(date_today_str,'%Y-%m-%d')

    current_age = calculate_age(date_today, birth_date)
    print("Your current age is", int(current_age))