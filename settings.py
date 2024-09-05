from os import environ


SESSION_CONFIGS = [

    {
        'name': 'Dynamic_Queue_Study2_11',
        'display_name': "4-6 4pm Study 2_11 (Visible,.83,Seq = 2,Matches = 40)",
        'num_demo_participants': 2,
        'app_sequence': [
            'DynamicQueue_01_Consent',
            'DynamicQueue_02_Introduction',
            'DynamicQueue_03_Instructions',
            'DynamicQueue_04_Quiz',
            'DynamicQueue_05_Experiment',
            'DynamicQueue_06_PayoffScreen',
            'DynamicQueue_07_Demographics',
            # 'DynamicQueue_08_FeedbackQuestions',
            'DynamicQueue_09_Feedback',
        ],

        'ShowQueue': 'before',
        'CutoffRoll': 11,
        'Sequence': 2,
        'Matches': 40,

        'doc': """
    'Sequence' parameter determines which sequence of supergame lengths is used.
    'Matches' parameter determines how many matches are played.
    'CutoffRoll' parameter determines the continuation probability (.5 -> cutoff=7, .66 -> cutoff=9, .75-> cutoff=10).
    'ShowQueue' parameter determines which treatment is played ('before'='Visible', 'after'='Not Visible')
"""

    },



]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = ''

INSTALLED_APPS = ['otree']
