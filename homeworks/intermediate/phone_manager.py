from homeworks.intermediate.h1_smartphone import Smartphone


class PhoneManager:
    def __init__(self, smartphone):
        if not isinstance(smartphone, Smartphone):
            raise Exception('Provide a smartphone instance.')

        self._smartphone = smartphone

    def charge(self, minutes):
        try:
            self._smartphone.charge(minutes)
            charge = self._smartphone.get_charge()
            print(f'Charge level is {charge}%')
        except Exception as error:
            print(error)

    def play(self, minutes):
        pass

    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def get_charge(self):
        pass

    def get_brand(self):
        brand = self._smartphone.get_brand()
        print(brand)

    def get_model(self):
        model = self._smartphone.get_model()
        print(model)
