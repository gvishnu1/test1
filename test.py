print('hi')
import datetime


def tell_date():
    today = datetime.date.today()
    print(f"Today's date is {today}")


if __name__ == "__main__":
    user_input = input("Ask me anything: ")
    if "date" in user_input.lower():
        tell_date()