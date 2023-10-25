question = input("Would you like to convert dollars to euros? (Y/N): ")
while question == "Y":
    dollar = float(input("Enter dollar amount to be converted: $"))
    euros = dollar * 0.94540
    print("Euros = $" + str(euros))
    question = input("Would you like to convert dollars to euros? (Y/N): ")
    if question == "N":
        break