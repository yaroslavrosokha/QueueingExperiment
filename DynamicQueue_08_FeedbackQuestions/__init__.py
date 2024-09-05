import numpy as np
from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Post-experimental Questionnaire.
"""


class Constants(BaseConstants):
    name_in_url = 'DynamicQueue_08_FeedbackQuestions'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    # Questionnaire
    understandingSelect = models.StringField(
        choices=['Clear', 'Somewhat Clear', 'Somewhat Confusing', 'Confusing'],
        verbose_name='Clarity of Instructions:',
        blank=True,
        widget=widgets.RadioSelectHorizontal,
    )
    explainedText = models.StringField(
        verbose_name='What could have been explained better?',
        blank=True,
    )
    strategy1Text = models.StringField(
        verbose_name='What was your strategy during the experiment? (Please be specific)',
        blank=True,
    )
    strategy2Text = models.StringField(
        verbose_name='Did your decision in a round depend on what happened in the previous rounds? If so, in what way? (Please be specific)',
        blank=True,
    )
    strategy3Text = models.StringField(
        verbose_name='Was your strategy different between the initial matches and the later matches of the experiment? If so, in what way? (Please be specific)',
        blank=True,
    )


# FUNCTIONS
# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
        'understandingSelect',
        'explainedText',
        'strategy1Text',
        'strategy2Text',
        'strategy3Text',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [Questionnaire]
