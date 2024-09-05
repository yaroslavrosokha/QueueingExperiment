from otree.api import *


author = 'Yaroslav Rosokha'
doc = """
Payoff information.
"""


class Constants(BaseConstants):
    name_in_url = 'DynamicQueue_06_PayoffScreen'
    players_per_group = None
    num_rounds = 1


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
### Change EarnBelief5 to EarnBelief25 below ###
class PaymentInfo(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['totalPayoffs'] = player.participant.payoff.to_real_world_currency(
            player.session
        )

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'MatchesPayoff': player.participant.payoff.to_real_world_currency(player.session),
            'TotalPayoff': player.participant.payoff_plus_participation_fee(),
            'Matches': player.session.config['Matches'],
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [PaymentInfo]
