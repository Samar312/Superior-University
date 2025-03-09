def jug_solver(limit_x, limit_y, goal):
    def possible_moves(state):
        x, y = state
        states = []
        states.append((limit_x, y))
        states.append((x, limit_y))
        states.append((0, y))
        states.append((x, 0))
        transfer = min(x, limit_y - y)
        states.append((x - transfer, y + transfer))
        transfer = min(y, limit_x - x)
        states.append((x + transfer, y - transfer))
        return states

    checked = set()
    queue = [((0, 0), [(0, 0)])]

    while queue:
        (cur_x, cur_y), path = queue.pop()
        if cur_x == goal or cur_y == goal:
            return path
        if (cur_x, cur_y) not in checked:
            checked.add((cur_x, cur_y))
            for new_state in possible_moves((cur_x, cur_y)):
                if new_state not in checked:
                    queue.append((new_state, path + [new_state]))
    return None

def display_steps(steps):
    if steps:
        print("Solution path:")
        for idx, (x, y) in enumerate(steps, 1):
            print(f"Step {idx}: Jug X: {x}, Jug Y: {y}")
    else:
        print("No valid solution found.")

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt).strip())  # Strip whitespace and convert to int
            if value > 0:  # Ensure positive input
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Enter a valid integer.")

x_capacity = get_integer_input("Enter capacity of Jug X: ")
y_capacity = get_integer_input("Enter capacity of Jug Y: ")
goal_amount = get_integer_input("Enter target amount: ")

result = jug_solver(x_capacity, y_capacity, goal_amount)
display_steps(result)
