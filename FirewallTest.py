import unittest
import csv
from Firewall import Firewall


class TestFirewall(unittest.TestCase):

    def setUp(self):
        self.firewall = Firewall("input.csv")
        self.records = []
        with open("test.csv") as csvfile:
            for row in csv.reader(csvfile):
                self.records.append(row)

    def test_all_records(self):
        for index, record in enumerate(self.records):
            with self.subTest(index):
                if record[4] == "True":
                    self.assertTrue(self.firewall.accept_packet(*self.__get_arguments(record)))
                else:
                    self.assertFalse(self.firewall.accept_packet(*self.__get_arguments(record)))

    @staticmethod
    def __get_arguments(record):
        return record[0], record[1], int(record[2]), record[3]


if __name__ == '__main__':
    unittest.main()
