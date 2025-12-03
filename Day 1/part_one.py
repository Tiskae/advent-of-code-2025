# rotations: list e.g ["L5", "R20",...]
def crackPuzzle(rotations):
    num_of_zeros = 0
    pointer = 50
    
    # logic
    # loop through rotations
    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])
        
        # left rotation
        if direction == "L":
            new_pointer = pointer - (clicks % 100)
            pointer = new_pointer if new_pointer >= 0 else 100 + new_pointer
            
        # right rotation
        if direction == "R":
            new_pointer = pointer + (clicks % 100)
            pointer = new_pointer if new_pointer < 100 else new_pointer % 100
            
        if pointer == 0:
            num_of_zeros += 1
    
    print(num_of_zeros)

test_rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

crackPuzzle(test_rotations)