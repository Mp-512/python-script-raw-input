def create_cast_list(filename):
    cast_list = []
    with open(filename) as file:
        for line in file:
            name = line.split(',')[0]
            cast_list.append(name)
    return cast_list

filename = 'flying_circus_cast.txt'
cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)