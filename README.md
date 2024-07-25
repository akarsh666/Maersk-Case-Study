# Maersk-Case-Study
# Container Terminal Simulation

This project simulates a container terminal using SimPy. It models the arrival of vessels, the unloading of containers using quay cranes, and the transportation of containers to the yard using trucks.

## Features

- **Vessel Arrivals**: Vessels arrive at the terminal following an exponential distribution with an average of 5 hours.
- **Berthing**: The terminal has 2 berths for vessels. If both berths are occupied, incoming vessels must wait.
- **Cranes**: The terminal has 2 quay cranes. Each vessel uses one crane to unload containers. It takes 3 minutes to move one container.
- **Trucks**: The terminal has 3 trucks that transport containers from the quay cranes to the yard blocks. It takes 6 minutes for a truck to drop off a container and return.
- **Logging**: The simulation logs key events with timestamps, including vessel arrivals, berthing, crane operations, and truck movements.

## Running steps
- **Save the python file in a folder**
- **Create a Virtual Environment**: python -m venv myenv
- **Activate the Virtual Environment**: On Linux or macOS: source myenv/bin/activate ||
                                        On windows: myenv\Scripts\activate
- **Install SimPy in the Virtual Environment**: pip install simpy
- **Run Your Simulation Script**: python container_terminal_simulation.py
