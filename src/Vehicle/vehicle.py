import numpy as np
class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model
        #Initialize mass properties
        self._mass_properties = {
            'mass': 0,
            'cm': np.zeros(3),  # Center of mass as a 3-element vector
            'inertia': np.zeros((3, 3))  # 3x3 inertia matrix
        }

    def _setVehicleMassProperties(self, data):
        self._mass_properties['mass'] = data['mass']
        self._mass_properties['cm'] = np.array([data['cm_x'], data['cm_y'], data['cm_z']])
        self._mass_properties['inertia'] = np.array([
            [data['inertia_00'], data['inertia_01'], data['inertia_02']],
            [data['inertia_10'], data['inertia_11'], data['inertia_12']],
            [data['inertia_20'], data['inertia_21'], data['inertia_22']]
        ])

    def _display_info(self):
        print(f"Vehicle Make: {self._make}, Model: {self._model}")
        print(f"Mass Properties: {self._mass_properties}")


