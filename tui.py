def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    print('------------------------------Solar Record Management System------------------------------')



def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection

    """
    # TODO: Your code here
    print('1. Load Data')
    print('2. Process Data')
    print('3. Visualise Data')
    print('4. Save Data')
    print('5. Exit')
    print()
    option = input('Please enter the number corresponding to your selection: ')
    if (option == '1'):
        return 1
    elif (option ==  '2'):
        return 2
    elif (option == '3'):
        return 3
    elif (option ==  '4'):
        return 4
    elif (option ==  '5'):
        return 5
    else:
        return None






def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f'{operation} has started.')





def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f'{operation} has completed.')




def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f'Error!  {error_msg}')


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here

    file_path = input('Please enter the file path of your data file: ')
    print()
    if ".csv" in file_path[-4:]: # if the last 4 characters of file path is ending in .csv will return the path
        return file_path
    else:
        print('Unsupported file extension, the file path is not ending in .csv')
        return None




def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print('How the data should be processed?  ')
    print()
    print('1. Retrieve entity')
    print('2. Retrieve entity details')
    print('3. Categorise entities by type')
    print('4. Categorise entities by gravity')
    print('5. Summarise entities by orbit')

    option = input('Please enter the number corresponding to your selection: ')
    if (option == '1'):
        return 1
    elif (option == '2'):
        return 2
    elif (option == '3'):
        return 3
    elif (option == '4'):
        return 4
    elif (option == '5'):
        return 5
    else:
        print('Invalid option')
        return None


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # TODO: Your code here
    name = input('Please enter the name of an entity: ')
    return name



def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # TODO: Your code here

    entity_name = input('Please enter the name of an entity: ')#asking user to enter name of entity
    index_list = [int(item) for item in input('Please enter the list of integer column indexes separated by comma: ').split(',')]#first I made sure the inputted indexes are converted into integers after used split() method to return a list of integers with the separator declared as ','
    final_list = [entity_name , index_list] #creating a new list containing name of entity and list of indexes
    return final_list #displaying the new list on the screen




def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here
    entity1 = []
    if cols == []:                    #if cols is empty list will display all entity values
        print(entity)
    else:
        for i in cols:                #I used for loop to iterate into list cols  ' into entity1 list
            entity1.append(entity[i]) #used append() method to add each element from entity list coresponding to index position 'i
        print(entity1)





def list_entities(entities,cols = []):
    """"
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    entity1 = []
    if cols == []:
        print(entities)
    else:
        for i in range(len(entities)): # I used nested for loop: i will iterate through (0 until lengh of entities)
            for i1 in cols:            # i1 will iterate into cols
                entity1.append(entities[i][i1])
        print(entity1)




def list_categories(categories = {}):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here
    print(categories)


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # TODO: Your code here
    lower_and_upper_limits = (float(input('Please enter the gravity lower limit: ')), float(input('Please enter the gravity upper limit: ')))
    return lower_and_upper_limits




def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here
    entity_names = input('Please enter the list of entity names separated by commas: ').split(',') #split() method splits a string into a list, separator specified is ','
    return entity_names






def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print('How the data should be visualised? ')
    print()
    print('1. Entities by type')
    print('2. Entities by gravity')
    print('3. Summary of orbits')
    print('4. Animate gravities')
    print()
    # Asking the user to input his selection
    option = input('Please enter the number corresponding to your selection:  ')
    if (option == '1'):
        return 1
    elif (option == '2'):
        return 2
    elif (option == '3'):
        return 3
    elif (option == '4'):
        return 4
    else:
        print('Invalid option')
        return None


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print('How the data should be saved? ')
    print()
    print('1. Export as JSON')
    print()
    option = input('Please enter the number corresponding to your selection: ')
    if (option == '1'):
        return 1
    else:
        print('Invalid selection')
        return None
