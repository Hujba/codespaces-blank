beef_burgers = {
    'Bun': 0.99, 'Beef patty': 1.59, 'Gluten free bun': 3.59
}

total_order = []          
total_order_prices = []   


def menu():
    print('--- Beef Burger Menu ---')
    print(f"1. Bun for ${beef_burgers['Bun']}")
    print(f"2. Beef patty for ${beef_burgers['Beef patty']}.")
    print(f"3. Gluten free bun for ${beef_burgers['Gluten free bun']}")
    print('4. Go to checkout.')


def customer_order():
    orderstr = input('Select what you would like to order: ')
    order = int(orderstr)
    if order == 1:
        total_order.append('Bun')
        total_order_prices.append(beef_burgers['Bun'])
    elif order == 2:
        total_order.append('Beef patty')
        total_order_prices.append(beef_burgers['Beef patty'])
    elif order == 3:
        total_order.append('Gluten free bun')
        total_order_prices.append(beef_burgers['Gluten free bun'])
    elif order == 4:
        total_order.append('__CHECKOUT__')  # Signal to break main loop
    else:
        print('Invalid selection. Please try again.')
        customer_order()

def check_out():
    print('\n--- Your Order Summary ---')
    print(total_order_prices)

print('Welcome to the Beef Burger Co. menu!')

while True:
    menu()
    customer_order()
    if len(total_order) > 0 and total_order[-1] == '__CHECKOUT__':
        break
check_out()