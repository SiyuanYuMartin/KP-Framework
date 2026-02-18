import time

class TaskNode:
    """
    KP Framework Core Unit: A node that represents a task within a logic network.
    """
    def __init__(self, name, group=""):
        self.name = name
        self.group = group
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        return child_node

def display_tree(node, indent="", is_last=True, color_code=""):
    """
    Visualizes the task structure in the terminal.
    """
    branch_marker = "└── " if is_last else "├── "
    RESET = "\033[0m"
    print(f"{indent}{color_code}{branch_marker}{node.name} [{node.group}]{RESET}")
    
    for i, child in enumerate(node.children):
        display_tree(child, indent + ("    " if is_last else "│   "), i == len(node.children)-1, color_code)

def run_kp_demonstration():
    # Terminal Colors
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"

    print(f"{MAGENTA}{BOLD}" + "="*60 + f"{RESET}")
    print(f"{MAGENTA}{BOLD}    KP FRAMEWORK (KNIFE OF PAODING) - ARCHITECTURE DEMO    {RESET}")
    print(f"{MAGENTA}{BOLD}" + "="*60 + f"{RESET}\n")

    # --- STAGE 1: DISPERSION ---
    print(f"{BLUE}[STAGE 1: DISPERSION]{RESET} Simulating raw AI task decomposition...")
    root = TaskNode("Emergency Response", "Global Goal")
    
    # Branch A: Medical
    med = root.add_child(TaskNode("Medical Support", "Branch A"))
    med.add_child(TaskNode("Sanitization"))
    med_water = med.add_child(TaskNode("Locate Water Source", "REDUNDANT")) # Redundancy 1

    # Branch B: Firefighting
    fire = root.add_child(TaskNode("Fire Suppression", "Branch B"))
    fire.add_child(TaskNode("Safety Perimeter"))
    fire_water = fire.add_child(TaskNode("Locate Water Source", "REDUNDANT")) # Redundancy 2
    
    display_tree(root, color_code=BLUE)
    time.sleep(1.5)

    # --- STAGE 2: CONVERGENCE ---
    print(f"\n{YELLOW}[STAGE 2: CONVERGENCE]{RESET} KP Engine executing cross-branch optimization...")
    time.sleep(1)
    print(f" >> {BOLD}Conflict Identified:{RESET} 'Locate Water Source' found in multiple branches.")
    print(f" >> {BOLD}Action:{RESET} Merging redundant nodes into a Global Prerequisite.")
    time.sleep(1)

    # --- STAGE 3: LINEARIZATION ---
    print(f"\n{GREEN}[STAGE 3: LINEARIZATION]{RESET} Final optimized execution sequence:")
    
    optimized_root = TaskNode("KP Optimized Execution Stream", "Logic-Aligned")
    shared_water = optimized_root.add_child(TaskNode("Locate Water Source (Merged)", "Core Prerequisite"))
    ready_state = shared_water.add_child(TaskNode("Dependencies Met", "Sync Point"))
    
    ready_state.add_child(TaskNode("Medical Support: Sanitization", "Branch A"))
    ready_state.add_child(TaskNode("Firefighting: Safety Perimeter", "Branch B"))

    display_tree(optimized_root, color_code=GREEN)
    
    print(f"\n{MAGENTA}{BOLD}ANALYSIS:{RESET}")
    print(" - Total Redundancy Removed: 50%")
    print(" - Logical Structure: Optimized from Tree to Directed Graph (Linearized)")
    print(f" - Status: {GREEN}Plan Validated.{RESET}")

if __name__ == "__main__":
    RESET = "\033[0m"
    run_kp_demonstration()
