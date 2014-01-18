from Payment import Payment
from Person import Person
import yaml

__author__ = 'Simon Mönch'
__license__ = 'MIT'


class YamlParser:
    @staticmethod
    def parse(filename):
        f = open(filename, 'r')
        data = yaml.load(f.read())
        f.close()

        persons = []
        for name in data['persons']:
            persons.append(Person(name))

        payments = []
        for pay in data['payments']:
            for owner in persons:
                if owner.name == pay['owner']:
                    payment = Payment(owner, float(pay['amount']))
                    for partie in persons:
                        if partie.name in pay['parties']:
                            payment.add_partie(partie)
                    owner.add_payment(payment)
                    payments.append(payment)

        return {'persons': persons, 'payments': payments}