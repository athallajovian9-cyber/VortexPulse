"""Unit test suite for Vortex Pulse native Win32 telemetry readers."""
import unittest
from pulse import get_cpu_count, get_ram_stats, CPUReader

class TestVortexPulse(unittest.TestCase):
    def test_cpu_count_valid(self):
        cores = get_cpu_count()
        self.assertIsInstance(cores, int)
        self.assertGreater(cores, 0)

    def test_ram_stats_valid(self):
        pct, used, total = get_ram_stats()
        self.assertGreaterEqual(pct, 0)
        self.assertLessEqual(pct, 100)
        self.assertGreater(total, 0.0)
        self.assertGreaterEqual(used, 0.0)
        self.assertLessEqual(used, total)

    def test_cpu_reader_sample(self):
        reader = CPUReader()
        pct = reader.get_percent()
        self.assertGreaterEqual(pct, 0.0)
        self.assertLessEqual(pct, 100.0)

if __name__ == "__main__":
    unittest.main()
