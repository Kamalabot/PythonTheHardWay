from nose.tools import *
from ex48 import lexicon

def test_directions():
    eq_(lexicon.scan("north"),[('direction','north')])
    result = lexicon.scan("north south east")
    eq_(result,[('direction','north'),
                ('direction','south'),
                ('direction','east')])

def test_verbs():
    eq_(lexicon.scan('go'),[('verb','go')])
    result = lexicon.scan("go kill eat")
    eq_(result,[('very','go'),
                ('verb','kill'),
                ('verb','eat')])

def test_stop():
    eq_(lexicon.scan('the'),[('stop','the')])
    result = lexicon.scan("the in of")
    eq_(result,[('stop','the'),
                ('stop','in'),
                ('stop','of')])

def test_nouns():
    eq_(lexicon.scan("bear"),[('noun','bear')])
    result = lexicon.scan('bear princess')
    eq_(result,[('noun','bear'),
                ('noun','princess')])

def test_numbers():
    eq_(lexicon.scan("1234"),[('number',1234)])
    result = lexicon.scan("3 91234")
    eq_(result,[('number',3),
                ('number',91234)])

def test_errors():
    eq_(lexicon.scan("ASFADFADS"),['error','ASFADFADS'])
    result = lexicon.scan("bear IAS princess")
    eq_(result,[('noun','bear'),
                ('error','IAS'),
                ('noun','princess')])