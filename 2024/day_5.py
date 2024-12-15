input_data = open("data/input_day_5.txt", "r").read().split("\n\n")

instructions = input_data[0].splitlines()
instruct_1 = [int(x.split("|")[0]) for x in instructions]
instruct_2 = [int(x.split("|")[1]) for x in instructions]

orders = input_data[1].splitlines()
orders = [x.split(",") for x in orders]
orders = [[int(x) for x in order] for order in orders]

middle_page_sum = 0
orders_failed = []

for order in orders:

    test_count = 0
    test_pass = 0

    if len(order) != len(set(order)):
        print("Duplicate order numbers in order - cannot test order")
        break

    else:
        for n1, n2 in zip(instruct_1, instruct_2):
            if n1 in order and n2 in order:
                test_count += 1
                if order.index(n1) < order.index(n2):
                    test_pass += 1

        if test_count == test_pass:
            # orders_passed.append(order)
            middle_page_sum += order[int((len(order) - 1) / 2)]

        else:
            orders_failed.append(order)

print(f"Sum of middle page for orders which passsed testing is {middle_page_sum}")


def apply_instructions(order: list, instruct_1, instruct_2):

    for n1, n2 in zip(instruct_1, instruct_2):
        if n1 in order and n2 in order:
            if order.index(n1) > order.index(n2):
                order.remove(n2)
                order.insert(order.index(n1) + 1, n2)
                apply_instructions(order, instruct_1, instruct_2)

    return order


middle_page_sum = 0
orders_fixed = []
for order in orders_failed:
    order_fixed = apply_instructions(order, instruct_1, instruct_2)
    middle_page_sum += order_fixed[int((len(order_fixed) - 1) / 2)]

print(f"Sum of middle page for orders which have been fixed is {middle_page_sum}")
