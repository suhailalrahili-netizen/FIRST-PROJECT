teams = [
    "Al-Ittihad", "Al-Nassr", "Al-Hilal", "Al-Ahli",
    "Al-Qadsiah", "Al-Taawoun", "Al-Ettifaq", "Neom",
    "Al-Hazem", "Al-Fayha", "Al-Shabab", "Al-Kholood",
    "Damac", "Al-Riyadh", "Al-Okhdood", "Al-Wahda",
    "Al-Fateh", "Al-Khaleej"
]

while True:
    user_input = input("Enter match code :")

    if user_input.lower() == 'q':
        print("Program ended.")
        break

    try:
        if user_input.startswith("0b"):
            match_num = int(user_input, 2)
        elif user_input.startswith("0x"):
            match_num = int(user_input, 16)
        elif any(c in "ABCDEFabcdef" for c in user_input):
            match_num = int(user_input, 16)
        else:
            match_num = int(user_input)

    except ValueError:
        print("Invalid input")
        continue

    binary = format(match_num, '018b')
    hexa = format(match_num, '05X')

    referee_bit = binary[0]
    tourney_bits = binary[1:3]
    stadium_bit = binary[3]
    status_bits = binary[4:8]
    team_b_bits = binary[8:13]
    team_a_bits = binary[13:18]

    idx_a = int(team_a_bits, 2)
    idx_b = int(team_b_bits, 2)

    if idx_a >= len(teams) or idx_b >= len(teams):
        print("Error: No team found")
        continue

    if idx_a == idx_b:
        print("Error: A team cannot play against itself")
        continue

    t_a = teams[idx_a]
    t_b = teams[idx_b]

    match referee_bit:
        case "0": referee = "Local"
        case "1": referee = "Foreign"

    match stadium_bit:
        case "0": stadium = f"{t_a} Stadium"
        case "1": stadium = f"{t_b} Stadium"

    match tourney_bits:
        case "00": tourn = "Saudi Pro League"
        case "01": tourn = "King's Cup"
        case "10": tourn = "Saudi Super Cup"
        case "11": tourn = "Crown Prince Cup"

    match status_bits:
        case "0001": status = f"{t_a} Won"
        case "0010": status = f"{t_b} Won"
        case "0100": status = "Draw"
        case "1000": status = "Postponed"
        case _: status = "Pending"

    print("\n--- Match Info ---")
    print(f"Match: {t_a} vs {t_b}")
    print(f"Tournament: {tourn} | Status: {status}")
    print(f"Stadium: {stadium} | Referee: {referee}")
    print(f"Binary: {binary} | Decimal: {match_num} | Hex: {hexa}")