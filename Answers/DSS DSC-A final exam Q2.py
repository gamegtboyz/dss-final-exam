# import the library
from experta import *

# creat the children of 'Fact' class, called it 'Suggessions'
class Suggestions(Fact):
    pass

# create the children class of KnowledgeEngine, called it 'Questionnaires'
class Questionnaires(KnowledgeEngine):
    @Rule(Suggestions(market_ready='low',stage='Seed'))
    def cautious(self):
        print('Cautious Invest')

    @Rule(Suggestions(market_ready='low',stage='Series A'))
    def avoid(self):
        print('Avoid Invest')

    @Rule(Suggestions(market_ready='low',stage='Mature'))
    def avoid(self):
        print('Avoid Invest')

    @Rule(Suggestions(market_ready='medium',stage='Seed'))
    def moderate(self):
        print('Moderate Invest')

    @Rule(Suggestions(market_ready='medium',stage='Series A'))
    def moderate(self):
        print('Moderate Invest')

    @Rule(Suggestions(market_ready='medium',stage='Mature'))
    def cautious(self):
        print('Cautious Invest')

    @Rule(Suggestions(market_ready='high',stage='Seed', industry='technology'))
    def strong(self):
        print('Strong Invest')

    @Rule(Suggestions(market_ready='high',stage='Series A', industry='technology'))
    def moderate(self):
        print('Moderate Invest')

    @Rule(Suggestions(market_ready='high',stage='Mature', industry='technology'))
    def cautious(self):
        print('Cautious Invest')

    @Rule(Suggestions(market_ready='high',stage='Seed', industry='Real Estate'))
    def strong(self):
        print('Strong Invest')

    @Rule(Suggestions(market_ready='high',stage='Series A', industry='Real Estate'))
    def moderate(self):
        print('Moderate Invest')

    @Rule(Suggestions(market_ready='high',stage='Mature', industry='Real Estate'))
    def moderate(self):
        print('Moderate Invest')


# create the input of this script

industry = input('Please specify your industry (technology, Real Estate)')
market_ready = input('Please specify your market readiness (high/medium/low)')
stage = input('Please specify your startup stage (Seed/Series A/ Mature)')

# pass the variables into class
engine = Questionnaires()
engine.reset()

engine.declare(Suggestions(industry = industry, market_ready = market_ready, stage = stage))
engine.run()
