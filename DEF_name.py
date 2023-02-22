def get_full_name(first_name, last_name, middle_name=False):
    if middle_name==False:
        return f'{first_name} {last_name}'
    else:
        return f'{first_name} {middle_name} {last_name}'


f=get_full_name('Vasya', 'Pes')
print(f)