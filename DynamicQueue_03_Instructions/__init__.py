from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Dynamic Queue experiment description of the payoff tables and transitions.
"""


class Constants(BaseConstants):
    name_in_url = 'DynamicQueue_03_Instructions'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    testingHistory = models.StringField()


# FUNCTIONS
# PAGES
class Instructions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoiceHistory': None,
            'otherChoiceHistory':None,
            'myPayoffHistory': None,
            'otherPayoffHistory': None,
            'tableRandomNumberHistory': None,
            'tableNumberHistory': None,
            'rollHistory': None,
            'myChoice': None,
            'otherChoice': None,
            'ShowQueue': None,
        }


class RoundDescription(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoiceHistory': None,
            'otherChoiceHistory':None,
            'myPayoffHistory':None,
            'otherPayoffHistory':None,
            'tableRandomNumberHistory':None,
            'tableNumberHistory':None,
            'rollHistory':None,
            'myChoice':None,
            'ShowQueue':None,

        }


class PayoffDetails(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoiceHistory': None,
            'otherChoiceHistory': None,
            'myPayoffHistory': None,
            'otherPayoffHistory': None,
            'tableRandomNumberHistory': None,
            'tableNumberHistory': None,
            'rollHistory': None,
            'myChoice': None,
            'otherChoice': None,
            'ShowQueue': None,
        }


class PayoffExample(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoiceHistory': None,
            'otherChoiceHistory': None,
            'myPayoffHistory': None,
            'otherPayoffHistory': None,
            'tableRandomNumberHistory': None,
            'tableNumberHistory': None,
            'rollHistory': None,
            'myChoice': None,
            'otherChoice': None,
            'ShowQueue': None,

        }


class Transitions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoiceHistory': None,
            'otherChoiceHistory': None,
            'myPayoffHistory': None,
            'otherPayoffHistory': None,
            'tableRandomNumberHistory': None,
            'tableNumberHistory': None,
            'rollHistory': None,
            'myChoice': None,
            'otherChoice': None,
            'ShowQueue': None,
        }


class History(Page):
    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoice': None,
            'otherChoice': None,
            'ShowQueue': None,
            'rollHistory': ",3,1,11",
            'roundHistory': ",1,2,3",
            'tableRandomNumberHistory': ",4,2,2",
            'tableNumberHistory': ",4,3,2",
            'myChoiceHistory': ",0,1,1",
            'otherChoiceHistory': ",1,1,0",
            'myPayoffHistory': ",68,44,14",
            'otherPayoffHistory': ",28,44,40",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class TransitionsExample(Page):
    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'tableRandomNumber': None,
            'tableNumber': None,
            'myChoice': None,
            'otherChoice': None,
            'ShowQueue': None,
            'rollHistory': ",3,1,11",
            'roundHistory': ",1,2,3",
            'tableRandomNumberHistory': ",4,2,2",
            'tableNumberHistory': ",4,3,2",
            'myChoiceHistory': ",0,1,1",
            'otherChoiceHistory': ",1,1,0",
            'myPayoffHistory': ",68,44,14",
            'otherPayoffHistory': ",28,44,40",
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class Matches(Page):
    form_model = 'player'
    form_fields = ['testingHistory']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'Matches': player.session.config['Matches'],
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }


page_sequence = [
    Matches,
    RoundDescription,
    Instructions,
    PayoffDetails,
    PayoffExample,
    Transitions,
    History,
    TransitionsExample,
]
