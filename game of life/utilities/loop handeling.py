import hashlib
import numpy as np


def grids_are_equal(grid1, grid2):
    return np.array_equal(grid1, grid2)


class GameUtils:
    @staticmethod
    def get_state_hash(grid):
        """Hash the grid state for loop detection."""
        grid_bytes = grid.tobytes()
        return hashlib.sha256(grid_bytes).hexdigest()

    @staticmethod
    def check_for_loop(state_hash, previous_states):
        """Check if the current state hash is in the set of previous states."""
        if state_hash in previous_states:
            print("Loop detected!")
            return True
        previous_states.add(state_hash)
        return False
