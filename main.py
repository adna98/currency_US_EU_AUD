exchange_to_usd = 1.874  # US dollar
exchange_to_euro = 1.955
exchange_to_aud = 1.275  # Australian dollar


def currency_choice():
    user_input = input("Pleas enter the currency that you want to exchange to BAM\n"
                       "It can be USD or EURO or AUD\n")
    user_input_number = input("Pleas enter the amount of money that you want to exchange to BAM\n")
    user_input_br = float(user_input_number)

    if user_input == "USD":
        print(f"For {user_input_br} USD you will get {user_input_br * exchange_to_usd} BAM")
    elif user_input == "EURO":
        print(f"For {user_input_br} EURO you will get {user_input_br * exchange_to_euro} BAM")
    elif user_input == "AUD":
        print(f"For {user_input_br} AUD you will get {user_input_br * exchange_to_aud} BAM")
    else:
        print("You enter the wrong currency,the currency can be USD EURO or AUD.\n"
              "Or you enter negative number, pleas enter just positive number.")


user_input = input("If you want close the program, enter exit\n")
while user_input != "exit":
    currency_choice()
    user_input = input("If you want close the program, enter exit\n")

