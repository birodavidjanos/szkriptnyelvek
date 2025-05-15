import unittest

def hamming_tavolsag(str1: str, str2: str) -> int:
    """Számolja ki a Hamming-távolságot két azonos hosszúságú sztring között."""
    if len(str1) != len(str2):
        raise ValueError("A sztringek hossza eltér, így a Hamming-távolság nem értelmezhető.")

    return sum(el1 != el2 for el1, el2 in zip(str1, str2))

class TestHammingTavolsag(unittest.TestCase):
    def test_hamming_distance_normal(self):
        self.assertEqual(hamming_tavolsag("toned", "roses"), 3)

    def test_hamming_distance_identical(self):
        self.assertEqual(hamming_tavolsag("hello", "hello"), 0)

    def test_hamming_distance_full_difference(self):
        self.assertEqual(hamming_tavolsag("abc", "xyz"), 3)

    def test_hamming_distance_length_mismatch(self):
        with self.assertRaises(ValueError):
            hamming_tavolsag("short", "longer")

if __name__ == "__main__":
    unittest.main()
