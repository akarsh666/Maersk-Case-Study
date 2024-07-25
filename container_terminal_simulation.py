import simpy
import random


SIMULATION_TIME = 1000  
AVG_ARRIVAL_TIME = 5  
NUM_CONTAINERS = 150  
NUM_BERTHS = 2
NUM_CRANES = 2
CRANE_TIME_PER_CONTAINER = 3  
NUM_TRUCKS = 3
TRUCK_TIME = 6  

def vessel(env, name, berths, cranes, trucks):
    
    print(f'{env.now}: Vessel {name} arrives')
    
    
    with berths.request() as berth_request:
        yield berth_request
        print(f'{env.now}: Vessel {name} berths')
        
        for _ in range(NUM_CONTAINERS):
            
            with cranes.request() as crane_request:
                yield crane_request
                print(f'{env.now}: Crane starts unloading container from Vessel {name}')
                
                
                yield env.timeout(CRANE_TIME_PER_CONTAINER)
                
                
                with trucks.request() as truck_request:
                    yield truck_request
                    print(f'{env.now}: Truck starts transporting container from Vessel {name}')
                    
                    
                    yield env.timeout(TRUCK_TIME)
                    print(f'{env.now}: Truck has dropped off container from Vessel {name}')
        
        print(f'{env.now}: Vessel {name} departs')

def vessel_arrivals(env, berths, cranes, trucks):
    vessel_number = 0
    while True:
        yield env.timeout(random.expovariate(1 / AVG_ARRIVAL_TIME))
        vessel_number += 1
        env.process(vessel(env, f'Vessel_{vessel_number}', berths, cranes, trucks))


env = simpy.Environment()


berths = simpy.Resource(env, NUM_BERTHS)
cranes = simpy.Resource(env, NUM_CRANES)
trucks = simpy.Resource(env, NUM_TRUCKS)


env.process(vessel_arrivals(env, berths, cranes, trucks))


env.run(until=SIMULATION_TIME)

