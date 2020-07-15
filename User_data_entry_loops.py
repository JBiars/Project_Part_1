# Framework for defining languages and assigning them a score type
# CH 7/13

language_menu = {
    1 : "Add A New Test",
    2 : "FAS",
    3 : "CFL",
    4 : "Semantic Fluency",
    5 : "Animals",
    6 : "Boston Naming"
}

scoretype_menu = {
    1 : "Standard Score",
    2 : "Scaled Score",
    3 : "T-Score",
    4 : "Z-score"
}


def define_langs(langs, score_types, lang_sctype_dict=None):
    ''' show initial languages (langs) dict to user, allow to add new test, assign a type to each existsing test or quit

        returns a dict which has all scoretypes for each entry in langs:
        lang_dict = {"FAS": "T-Score",
                    "CFL": "Standard Score"
                    ...
                    }


        NEW:
        {'CFL': {"Entered Type": "T-score",
                 "Standard Score":None,
                 "Scaled Score":None,
                 "T-Score":3,4
                 "Z-score":None
},
...
}
    '''
    max_item = len(langs)
    # If lang_sctype_dict was not given, start a new
    if lang_sctype_dict == None: 
        lang_sctype_dict = {}

    while True: # loop forever, use return to jump out of loop for the next step

        # Display existing menu for the user
        print("\nDefine Language Menu")
        print("Currently defined languages:", lang_sctype_dict)
        print(language_menu)
        

        # Prompt user to select a test (options 2 through end) or add a new test (option 1)
        lang_selection_str = input("Enter number for the language you want to assign a score type to (0 when you're finished): ")
        lang_selection = int(lang_selection_str)
        #print(lang_selection)

        if lang_selection == 0: # done
            return lang_sctype_dict

        elif lang_selection != 1: # Add a new test to the menu
            lang = language_menu[lang_selection]
            sctype = define_score_type(lang, score_types)
            lang_sctype_dict[lang] = sctype
        
        else:  # add new lang
            new_test = input("Enter Name of New Test: ")
            max_item += 1
            language_menu[max_item] = new_test
            #print(language_menu)
            
            lang = new_test
            sctype = define_score_type(lang, score_types)
            lang_sctype_dict[lang] = sctype
   
def define_score_type(lang, score_types):
    '''Have user select a score type (from score_types) for lang and return it (string)
    '''
    print(score_types)
    score_selection_str = input("Enter score type for " + lang + ": ")
    score_selection  = int(score_selection_str)
    sct = score_types[score_selection]
    return(sct)

#
# MAIN
#

# test define_score_type
#print(define_score_type("FAS", scoretype_menu))

# Make new dict
d = define_langs(language_menu, scoretype_menu)
print(d)

# save dict in pickle format as test.p
import pickle
pickle.dump(d, open( "test.p", "wb" ))

# read it back in and edit it
d_from_file = pickle.load(open( "test.p", "rb" ))
d = define_langs(language_menu, scoretype_menu, d_from_file)


{'CFL': {"Entered Type": "T-score",
         "Standard Score":None,
         "Scaled Score":None,
         "T-Score":3.4,
         "Z-score":None
        },
 ...
}