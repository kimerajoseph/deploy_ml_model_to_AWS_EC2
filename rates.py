import copy

def rates_function(marital_status,income):
    #loan amount should be 50% of applicant's annual net income
    # Take a tax rate of 25% for income<58000 (unmarried) and 25% for income <115,000 (married)
    # 45%, income < 275000 and unmarried. 600k threshold for married applicants
    #int_list = list(map(int, new_list))
    #criteria 1 not married and income < 58k
    print(f"rate function called {income} {marital_status}")
    if marital_status != 2 and income < 58000:
        rate = 0.25
    
    # married and income < 115k
    elif marital_status == 2 and income < 115000:
        rate = 0.25

    # unmarried person earning between 58k and 275k
    elif marital_status != 2 and 58000 <= income <= 275000:
        rate = 0.45
    
    elif marital_status == 2 and 115000 <= income <= 600000:
        rate = 0.45

    # all other cases, use a flat rate of 30%
    else:
        rate = 0.3
    
    amount = rate * income
    return amount

def process_list(val):
# drop the name and decode phones and emails
    new_list = copy.deepcopy(val)
    new_list.pop(0)
    if new_list[10] != '':
        new_list[10]=1
    else:
        new_list[10]=0
    if new_list[11] != '':
        new_list[11]=1
    else:
        new_list[11]=0
    if new_list[12] != '':
        new_list[12]=1
    else:
        new_list[12]=0

    return new_list