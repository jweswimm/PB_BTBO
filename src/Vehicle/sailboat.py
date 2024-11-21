import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Vehicle.vehicle import Vehicle

class Sailboat(Vehicle):
    def __init__(self, make, model, length, beam, draft, mast_height, mass):
        super().__init__(make, model)
        self._mast_height = mast_height
        self._length = length
        self._beam = beam
        self._draft = draft
        self._mass = mass

    def _display_info(self):
        super()._display_info()
        print(f"Mast Height: {self._mast_height}, Beam: {self._beam}, Draft: {self._draft}, Mass: {self._mass}")
