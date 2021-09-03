

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib.animation import FuncAnimation

import numpy as np






def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """

    sizes = [len(categories['Planets']), len(categories['Non-Planets'])]
    labels = ['Planets', 'Non-Planets']
    plt.pie(sizes, labels=labels)
    plt.legend(title = 'Entities by type')
    plt.show()


def entities_bar(categories):

    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    data = [len(categories['Low']), len(categories['Medium']), len(categories['High'])]

    plt.bar(['Low', 'Medium', 'High'], data)
    plt.title('Entities by gravity')
    plt.xlabel('Gravity type')
    plt.ylabel('Number of entities')
    plt.show()


def orbits(summary):

      """
        Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

        Summary is a nested dictionary of the form:
        summary = {
            "orbited planet": {
                "small": [entity, entity, entity],
                "large": [entity, entity]
            }
        }

        The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
        number of "small" and "large" orbiting entities.

        :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
        :return: Does not return anything
        """


    #plt.show()

    #data = [len(summary.values()) , len(summary.values())]
    #plt.bar(['small', 'large'], data)



def gravity_animation():

    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    #x = [len(categories['Low']), len(categories['Medium']), len(categories['High'])]
    #y = ['Low', 'Medium', 'High']
    #fig, ax = plt.subplots()
    #fig = plt.figure()
    #ax = plt.axes()

    #plt.show()

gravity_animation()

