def gender(x):
    x['gender'] = 'genderless'
    if x['index_group_name'] in ['Ladieswear', 'Divided']:
        x['gender'] = 'female'
    if x['index_group_name'] == 'Menswear':
        x['gender'] = 'male'
    if x['index_group_name'] in ['Baby/Children', 'Sport']:
        if 'boy' in x['department_name'].lower() or 'men' in x['department_name'].lower():
            x['gender'] = 'male'
        if 'girl' in x['department_name'].lower() or 'ladies' in x['department_name'].lower():
            x['gender'] = 'female'
    if x['section_name'] == 'Mama':
        x['gender'] = 'pregnant'

    return x
