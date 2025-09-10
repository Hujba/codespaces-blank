
# Dictionary of menu items and their prices
beef_burgers = {
    'Bun': 0.99,
    'Beef patty': 3.59,
    'Gluten free bun': 1.59,
    'Cheese': 0.59,
    'Lettuce': 0.29,
    'Tomato': 0.39,
    'Onion': 0.19,
    'Pickles': 0.19,
    'Ketchup': 0.09,
    'Mustard': 0.09,

}
meal_deals = {
    'Beef burger meal': 7.99,
    'Cheeseburger meal': 8.49,
    'Veggie burger meal': 7.49
}

# Lists to store the user's order and corresponding prices
total_order = []
total_order_prices = []

# Function to display the menu options
def menu():
    print('--- Beef Burger Menu ---')
    print(f"1. Bun for ${beef_burgers['Bun']}")
    print(f"2. Beef patty for ${beef_burgers['Beef patty']}")
    print(f"3. Gluten free bun for ${beef_burgers['Gluten free bun']}")
    print(f"4. Cheese for ${beef_burgers['Cheese']}")
    print(f"5. Lettuce for ${beef_burgers['Lettuce']}")
    print(f"6. Tomato for ${beef_burgers['Tomato']}")
    print(f"7. Onion for ${beef_burgers['Onion']}")
    print(f"8. Pickles for ${beef_burgers['Pickles']}")
    print(f"9. Ketchup for ${beef_burgers['Ketchup']}")
    print(f"10. Mustard for ${beef_burgers['Mustard']}")
    print('11. Go to checkout.')



# Function to take the customer's order and update order lists
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
        total_order.append('Cheese')
        total_order_prices.append(beef_burgers['Cheese'])
    elif order == 5:
        total_order.append('Lettuce')
        total_order_prices.append(beef_burgers['Lettuce'])
    elif order == 6:
        total_order.append('Tomato')
        total_order_prices.append(beef_burgers['Tomato'])
    elif order == 7:
        total_order.append('Onion')
        total_order_prices.append(beef_burgers['Onion'])
    elif order == 8:
        total_order.append('Pickles')
        total_order_prices.append(beef_burgers['Pickles'])
    elif order == 9:
        total_order.append('Ketchup')
        total_order_prices.append(beef_burgers['Ketchup'])
    elif order == 10:
        total_order.append('Mustard')
        total_order_prices.append(beef_burgers['Mustard'])
    elif order == 11:
        total_order.append('__CHECKOUT__')  # Special marker to signal checkout
    else:
        print('Invalid selection. Please try again.')
        customer_order()


# Function to display the order summary and total price
def check_out():
    print('\n--- Your Order Summary ---')
    # Remove the checkout marker if present
    order_items = [item for item in total_order if item != '__CHECKOUT__']
    if not order_items:
        print('No items ordered.')
        return
    print('Items in your order:')
    for item in order_items:
        print(f'- {item} (${beef_burgers[item]:.2f})')
    total = sum(total_order_prices)
    print(f'Total price: ${total:.2f}')

print('Welcome to the Beef Burger Co. menu!')
meal_deal = input("Would you like a meal deal? (yes/no)")
if meal_deal == 'yes':
    print('--- Meal Deals ---')
    for deal, price in meal_deals.items():
        print(f'{deal} for ${price}')
    selected_deal = input('Please enter the name of the meal deal you want: ')
    if selected_deal in meal_deals:
        total_order.append(selected_deal)
        total_order_prices.append(meal_deals[selected_deal])
        print(f'Added {selected_deal} to your order.')
    else:
        print('Invalid meal deal selection. Proceeding without a meal deal.')

while True:
    menu()
    customer_order()
    # Break the loop if checkout is selected
    if len(total_order) > 0 and total_order[-1] == '__CHECKOUT__':
        break
check_out()