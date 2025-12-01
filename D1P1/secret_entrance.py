def get_secret(sol: list[int]) -> int:
    position = 50
    secret_code = 0

    for command in sol:
        dir, turns = (command[0], int(command[1:]))

        if dir == "R":
            new_position = position + turns %100
            position = new_position if new_position <= 99 else new_position % 100

        else:
            new_position = (position - turns)%100
            position = new_position if new_position >= 0  else 99-new_position+1

        if position == 0:
            secret_code += 1

    print(secret_code)

f = open("input.txt")

get_secret(f.read().split())