import copy as cp

import numpy as np
from otree.api import *


author = 'Yaroslav Rosokha December 2019'
doc = """
Dynamic Queue Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'DynamicQueue_05_Experiment'
    seqs11 = [
        [
            4,
            12,
            30,
            4,
            15,
            1,
            10,
            2,
            5,
            2,
            11,
            19,
            6,
            2,
            1,
            2,
            5,
            7,
            2,
            3,
            2,
            2,
            9,
            8,
            6,
            2,
            3,
            13,
            1,
            21,
            13,
            1,
            12,
            9,
            8,
            6,
            15,
            2,
            3,
            1,
        ],
        [
            8,
            3,
            15,
            1,
            11,
            10,
            6,
            2,
            3,
            2,
            4,
            16,
            4,
            1,
            13,
            11,
            20,
            4,
            6,
            9,
            2,
            3,
            4,
            8,
            1,
            10,
            6,
            12,
            14,
            11,
            14,
            3,
            2,
            11,
            6,
            5,
            12,
            12,
            2,
            3,
        ],
        [
            7,
            6,
            4,
            7,
            8,
            3,
            1,
            3,
            9,
            1,
            6,
            3,
            2,
            2,
            2,
            38,
            22,
            7,
            2,
            1,
            4,
            5,
            3,
            3,
            6,
            1,
            1,
            21,
            1,
            15,
            17,
            1,
            14,
            5,
            3,
            1,
            4,
            3,
            5,
            1,
        ],
        [
            11,
            15,
            8,
            1,
            7,
            6,
            3,
            4,
            5,
            6,
            16,
            2,
            4,
            4,
            3,
            1,
            7,
            8,
            12,
            2,
            1,
            10,
            11,
            6,
            4,
            6,
            1,
            4,
            18,
            2,
            9,
            1,
            6,
            10,
            20,
            1,
            1,
            1,
            3,
            5,
        ],
    ]
    cumul11 = [np.roll(np.cumsum(s, dtype=int), 1) for s in seqs11]
    seqs9 = [
        [
            4,
            3,
            7,
            1,
            1,
            5,
            3,
            1,
            1,
            9,
            8,
            1,
            2,
            4,
            10,
            4,
            1,
            1,
            1,
            4,
            1,
            4,
            2,
            4,
            1,
            2,
            8,
            3,
            7,
            12,
            4,
            2,
            2,
            1,
            2,
            2,
            3,
            7,
            1,
            1,
            3,
            2,
            1,
            1,
            9,
            2,
            1,
            1,
            4,
            2,
        ],
        [
            1,
            2,
            1,
            2,
            6,
            2,
            1,
            1,
            2,
            2,
            2,
            5,
            3,
            1,
            1,
            4,
            1,
            1,
            2,
            2,
            2,
            3,
            1,
            4,
            6,
            2,
            1,
            2,
            2,
            2,
            2,
            2,
            9,
            1,
            1,
            3,
            3,
            1,
            1,
            7,
            3,
            3,
            5,
            5,
            1,
            1,
            4,
            15,
            4,
            6,
        ],
        [
            3,
            2,
            1,
            3,
            1,
            1,
            2,
            1,
            4,
            2,
            4,
            1,
            1,
            1,
            4,
            3,
            2,
            4,
            2,
            2,
            7,
            3,
            3,
            2,
            3,
            1,
            3,
            3,
            6,
            1,
            6,
            3,
            2,
            2,
            2,
            1,
            1,
            4,
            1,
            3,
            2,
            1,
            1,
            6,
            3,
            3,
            6,
            4,
            2,
            9,
        ],
        [
            2,
            4,
            7,
            7,
            1,
            1,
            1,
            3,
            1,
            5,
            3,
            3,
            5,
            1,
            7,
            1,
            3,
            2,
            2,
            5,
            6,
            8,
            1,
            1,
            5,
            1,
            2,
            3,
            1,
            3,
            4,
            5,
            1,
            2,
            2,
            1,
            5,
            3,
            7,
            1,
            2,
            4,
            4,
            1,
            2,
            1,
            4,
            3,
            4,
            4,
        ],
    ]
    cumul9 = [np.roll(np.cumsum(s, dtype=int), 1) for s in seqs9]
    seqs7 = [
        [
            4,
            2,
            1,
            5,
            1,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            3,
            1,
            1,
            9,
            5,
            3,
            1,
            2,
            2,
            2,
            2,
            7,
            1,
            4,
            1,
            1,
            1,
            3,
            1,
            1,
            2,
            1,
            1,
            2,
            4,
            1,
            2,
            2,
            6,
            3,
            1,
            6,
            12,
            2,
            2,
            2,
            2,
            1,
            1,
            1,
            2,
            3,
            7,
            1,
            1,
            3,
            1,
            1,
            1,
            1,
            5,
            2,
            2,
            2,
            1,
            1,
            4,
            2,
            1,
            2,
            1,
            2,
            6,
            1,
            1,
            1,
            1,
            2,
            2,
            1,
            1,
            1,
            5,
            1,
            1,
            6,
            1,
            3,
            1,
            1,
            2,
            2,
            1,
            1,
            1,
            1,
            1,
            4,
        ],
        [
            2,
            2,
            1,
            4,
            3,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            1,
            2,
            1,
            1,
            4,
            1,
            2,
            2,
            1,
            2,
            1,
            2,
            1,
            1,
            2,
            2,
            2,
            1,
            7,
            1,
            1,
            1,
            1,
            2,
            3,
            1,
            1,
            1,
            1,
            5,
            3,
            3,
            5,
            5,
            1,
            1,
            4,
            2,
            13,
            2,
            1,
            1,
            1,
            2,
            1,
            2,
            3,
            2,
            1,
            3,
            1,
            1,
            2,
            1,
            2,
            2,
            2,
            4,
            1,
            1,
            1,
            1,
            3,
            1,
            1,
            2,
            1,
            1,
            1,
            2,
            3,
            3,
            2,
            1,
            4,
            4,
            2,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
        ],
        [
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            1,
            4,
            2,
            2,
            1,
            3,
            2,
            2,
            1,
            1,
            3,
            3,
            6,
            1,
            1,
            2,
            2,
            1,
            3,
            2,
            2,
            2,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            3,
            2,
            1,
            4,
            1,
            1,
            4,
            1,
            1,
            4,
            2,
            1,
            1,
            1,
            2,
            1,
            3,
            7,
            7,
            1,
            1,
            1,
            2,
            1,
            1,
            5,
            3,
            3,
            4,
            1,
            1,
            4,
            3,
            1,
            3,
            1,
            2,
            2,
            2,
            1,
            3,
            1,
            1,
            1,
            1,
            2,
            2,
            1,
            1,
            5,
            1,
            3,
            2,
            2,
            1,
        ],
        [
            2,
            2,
            4,
            1,
            1,
            2,
            3,
            2,
            2,
            4,
            1,
            1,
            2,
            3,
            1,
            2,
            2,
            1,
            1,
            3,
            1,
            3,
            3,
            2,
            1,
            2,
            2,
            1,
            5,
            1,
            2,
            4,
            3,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            1,
            2,
            1,
            1,
            1,
            2,
            1,
            2,
            2,
            2,
            4,
            1,
            6,
            3,
            2,
            2,
            1,
            1,
            1,
            4,
            4,
            2,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            4,
            1,
            1,
            3,
            2,
            1,
            4,
            1,
            1,
            1,
            1,
            1,
            3,
            1,
            2,
            4,
            1,
            2,
            1,
            1,
            1,
            4,
            1,
            5,
            2,
            1,
            2,
            2,
            1,
        ],
    ]
    cumul7 = [np.roll(np.cumsum(s, dtype=int), 1) for s in seqs7]
    players_per_group = 2
    num_rounds = 300
    payoff_matrices = {2: [[32, 40], [14, 24]], 3: [[32, 68], [28, 44]], 4: [[32, 68], [28, 64]]}


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    matchNumber = models.IntegerField()
    myChoice = models.IntegerField()
    myPayoff = models.CurrencyField()
    tableNumber = models.IntegerField()
    tableRandomNumber = models.IntegerField()
    roll = models.IntegerField()
    roundNumber = models.IntegerField()
    visibility = models.StringField()
    rollHistory = models.StringField()
    roundHistory = models.StringField()
    tableRandomNumberHistory = models.StringField()
    tableNumberHistory = models.StringField()
    myChoiceHistory = models.StringField()
    otherChoiceHistory = models.StringField()
    myPayoffHistory = models.StringField()
    otherPayoffHistory = models.StringField()


# FUNCTIONS
def get_round_outcomes(group: Group):
    p1, p2 = group.get_players()
    p1.myPayoff = Constants.payoff_matrices[p1.tableNumber][p1.myChoice][p2.myChoice]
    p2.myPayoff = Constants.payoff_matrices[p2.tableNumber][p2.myChoice][p1.myChoice]
    p1.payoff = Constants.payoff_matrices[p1.tableNumber][p1.myChoice][p2.myChoice]
    p2.payoff = Constants.payoff_matrices[p2.tableNumber][p2.myChoice][p1.myChoice]
    seq_id = group.session.config['Sequence'] - 1
    if group.session.config['CutoffRoll'] == 7:
        crit_rounds = Constants.cumul7[seq_id]
    if group.session.config['CutoffRoll'] == 9:
        crit_rounds = Constants.cumul9[seq_id]
    if group.session.config['CutoffRoll'] == 11:
        crit_rounds = Constants.cumul11[seq_id]
    if group.round_number in crit_rounds:
        temp_roll = np.random.choice(list(range(group.session.config['CutoffRoll'], 13)))
        p1.roll = temp_roll
        p2.roll = temp_roll
    else:
        temp_roll = np.random.choice(list(range(1, group.session.config['CutoffRoll'])))
        p1.roll = temp_roll
        p2.roll = temp_roll
    p1.update_history()
    p2.update_history()


def init_match(group: Group):
    for p in group.get_players():
        p.init_match()


def init_round(group: Group):
    for p in group.get_players():
        p.init_round()


def creating_session(subsession: Subsession):
    players = subsession.get_players()
    seq_id = subsession.session.config['Sequence'] - 1
    if subsession.session.config['CutoffRoll'] == 7:
        crit_rounds = Constants.cumul7[seq_id]
    if subsession.session.config['CutoffRoll'] == 9:
        crit_rounds = Constants.cumul9[seq_id]
    if subsession.session.config['CutoffRoll'] == 11:
        crit_rounds = Constants.cumul11[seq_id]
    crit_rounds[0] = 0
    if subsession.round_number - 1 in crit_rounds:
        subsession.group_randomly()
    else:
        subsession.group_like_round(subsession.round_number - 1)


def init_match(player: Player):
    player.myChoiceHistory = ""
    player.myPayoffHistory = ""
    player.tableRandomNumberHistory = ""
    player.tableNumberHistory = ""
    player.otherChoiceHistory = ""
    player.otherPayoffHistory = ""
    player.rollHistory = ""
    player.roundHistory = ""
    player.roundNumber = 1
    if player.id_in_group == 1:
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if player.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if player.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        crit_rounds[0] = 0
        player.matchNumber = np.argwhere(crit_rounds == player.round_number - 1)[0][0] + 1
        player.tableRandomNumber = np.random.choice([2, 3, 4])
        player.tableNumber = player.tableRandomNumber
        for p in player.get_others_in_group():
            p.matchNumber = player.matchNumber
            p.tableRandomNumber = player.tableRandomNumber
            p.tableNumber = player.tableRandomNumber


def init_round(player: Player):
    player.myChoiceHistory = player.in_round(player.round_number - 1).myChoiceHistory
    player.myPayoffHistory = player.in_round(player.round_number - 1).myPayoffHistory
    player.otherChoiceHistory = player.in_round(player.round_number - 1).otherChoiceHistory
    player.otherPayoffHistory = player.in_round(player.round_number - 1).otherPayoffHistory
    player.tableNumberHistory = player.in_round(player.round_number - 1).tableNumberHistory
    player.tableRandomNumberHistory = player.in_round(
        player.round_number - 1
    ).tableRandomNumberHistory
    player.roundHistory = player.in_round(player.round_number - 1).roundHistory
    player.rollHistory = player.in_round(player.round_number - 1).rollHistory
    player.matchNumber = player.in_round(player.round_number - 1).matchNumber
    seq_id = player.session.config['Sequence'] - 1
    if player.session.config['CutoffRoll'] == 7:
        crit_rounds = Constants.cumul7[seq_id]
    if player.session.config['CutoffRoll'] == 9:
        crit_rounds = Constants.cumul9[seq_id]
    if player.session.config['CutoffRoll'] == 11:
        crit_rounds = Constants.cumul11[seq_id]
    crit_rounds[0] = 0
    player.roundNumber = int(player.round_number - crit_rounds[player.matchNumber - 1])
    if player.id_in_group == 1:
        leftover = (
            player.in_round(player.round_number - 1).tableNumber
            - player.in_round(player.round_number - 1).myChoice
            - 1
        )
        for p in player.get_others_in_group():
            leftover -= p.in_round(player.round_number - 1).myChoice + 1
        leftover = max(leftover, 0)
        player.tableRandomNumber = np.random.choice([2, 3, 4])
        player.tableNumber = min(leftover + player.tableRandomNumber, 4)
        for p in player.get_others_in_group():
            p.tableRandomNumber = player.tableRandomNumber
            p.tableNumber = player.tableNumber


def update_history(player: Player):
    player.rollHistory += "," + str(player.roll)
    player.roundHistory += "," + str(player.roundNumber)
    player.tableNumberHistory += "," + str(player.tableNumber)
    player.tableRandomNumberHistory += "," + str(player.tableRandomNumber)
    player.myChoiceHistory += "," + str(player.myChoice)
    player.myPayoffHistory += "," + str(player.myPayoff)
    for p in player.get_others_in_group():
        player.otherChoiceHistory += "," + str(p.myChoice)
        player.otherPayoffHistory += "," + str(p.myPayoff)


# PAGES
class visibilityAnnouncement(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if player.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if player.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        crit_rounds[0] = 0
        player.matchNumber = int(np.sum(np.array(crit_rounds) < player.round_number))
        return {
            'FirstMatch': player.matchNumber,
            'LastMatch': int(player.session.config['Matches']),
            'Drawn': player.session.config['ShowQueue'],
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }


class beginExperiment(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'Matches': player.session.config['Matches'],
            'PointsPerDollar': int(1.0 / player.session.config['real_world_currency_per_point']),
            'ShowUpFee': int(player.session.config['participation_fee']),
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }


class p01_WaitForGroup(WaitPage):
    template_name = 'DynamicQueue_05_Experiment/p01_WaitForGroup.html'

    @staticmethod
    def after_all_players_arrive(group: Group):
        seq_id = group.session.config['Sequence'] - 1
        if group.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if group.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if group.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        crit_rounds[0] = 0
        if (group.round_number - 1) in crit_rounds:
            init_match(group)
        else:
            init_round(group)

    @staticmethod
    def vars_for_template(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if player.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if player.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        crit_rounds[0] = 0
        player.matchNumber = int(np.sum(np.array(crit_rounds) < player.round_number))
        temp = {
            'matchNumber': player.matchNumber,
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp

    @staticmethod
    def is_displayed(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            total_rounds = np.sum(Constants.seqs7[seq_id])
        if player.session.config['CutoffRoll'] == 9:
            total_rounds = np.sum(Constants.seqs9[seq_id])
        if player.session.config['CutoffRoll'] == 11:
            total_rounds = np.sum(Constants.seqs11[seq_id])
        return player.round_number <= total_rounds


class p02_Round(Page):
    form_model = 'player'
    form_fields = ['myChoice']

    @staticmethod
    def is_displayed(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            total_rounds = np.sum(Constants.seqs7[seq_id])
        if player.session.config['CutoffRoll'] == 9:
            total_rounds = np.sum(Constants.seqs9[seq_id])
        if player.session.config['CutoffRoll'] == 11:
            total_rounds = np.sum(Constants.seqs11[seq_id])
        return player.round_number <= total_rounds

    @staticmethod
    def vars_for_template(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if player.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if player.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        crit_rounds[0] = 0
        player.matchNumber = int(np.sum(np.array(crit_rounds) < player.round_number))
        temp = {
            'rollHistory': player.rollHistory,
            'roundHistory': player.roundHistory,
            'tableRandomNumberHistory': player.tableRandomNumberHistory,
            'tableNumberHistory': player.tableNumberHistory,
            'myChoiceHistory': player.myChoiceHistory,
            'otherChoiceHistory': player.otherChoiceHistory,
            'myPayoffHistory': player.myPayoffHistory,
            'otherPayoffHistory': player.otherPayoffHistory,
            'matchNumber': player.matchNumber,
            'tableNumber': player.tableNumber,
            'tableRandomNumber': player.tableRandomNumber,
            'ShowQueue': player.session.config['ShowQueue'] == 'before',
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class p03_WaitForChoice(WaitPage):
    template_name = 'DynamicQueue_05_Experiment/p03_WaitForChoice.html'

    @staticmethod
    def after_all_players_arrive(group: Group):
        get_round_outcomes(group)

    @staticmethod
    def is_displayed(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            total_rounds = np.sum(Constants.seqs7[seq_id])
        if player.session.config['CutoffRoll'] == 9:
            total_rounds = np.sum(Constants.seqs9[seq_id])
        if player.session.config['CutoffRoll'] == 11:
            total_rounds = np.sum(Constants.seqs11[seq_id])
        return player.round_number <= total_rounds

    @staticmethod
    def vars_for_template(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if player.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if player.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        crit_rounds[0] = 0
        player.matchNumber = int(np.sum(np.array(crit_rounds) < player.round_number))
        player.visibility = player.session.config['ShowQueue']
        temp = {
            'rollHistory': player.rollHistory,
            'roundHistory': player.roundHistory,
            'tableRandomNumberHistory': player.tableRandomNumberHistory,
            'tableNumberHistory': player.tableNumberHistory,
            'myChoiceHistory': player.myChoiceHistory,
            'otherChoiceHistory': player.otherChoiceHistory,
            'myPayoffHistory': player.myPayoffHistory,
            'otherPayoffHistory': player.otherPayoffHistory,
            'matchNumber': player.matchNumber,
            'tableNumber': player.tableNumber,
            'tableRandomNumber': player.tableRandomNumber,
            'myChoice': player.myChoice,
            'ShowQueue': player.session.config['ShowQueue'] == 'before',
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


class p04_postMatch(Page):
    @staticmethod
    def is_displayed(player: Player):
        seq_id = player.session.config['Sequence'] - 1
        if player.session.config['CutoffRoll'] == 7:
            crit_rounds = Constants.cumul7[seq_id]
        if player.session.config['CutoffRoll'] == 9:
            crit_rounds = Constants.cumul9[seq_id]
        if player.session.config['CutoffRoll'] == 11:
            crit_rounds = Constants.cumul11[seq_id]
        return (player.round_number) in crit_rounds

    @staticmethod
    def vars_for_template(player: Player):
        temp = {
            'rollHistory': player.rollHistory,
            'roundHistory': player.roundHistory,
            'tableRandomNumberHistory': player.tableRandomNumberHistory,
            'tableNumberHistory': player.tableNumberHistory,
            'myChoiceHistory': player.myChoiceHistory,
            'otherChoiceHistory': player.otherChoiceHistory,
            'myPayoffHistory': player.myPayoffHistory,
            'otherPayoffHistory': player.otherPayoffHistory,
            'matchNumber': player.matchNumber,
            'tableNumber': player.tableNumber,
            'tableRandomNumber': player.tableRandomNumber,
            'CutoffRoll': int(player.session.config['CutoffRoll']),
        }
        return temp


page_sequence = [
    beginExperiment,
    visibilityAnnouncement,
    p01_WaitForGroup,
    p02_Round,
    p03_WaitForChoice,
    p04_postMatch,
]
