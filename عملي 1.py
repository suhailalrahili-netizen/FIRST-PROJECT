order_num = int(input("Enter order: "))
binary = format(order_num, '08b')

temp_bit    = binary[0]
size_bit    = binary[1]
sugar_bits  = binary[2:4]
milk_bit    = binary[4]
ice_bit     = binary[5]
drink_bits  = binary[6:8]

temp = "Hot" if temp_bit == "1" else "Cold"
size = "Large" if size_bit == "1" else "Small"

match sugar_bits:
    case "00": sugar = "No Sugar"
    case "01": sugar = "Low Sugar"
    case "10": sugar = "Medium Sugar"
    case "11": sugar = "Extra Sugar"

milk = "With Milk" if milk_bit == "1" else "No Milk"
ice  = "With Ice" if ice_bit == "1" else "No Ice"

match drink_bits:
    case "00": drink = "Tea"
    case "01": drink = "Coffee"
    case "10": drink = "Water"
    case "11": drink = "Mint"


print(f"Order: {temp} {drink} | Size: {size}")
print(f"Extras: {sugar}, {milk}, {ice}")
print(f"Binary: {binary}")