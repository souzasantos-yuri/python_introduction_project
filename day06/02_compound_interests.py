# %%

def compound_interests(amount, interest, years):
    '''Calculate the financial return due to a given amount through years and a given interest rate.
    
    amount:
        integer number that represents the value you want to enter

    interest:
        a float number between 0 and 1 that represets the interest rate

    years:
        a integer number >= 1 that represents the time of investment

    '''
    return amount * (1 + interest) ** years

# %%

compound_interests(interest=0.13, years=4, amount=1000)

# %%

value = compound_interests(interest=0.13, years=5, amount=1000)