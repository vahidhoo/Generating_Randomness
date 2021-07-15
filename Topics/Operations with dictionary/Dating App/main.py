def select_dates(potential_dates):
    names = ', '.join([d['name'] for d in potential_dates if d['age'] >= 30 and 'art' in d['hobbies'] and d['city'] == 'Berlin'])

    return names
