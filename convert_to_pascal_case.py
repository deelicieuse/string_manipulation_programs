# prompt for full name in improper casing a
full_name = input("Please enter your full name in improper casing: ")

# convert to title case and remove spaces
pascal_case_full_name = full_name.title().replace(" ","")

# print pascal case full name
print(pascal_case_full_name)