
import random

print("Vacuum Agent Simulation(simple reflex agent) ")
print("Grid Layout: [A][B]")

# Start the vacuum in a random room
location = random.choice(['A', 'B']) 
rooms_checked = 0  #

while True:
    print(f"\n--- Current Location: Block {location} ---")
    
    # 1. Ask ONLY for the condition of the current block
    status = input(f"What is the condition on block {location} (clean/dirty) [or 'exit' to quit]: ").strip().lower()

    if status == 'exit':
        print("Ending simulation")
        break

    if status not in ['clean', 'dirty']:
        print("Invalid condition. Rooms can either be clean or dirty only.")
        continue

    print(f"\n[Agent Decision]:")
    
    # 2. Check condition first
    if status == 'dirty':
        print(f"   Block {location} is DIRTY -> Action: Suck")
        rooms_checked = 0  # Reset counter because we found dirt; need to re-verify everything
        
    # 3. If clean, automatically update 'location' for the next loop iteration
    elif location == 'A':
        print(f"   Block A is CLEAN -> Action: Move_Right")
        rooms_checked += 1  
        location = 'B'  # Automatically moves the agent to B
        
    elif location == 'B':
        print(f"   Block B is CLEAN -> Action: Move_Left")
        rooms_checked += 1 
        location = 'A'  # Automatically moves the agent to A
    
    # 4. This will now execute perfectly!
    if rooms_checked >= 2:
        print("\[Thorough Check Complete]: Both blocks A and B have been verified as CLEAN!")
        print("Ending simulation")
        break