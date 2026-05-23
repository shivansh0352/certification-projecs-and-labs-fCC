def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),  # Source rod
        [],                     # Auxiliary rod
        []                      # Target rod
    ]

    result = []

    # Saved the current state of rods
    def save_state():
        result.append(f"{rods[0]} {rods[1]} {rods[2]}")

    # Recursive Hanoi Solver
    def move(disks, source, target, auxiliary):
        if disks == 1:
            rods[target].append(rods[source].pop())
            save_state()
            return

        move(disks - 1, source, auxiliary, target)

        rods[target].append(rods[source].pop())
        save_state()

        move(disks - 1, auxiliary, target, source)

    save_state()
    move(n, 0, 2, 1)

    return "\n".join(result)