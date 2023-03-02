"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    
    """
    species = set()

    fil = open(filename)
    for line in fil:
        spec = line.rstrip().split("|")[1]
        species.add(spec)
        
    
    return species
       


    # TODO: replace this with your co


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villagers = []
    fil = open(filename)
    for line in fil:
        line = line.rstrip().split("|")
        species = line[1]
        names = line[0]
        if search_string == species or "All":
            villagers.append(names)
        
    # TODO: replace this with your code
 
    return villagers


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    villagers = []
    fitness =[]
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    # TODO: replace this with your code
    fil = open(filename)
    for line in fil:
        line = line.rstrip().split("|")
        hobby = line[3]
        if hobby == "Fitness":
            fitness.append(line[0])
        elif hobby == "Education":
            education.append(line[0])
        elif hobby == "Nature":
            nature.append(line[0])
        elif hobby == "Music":
            music.append(line[0])
        elif hobby == "Fashion":
            fashion.append(line[0])
        elif hobby == "Play":
            play.append(line[0])
    
    villagers = [sorted(fitness),sorted(education),sorted(nature),sorted(music),sorted(play),sorted(fashion)]
    
    return villagers


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    fil = open(filename)
    for line in fil:
        line = line.rstrip().split("|")
        all_data.append(line)
    data_tuple = tuple(all_data)
   
    
    return data_tuple


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    motto = []
    fil = open(filename)
    for line in fil:
        line = line.rstrip().split("|")
        if line[0] == villager_name:
            motto.append(line[-1])
        else:
            None
    return motto


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    name = []
    
    fil = open(filename)
    for line in fil:
        line = line.rstrip().split("|")
        if line[0] == villager_name:
            mood_name =line[2]
            break
    for line in fil:
        line = line.rstrip().split("|")   
        if line[2] == mood_name:
            name.append(line[0])  
        
    return name

print(find_likeminded_villagers("villagers.csv", "Antonio"))