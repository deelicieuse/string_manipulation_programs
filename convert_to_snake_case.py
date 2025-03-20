# prompt for full name in incorrect casing
full_name = input("Please enter your full name in improper casing: ")

# convert to lowercase and replace spaces with "_"
snake_case_full_name = full_name.lower(),replace(" ", "_")

# print snake case full name