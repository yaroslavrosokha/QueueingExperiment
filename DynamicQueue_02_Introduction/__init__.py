from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Introduction to Dynamic Queue Repeated Games Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'DynamicQueue_02_Introduction'
    min_payment = 5
    players_per_group = None
    duration = 60
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class welcome(Page):
    pass


page_sequence = [
    welcome,
]
