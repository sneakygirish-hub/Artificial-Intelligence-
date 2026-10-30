import random
import time

class VacuumEnvironment:
    def __init__(self):
        # Rooms can be 'Clean' or 'Dirty'
        self.locations = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }
        # Start vacuum cleaner in a random room
        self.vacuum_location = random.choice(['A', 'B'])

    def display_status(self):
        print(f"Environment Status -> Room A: {self.locations['A']} | Room B: {self.locations['B']}")
        print(f"Vacuum Location    -> Room {self.vacuum_location}\n")

    def all_clean(self):
        return self.locations['A'] == 'Clean' and self.locations['B'] == 'Clean'


class ReflexVacuumAgent:
    def __init__(self, environment):
        self.env = environment
        self.cost = 0  # Track performance cost (moves/cleans)

    def sense_and_act(self):
        current_loc = self.env.vacuum_location
        status = self.env.locations[current_loc]

        print(f"[Sensing] Vacuum is in Room {current_loc}. Status: {status}")
        time.sleep(0.8)  # Dramatic pause for simulation readability

        if status == 'Dirty':
            print(f"[Action] Sucking dirt in Room {current_loc}...")
            self.env.locations[current_loc] = 'Clean'
            self.cost += 1
        else:
            # If current room is clean, move to the other room
            next_loc = 'B' if current_loc == 'A' else 'A'
            print(f"[Action] Room {current_loc} is already clean. Moving to Room {next_loc}...")
            self.env.vacuum_location = next_loc
            self.cost += 1
        
        print(f"Current Performance Score (Actions taken): {self.cost}")
        print("-" * 50)


# --- Execution Flow ---
if __name__ == "__main__":
    print("=" * 50)
    print("      VACUUM CLEANER AGENT SIMULATION")
    print("=" * 50)
    
    # Initialize environment and agent
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent(env)
    
    # Display initial state
    env.display_status()
    print("-" * 50)

    # Simulation loop runs until both rooms are clean
    step = 1
    while not env.all_clean():
        print(f"Step {step}:")
        agent.sense_and_act()
        step += 1

    # Check one last time to confirm both are clean
    if env.all_clean():
        print("Step Encountered: All rooms are verified CLEAN!")
        env.display_status()
        print(f"Simulation completed successfully in {step-1} steps with a total cost of {agent.cost}.")
