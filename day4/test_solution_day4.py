import unittest
from solution_day4 import parse_pass_batch, read_pass_batch, is_valid_pass

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

class TestValidPass(unittest.TestCase):

    def test_valid_pass(self):
        valid_passes = [
                "ecl:g pid:8 eyr:2020 hcl:#ff byr:1937 iyr:2017 cid:1 hgt:18",
                "ecl:g pid:8 eyr:2020 hcl:#ff byr:1937 iyr:2017 hgt:18"
 ]
        invalid_passes = [
                "",
                "pid:8 eyr:2020 hcl:#ff byr:1937 iyr:2017 cid:1 hgt:18",
                "ecl:g eyr:2020 hcl:#ff byr:1937 iyr:2017 cid:1 hgt:18",
                "ecl:g pid:8 hcl:#ff byr:1937 iyr:2017 cid:1 hgt:18",
                "ecl:g pid:8 eyr:2020 byr:1937 cid:1 hgt:18",
                "ecl:g pid:8 eyr:2020 hcl:#ff byr:1937 iyr:2017 cid:1"
                ]
        for p in valid_passes:
            self.assertTrue(is_valid_pass(p))
        for p in invalid_passes:
            self.assertFalse(is_valid_pass(p))

if __name__ == "__main__":
    unittest.main()

