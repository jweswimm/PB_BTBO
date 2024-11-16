# PB_BTBO
<h1>Autonomous Sailing</h1>
Objective: Create a series of tools, software, and philosophy behind an autonomous sailboat. Test and apply to my own boat. This is split up into various parts:

* Theoretical Uses & Philosophy
* Server
* Boat health diagnostics and surveilance 
* Navigation
* Communication
* Control
* MC Informed Guidance
* Displays & Interfaces

<h2>Theoretical Uses & Philosophy</h2>
I want to build the most technologically advanced boat in the world.
The boat should be able to sail itself to given coordinates and be completely controllable by the lead engineer.
<h3> Philosophy</h3>

**Robustness**: The boat should be able to sail effectively and respond to inclement weather. The controllable physical inputs to the boat should be durable. 

**Engineering**: There's something extremely special about developing systems from the ground up. Here we can create a unique suite of technology that has the potential to benefit the lives of an incredible community. Proper documentation is necesssary. Guidance and navigation will be informed via monte carlo sims. A physics-based simulation environment will account for the geometries of the sails, the mass properties of the boat, the fluid dynamics of the wind across the sail and the water across the hulls (Navier-Stokes). Realtime sensor updates can be implemented via NMEA2k bus facilitated by Signal K and regular API calls (e.g. tomorrow.io). 

For the montecarlo runs, I'm thinking of using parallelized sims via CUDA. The vehicle dynamics (integration steps) will take place in C++, while the parametrization and configurability will be in python (swig?).

Telemetry and chart plots inform real time montecarlos, MCs inform GNC, GNC informs controllable inputs.


<h3> Safety Drone </h3>
This could be used as a smaller boat following a larger sailing vessel. This drone could carry more equipment, food, surfboards, fishing poles, etc. 

<h3> Ocean Crossings </h3>
Open ocean crossings require concentration, planning, and difficult decisions. Having a telemetry + simulation informed GNC system would make safer passages.

<h2> Server </h2>
Signal K is the answer. 

- Raspberry Pi running [Signal K](https://signalk.org/)
    - [Guide](https://github.com/SignalK/signalk-server)
