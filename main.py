from sys import argv
from YamlParser import YamlParser

__author__ = 'Simon Mönch'
__license__ = 'MIT'

data = YamlParser.parse(argv[1])

for payment in data['payments']:
    owner = payment.owner
    avg = payment.average()

    for partie in payment.parties:
        owner.paid(partie, avg)
        partie.owes(owner, avg)

for person in data['persons']:
    print(person.name)
    print(person.pays)