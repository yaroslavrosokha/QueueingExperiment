import copy as cp

import numpy as np
from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
A quiz app for dynamic queue repeated games experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'DynamicQueue_04_Quiz'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quizHistory1 = models.StringField()
    quizHistory2 = models.StringField()
    quizHistory3 = models.StringField()
    quizHistory4 = models.StringField()
    quizHistory5 = models.StringField()
    quizHistory6 = models.StringField()
    quizHistory7 = models.StringField()
    quizHistory8 = models.StringField()
    quizHistory9 = models.StringField()
    quizHistory10 = models.StringField()


# FUNCTIONS
# PAGES
class beginQuiz(Page):
    pass


class Question1(Page):
    form_model = 'player'
    form_fields = ['quizHistory1']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': "",
            'roundHistory': "",
            'tableRandomNumberHistory': "",
            'tableNumberHistory': "",
            'myChoiceHistory': "",
            'otherChoiceHistory': "",
            'myPayoffHistory': "",
            'otherPayoffHistory': "",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question2(Page):
    form_model = 'player'
    form_fields = ['quizHistory2']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': "",
            'roundHistory': "",
            'tableRandomNumberHistory': "",
            'tableNumberHistory': "",
            'myChoiceHistory': "",
            'otherChoiceHistory': "",
            'myPayoffHistory': "",
            'otherPayoffHistory': "",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question3(Page):
    form_model = 'player'
    form_fields = ['quizHistory3']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': ",2",
            'roundHistory': ",1",
            'tableRandomNumberHistory': ",3",
            'tableNumberHistory': ",3",
            'myChoiceHistory': ",1",
            'otherChoiceHistory': ",0",
            'myPayoffHistory': ",28",
            'otherPayoffHistory': ",68",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question4(Page):
    form_model = 'player'
    form_fields = ['quizHistory4']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': ",2",
            'roundHistory': ",1",
            'tableRandomNumberHistory': ",3",
            'tableNumberHistory': ",3",
            'myChoiceHistory': ",1",
            'otherChoiceHistory': ",0",
            'myPayoffHistory': ",28",
            'otherPayoffHistory': ",68",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question5(Page):
    form_model = 'player'
    form_fields = ['quizHistory5']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': ",2",
            'roundHistory': ",1",
            'tableRandomNumberHistory': ",3",
            'tableNumberHistory': ",3",
            'myChoiceHistory': ",1",
            'otherChoiceHistory': ",0",
            'myPayoffHistory': ",28",
            'otherPayoffHistory': ",68",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question6(Page):
    form_model = 'player'
    form_fields = ['quizHistory6']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': "",
            'roundHistory': "",
            'tableRandomNumberHistory': "",
            'tableNumberHistory': "",
            'myChoiceHistory': "",
            'otherChoiceHistory': "",
            'myPayoffHistory': "",
            'otherPayoffHistory': "",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question7(Page):
    form_model = 'player'
    form_fields = ['quizHistory7']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': "",
            'roundHistory': "",
            'tableRandomNumberHistory': "",
            'tableNumberHistory': "",
            'myChoiceHistory': "",
            'otherChoiceHistory': "",
            'myPayoffHistory': "",
            'otherPayoffHistory': "",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question8(Page):
    form_model = 'player'
    form_fields = ['quizHistory8']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': ",1,1,1,3,2",
            'roundHistory': ",1,2,3,4,5",
            'tableRandomNumberHistory': ",2,2,4,2,4",
            'tableNumberHistory': ",2,2,4,3,4",
            'myChoiceHistory': ",0,1,1,1,0",
            'otherChoiceHistory': ",1,0,0,1,0",
            'myPayoffHistory': ",40,14,28,44,32",
            'otherPayoffHistory': ",14,40,68,44,32",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question9(Page):
    form_model = 'player'
    form_fields = ['quizHistory9']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': ",1,1,1,3,2",
            'roundHistory': ",1,2,3,4,5",
            'tableRandomNumberHistory': ",2,2,4,2,4",
            'tableNumberHistory': ",2,2,4,3,4",
            'myChoiceHistory': ",0,1,1,1,0",
            'otherChoiceHistory': ",1,0,0,1,0",
            'myPayoffHistory': ",40,14,28,44,32",
            'otherPayoffHistory': ",14,40,68,44,32",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Question10(Page):
    form_model = 'player'
    form_fields = ['quizHistory10']

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': ",1,1,1,3,2",
            'roundHistory': ",1,2,3,4,5",
            'tableRandomNumberHistory': ",2,2,4,2,4",
            'tableNumberHistory': ",2,2,4,3,4",
            'myChoiceHistory': ",0,1,1,1,0",
            'otherChoiceHistory': ",1,0,0,1,0",
            'myPayoffHistory': ",25,12,12,32,25",
            'otherPayoffHistory': ",12,25,50,32,25",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class p01_WaitForGroup(WaitPage):
    template_name = 'DynamicQueue_04_Quiz/p01_WaitForGroup.html'

    @staticmethod
    def after_all_players_arrive(group: Group):
        pass

    @staticmethod
    def vars_for_template(player: Player):
        temp = {'matchNumber': 1}
        return temp


page_sequence = [
    beginQuiz,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10,
]
