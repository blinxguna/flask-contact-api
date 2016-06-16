from faker import Factory
import pprint


CONTACT_MAPPING = {
    "name": "name",
    "email": "email",
    "address": {
        "type": "job",
        "line": "address",
        "city": "city",
        "zip": "zipcode"
    },
    "phone": {
        "type": "color_name",
        "number": "phone_number",
        "country": "country_code"
    }
}


class FakeContact(object):

    def __init__(self):
        self.fake = Factory.create()

    def generate_data(self, count):
        result = []
        for i in xrange(0, int(count)):
            result.append(self._create_fake_data())
        return result

    def _create_fake_data(self):
        output_dict = {}
        for k, v in CONTACT_MAPPING.items():
            if type(v) == dict:
                sub_dict = {}
                for k1, v1 in v.items():
                    sub_dict[k1] = getattr(self.fake, v1)()
                output_dict[k] = sub_dict
            else:
                output_dict[k] = getattr(self.fake, v)()
        return output_dict


if __name__ == "__main__":
    test = FakeContact()
    result = test.generate_data(10)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)
