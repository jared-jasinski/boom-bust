def block_reward(block):
    halvings = int(block / 210_000)
    if halvings >= 64:
        return 0
    max_quantity_to_release = 50 * 100_000_000 >> halvings
    block += 1
    return max_quantity_to_release / 100_000_000

