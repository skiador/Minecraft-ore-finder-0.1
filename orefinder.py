from minescript import player, getblock, echo

# x, y, z is the player position
x, y, z = [int(p) for p in player().position]


# scans the area around the player from a range of -10 to 5
for dx in range(-10, 6):
    for dy in range(-10, 6):
        for dz in range(-10, 6):

            bx = x + dx
            by = y + dy
            bz = z + dz

            # Here will search the area to try to find blocks
            block = getblock(bx, by, bz)

            # If it find a block with ore in the name it will show in the chat
            if "ore" in block:
                echo(f"Found a {block} at {bx} {by} {bz}")
