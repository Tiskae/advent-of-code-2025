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
        
        for i in range(start, end + 1):
            if len(str(i)) % 2 == 1:
                continue

            middle = len(str(i)) // 2
            first_half = str(i)[:middle]
            second_half = str(i)[middle:]

            if first_half != second_half:
                continue

            invalid_ids.append(i)

    # print sum of invalid ids
    print(sum(invalid_ids))
    
test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

findInvalidIDs(test_data)