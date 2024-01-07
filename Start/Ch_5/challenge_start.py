# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# TODO: process each order
for ord in test_orders:
    ord_amt = 0
    print('------------------')
    for line in ord:
        garment = line[0]
        line_price = 0
        match garment:
            case 'shirt' | 'pants' | 'jacket' | 'dress':
                laundry_type = 'Dry Clean'
                size = line[1]
                starch = line[2]
                starch_desc = (lambda x: 'Starched' if x else '')(starch)
                starch_price = (lambda x: 2 if x else 0)(starch)
                same_day = line[3]
                same_day_price = (lambda x: 10 if x else 0)(same_day)
                same_day_desc = (lambda x: 'same-day' if x else '')(same_day)
                line_price = 12.95 + starch_price + same_day_price
                line_desc = f"{laundry_type}: ({size}) {garment} {starch_desc} {same_day_desc}"
            case 'comforter' | 'cover':
                laundry_type = 'Blanket'
                dry_clean = line[1]
                dry_clean_desc = (lambda x: 'Dry clean' if x else '')(dry_clean)
                size = line[2]
                line_price = 25
                line_desc = f"{laundry_type}: ({size}) {garment} {dry_clean_desc}"    
            case _:
                laundry_type = 'Wash/Fold'
                weight = line[1]
                init_price = 4.95 * weight
                line_price = (lambda x: (4.95 * x)*(0.9) if (x > 15) else (4.95 * x))(weight)
                line_desc = f"{laundry_type}: {garment}, {weight}"
        ord_amt = ord_amt + line_price
        print(line_desc)
    print(f"Order total: ${round(ord_amt, 2):.2f}")
    print('------------------')
