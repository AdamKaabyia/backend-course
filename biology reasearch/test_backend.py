# test_backend.py
import unittest
from backend import process_records, alive_rabbits


class TestBackend(unittest.TestCase):

    def test_process_records_no_deaths_exceeding(self):
        """Test processing with no records of deaths exceeding the living population."""
        test_records = [
            {'timestamp': '2024-03-20T12:00:00', 'deaths': 10, 'births': 20},
            # ... add more test records as needed ...
        ]
        result = process_records(test_records)
        self.assertEqual(len(result), len(test_records))
        self.assertEqual(alive_rabbits, 110)  # Assuming 100 initial rabbits plus 10 births

    def test_process_records_with_deaths_exceeding(self):
        """Test processing where a record has deaths exceeding the living population."""
        test_records = [
            {'timestamp': '2024-03-20T12:00:00', 'deaths': 101, 'births': 20},
            # ... add more test records as needed ...
        ]
        result = process_records(test_records)
        self.assertNotIn(test_records[0], result)
        self.assertEqual(alive_rabbits, 100)  # No change in the rabbit population

    def test_multiple_record_batches(self):
        """Test processing multiple batches of records."""
        test_records = [
            # First batch of 10
            {'timestamp': '2024-03-20T12:00:00', 'deaths': 5, 'births': 10},
            # ... add 9 more test records ...
            # Second batch of 10
            {'timestamp': '2024-03-20T12:10:00', 'deaths': 15, 'births': 20},
            # ... add 9 more test records ...
        ]
        # Process first batch
        process_records(test_records[:10])
        # Check results after first batch
        self.assertEqual(alive_rabbits, 105)  # Example expected value

        # Process second batch
        process_records(test_records[10:20])
        # Check results after second batch
        self.assertEqual(alive_rabbits, 110)  # Example expected value, depending on records




if __name__ == '__main__':
    unittest.main()
