from homeworks.intermediate.h2_smartphone_advanced import Smartphone, OnePlus


class PhoneManager:
    def __init__(self, smartphone):
        if not isinstance(smartphone, Smartphone):
            raise Exception('Provide a smartphone instance.')

        self._smartphone = smartphone

    def charge(self, minutes):
        try:
            self._smartphone.charge(minutes)
            charge = self._smartphone.get_charge ## without () bcs PROPERTY
            print(f'Charged for {minutes} and new charge level is {charge}%')
        except Exception as error:
            print(error)

    def play(self, minutes):
        try:
            self._smartphone.play(minutes)
            charge = self._smartphone.get_charge
            print(f'Music played for {minutes} and new charge level is {charge}%')
        except Exception as error:
            print(error)

    def turn_on(self):
        try:
            self._smartphone.turn_on()
        except Exception as error:
            print(error)

    def turn_off(self):
        try:
            self._smartphone.turn_off()
        except Exception as error:
            print(error)

    def get_charge(self):
        try:
            charge = self._smartphone.get_charge ## is property, so WITHOUT ()
            print(f'Charge level is {charge}%')
        except Exception as error:
            print(error)

    def get_brand(self):
        try:
            brand = self._smartphone.get_brand()
            print(brand)
        except Exception as error:
            print(error)

    def get_model(self):
        try:
            model = self._smartphone.get_model()
            print(model)
        except Exception as error:
            print(error)


smart = OnePlus('p10')
## I imported the class as follows: wrote its name. Ctrl+2times blank
# (if he gives you a list, choose yours among the) => is added above
phone = PhoneManager(smart)
phone.turn_on()
phone.get_charge()
phone.charge(10)
phone.play(20)
phone.get_charge()


