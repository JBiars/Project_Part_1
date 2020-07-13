# Prep work for adding the tests
# Create initial menu
language_menu = {
    1 : "Add A New Test",
    2 : "FAS",
    3 : "CFL",
    4 : "Semantic Fluency",
    5 : "Animals",
    6 : "Boston Naming"
}
max_item = 6

# Display existing menu for the user
print(language_menu)

# Prompt user to select a test (options 2 through end) or add a new test (option 1)
lang_selection = int(input("Enter Selection: "))
print(lang_selection)

# Add a new test to the menu
if lang_selection != 1:
    print(lang_selection, ":", language_menu[lang_selection])
else: 
    new_test = input("Enter Test: ")
    max_item += 1
    language_menu[max_item] = new_test
    print(language_menu)
   

# Create menu of score types
# Which score type a user initially selects will determine the calculations that will ultimately be run

scoretype_menu = {
    1 : "Standard Score",
    2 : "Scaled Score",
    3 : "T-Score",
    4 : "z-score"
}

print(scoretype_menu)

score_selection = int(input("Enter Selection: "))
print(score_selection, ":", scoretype_menu[score_selection])
  
