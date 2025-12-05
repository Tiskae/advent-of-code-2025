def is_repeated_sequence(index_map, length):
    """
    index_map: dict {digit: [sorted indices]}
    length: total length of the number
    Return True only if the number is exactly B repeated k times (k >= 2)
    """

    # Get all possible block sizes (must divide the total length)
    divisors = [d for d in range(1, length) if length % d == 0]

    for L in divisors:
        k = length // L
        if k < 2:
            continue  # must repeat at least twice

        # Try to reconstruct the block
        block = [None] * L
        consistent = True

        for digit, idxs in index_map.items():
            for idx in idxs:
                pos = idx % L
                if block[pos] is None:
                    block[pos] = digit
                elif block[pos] != digit:
                    consistent = False
                    break
            if not consistent:
                break

        if not consistent:
            continue  # This block length not possible

        # Now verify reconstructed block produces *exactly* the same index map
        regenerated = {}
        for pos in range(length):
            d = block[pos % L]
            if d not in regenerated:
                regenerated[d] = []
            regenerated[d].append(pos)

        # Compare regenerated with original
        if regenerated == index_map:
            return True  # FOUND a true repeat sequence

    return False


def findInvalidIDs(id_ranges):
    # convert the id ranges to a list
    ranges_strings = id_ranges.split(",")
    ranges = []
    invalid_ids = []
    
    # format each range as a list: [start, end]
    for rng in ranges_strings:
        limits = rng.split("-")
        ranges.append([int(limits[0]), int(limits[1])])
        
    # find invalid ids
    for r in ranges:
        start, end = r

        for num in range(start, end + 1):
            numbers_hashmap = {}

            # format each number
            for idx, j in enumerate(str(num)):
                key = j
                if numbers_hashmap.get(key):
                    numbers_hashmap[key].append(idx)
                else:
                    numbers_hashmap[key] = [idx]
            
            # check for repeat pattern
            all_indices = numbers_hashmap

            is_invalid = is_repeated_sequence(all_indices, len(str(num)))
   
            if is_invalid:
                invalid_ids.append(num)


    # print sum of invalid ids
    print(invalid_ids, sum(invalid_ids))
    
test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

findInvalidIDs(test_data)