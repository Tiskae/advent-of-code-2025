def getLargestJoltages(banks):
    joltages = []

    for bank in banks:
        bank_arr = list(str(bank))
        joltage_arr = [bank_arr[0]]
        first_idx = 0

        # get the first value
        for idx, i in enumerate(bank_arr[:-11]):
            if idx == 0:
                continue

            if int(i) > int(joltage_arr[0]):
                joltage_arr[0] = str(i)
                first_idx = idx

        # when there is no freedom of choice left
        if first_idx == len(bank_arr) - 12:
            joltages.append(int("".join(bank_arr[first_idx:])))
            continue 

        # get the remaining 11 values
        prev_idx = first_idx

        for i in range(11):
            start = prev_idx + 1
            stop = len(bank_arr) - 10 + i

            joltage_arr.append(str(bank_arr[start]))
            prev_idx += 1

            for idx, j in enumerate(bank_arr[start: stop]):
                if int(j) > int(joltage_arr[i + 1]):
                    joltage_arr[i + 1] = j
                    prev_idx = start + idx

        # append final joltage
        joltages.append(int("".join(joltage_arr)))

    print(f"sum: {(joltages)}")

test_data = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
# answer: [987654321111 + 811111111119 + 434234234278 + 888911112111] = 3121910778619

getLargestJoltages(test_data)