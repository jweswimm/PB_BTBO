#This script will run the simulation for the given number of iterations and return the results

class simulationExecutive():
    def __init__(self, stopTime, dt):
        self._stopTime = stopTime
        self._dt = dt

    def _getTimeReal(self, mode='current'):
        if mode == 'current':
            return self._currentTime
        else:
            return self._stopTime

    
    def run(self):
        for i in range(self.iterations):
            self.sim.run()
            self.results.append(self.sim.getResults())
        return self.results
    