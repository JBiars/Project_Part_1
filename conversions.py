# wrapper for all conversions


# Conversions from one of these types: Standard Score, Scaled Score, T-score, z-score
# into another of them
def convert(from_score_type, to_score_type, score):
    ''' Converts a score value (number) from from_score_type (str) to to_score_type (str)
    and returns converted score value. Returns None on error.
    Valid types are "standard", "scaled", "t" and "z"
    '''

    v = score # incoming score value
    cv = None # result of the conversion

    # run through all possible combinations of score types
    if from_score_type == "standard":
        if   to_score_type == "scaled":
            pass #  change pass to the correct conversion math: cv = <some math with v>
        elif to_score_type == "t":
            pass #  change pass to the correct conversion math: cv = <some math with v>
        elif to_score_type == "z":
             pass #  change pass to the correct conversion math: cv = <some math with v>
        else:
            return None # Error!
    elif from_score_type == "scaled":
        if  to_score_type == "standard":
            pass
        # ETC

    print(f"{from_score_type}:{v} -> {to_score_type}:{cv}") # DEBUG - comment out after testing!

    return cv

# test the function
convert("standard", "scaled", 123)
# all other combinations