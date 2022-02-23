# API DATA MAPPING
# for key, value in data.items():
    # if isinstance(value, str):
    #     data[key] = value.lower()

gender_map = {'male':1,'female':0}
marital_status_map = {'civil marriage':1,'married':2,'single':3,'separated':4,'widow':5}
income_type_map = {'working':1,'commercial associate':2,'pensioner':3,'state servant':4,'student':5}
level_of_education = {'academic degree':1,'higher education':2,'secondary':3,'incomplete higher':4, 'lower secondary':5}          
occupation_map = {'security':1, 'sales':2, 'accountants':3, 'laborers':4,'managers':5, 'drivers':6, 'realty agents':17, 'it staff':18,
          'core staff':7, 'high skill tech staff':8,'cleaning staff':9, 'private service staff':10,'cooking staff':11,
          'semi-skilled laborers':12, 'medicine staff':13, 'secretaries':14,'waiters/barmen staff':15,'hR staff':16}
housing_type = {'apartment':1,'house':2,'with parents':4,'co-op apartment':5,'office apartment':6}           
property_map = {'yes':1,'no':0}

def decode_api_data(data):
    # convert all string values to lower case
    # data = dict((key,value.lower()) for key,value in data.items() if isinstance(value,str))
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.lower()
        else:
            data[key] = value


    if data['mobile'] != '':
        data['mobile'] = 1

    else:
        data['mobile'] = 0

    if data['work_phone'] != '':
        data['work_phone'] = 1

    else:
        data['work_phone'] = 0

    if data['email'] != '':
        data['email'] = 1
    
    else:
        data['email'] = 0

    return data

def decode_df_columns(new_data):
    # Maping categorical data to int categories
    new_data['gender'] = new_data['gender'].map(gender_map)
    new_data['marital_status'] = new_data['marital_status'].map(marital_status_map)
    new_data['income_type'] = new_data['income_type'].map(income_type_map)
    new_data['level_of_education'] = new_data['level_of_education'].map(level_of_education)
    new_data['occupation_type'] = new_data['occupation_type'].map(occupation_map)
    new_data['housing_type'] = new_data['housing_type'].map(housing_type)
    new_data['property_owner'] = new_data['property_owner'].map(property_map)

    return new_data