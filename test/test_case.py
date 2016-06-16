from src.app import app
import unittest
import json


class ContactTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get("/")
        msg = "Hello, World! This is Sample Contact API"
        self.assertEquals(response.data, msg)

    def test_contact_generation(self):
        response = self.app.get("/api/v1/contact")
        json_data = json.loads(response.data)
        total_len = len(json_data)
        response = self.app.get("/api/v1/contact/generate/10")
        self.assertEquals(response.status, '200 OK')
        response = self.app.get("/api/v1/contact")
        self.assertEquals(response.status, '200 OK')
        json_data = json.loads(response.data)
        import pdb;pdb.set_trace()
        self.assertEquals(len(json_data), int(total_len) + 10)

    def test_contact_single(self):
        response = self.app.get("/api/v1/contact")
        json_data = json.loads(response.data)
        output_data =json_data[0]
        response = self.app.get("/api/v1/contact/"+output_data['email'])
        self.assertEquals(response.status, '200 OK')
        json_data_2 = json.loads(response.data)
        import pdb; pdb.set_trace()
        self.assertEquals(output_data, json_data_2[0])

    def test_contact_delete(self):
        response = self.app.get("/api/v1/contact/generate/10")
        response = self.app.get("/api/v1/contact")
        json_data = json.loads(response.data)
        output_data =json_data[0]
        response = self.app.delete("/api/v1/contact/"+output_data['email'])
        import pdb;pdb.set_trace()
        self.assertEquals(response.status, '204 NO CONTENT')
        response = self.app.get("/api/v1/contact")
        json_data = json.loads(response.data)
        self.assertEquals(len(json_data), 9)


if __name__ == '__main__':
    unittest.main()
