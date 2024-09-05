from otree.api import Currency as c, currency_range

from . import *
from otree.api import Bot



class PlayerBot(Bot):

    def play_round(self):
        submitted_answer = self.player.current_question()['choice1']
        yield (Question, {'submitted_answer': submitted_answer})
        if self.round_number == Constants.num_rounds:
            yield (Results)
