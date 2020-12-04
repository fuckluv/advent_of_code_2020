import unittest
from solution_day4 import parse_pass_batch, read_pass_batch

class TestParsePassBatch(unittest.TestCase):

    def test_parse_pass_batch(self):
        test_pass_batch = (
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd" "\n"
        "byr:1937 iyr:2017 cid:147 hgt:183cm" "\n"
        "\n"
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884" "\n"
        "hcl:#cfa07d byr:1929" "\n"
        )
        expected = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
        ]
        actual = [l for l in parse_pass_batch(test_pass_batch)]
        self.assertEqual(actual, expected)

class TestReadBatch(unittest.TestCase):

    def test_read_batch(self):
        actual = [l for l in read_pass_batch("./test_input.txt")]
        self.assertEqual(len(actual), 251)

if __name__ == "__main__":
    unittest.main()

