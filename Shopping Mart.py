def show_menu():
    '''
    Description: Prints the menu as shown in the PDF

    Parameters: No paramters

    Returns: No return value
    '''
    print('=' * 50)
    print('\t', '\t', '  MY BAZAAR')
    print('=' * 50)

    print('Hello! Welcome to my grocery store!')
    print('Following are the products available n the shop:')

    print('\n')
    print('-' * 50)
    print('CODE | DESCRIPTION |  CATEGORY    | COST (Rs)')
    print('-' * 50)
    print('  0  | Tshirt      | Apparels     | 500')
    print('  1  | Trousers    | Apparels     | 600')
    print('  2  | Scarf       | Apparels     | 250')
    print('  3  | Smartphone  | Electronics  | 20,000')
    print('  4  | iPad        | Electronics  | 30,000')
    print('  5  | Laptop      | Electronics  | 50,000')
    print('  6  | Eggs        | Eatables     | 5')
    print('  7  | Chocolate   | Eatables     | 10')
    print('  8  | Juice       | Eatables     | 100')
    print('  9  | Milk        | Eatables     | 45')
    print('-' * 50)


def choice():
    x = input("Would you like to buy in bulk? (y or Y / n or N): ")
    if x == 'n' or x == 'N':
        z = get_regular_input()
        return z
    elif x == 'y' or x == 'Y':
        z = get_bulk_input()
        return z
    else:
        input("Enter a valid input: ")
        return choice()


def get_bulk_input():
    print('\n')
    print('-' * 50)
    print("ENTER ITEM AND QUANTITIES")
    print('-' * 50)
    freqq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def bulk_input(freqq):
        dic = dict(
            {0: 'Tshirt', 1: 'Trousers', 2: 'Scarf', 3: 'Smartphone', 4: 'iPad', 5: 'Laptop', 6: 'Eggs', 7: 'Chocolate',
             8: 'Juice', 9: 'Milk'})

        x = input('Enter code and quantity (leave blank to stop):')

        if not x:
            print('Your order has been finalized.')
            return freqq
        elif int(x[0] + x[1]) not in range(0, 10):
            if x[3] == '-':
                print('Invalid code and quantity. Try again.')
                print('\n')
                return bulk_input(freqq)
            else:
                print('Invalid code. Try again.')
                print('\n')
                return bulk_input(freqq)
        elif x[2] == '-':
            print('Invalid quantity. Try again.')
            print('\n')
            return bulk_input(freqq)
        else:
            for i in range(0, 10):
                if i == int(x[0]):
                    freqq[i] += int(x[2:])
                    print(f'You added {x[2:]} {dic[i]}')
                    print('\n')
            return bulk_input(freqq)
    bulk_input(freqq)
    return freqq


def get_regular_input():
    print('\n')
    print('-' * 50)
    print('ENTER ITEMS YOU WISH TO BUY')
    print('-' * 50)

    def regular_input():
        q = input("Enter the item codes (space separated): ")
        i = 0
        mylist = []
        while i < len(q):
            if q[i] == ' ':
                i += 1
                pass
            elif q[i] == '-':
                i += 2
                print(f'The input {q[i - 2] + q[i - 1]} was invalid and so it is not considered')
                pass
            else:
                mylist.append(q[i])
                i += 1

        freq = []
        mylist2 = []

        for item in mylist:
            if item not in mylist2:
                mylist2.append(item)

        mylist2.sort()

        lst = []
        for item in mylist2:
            if item == ' ':
                pass
            else:
                lst.append(item)

        for a in lst:
            count = 0
            for b in mylist:
                if a == b:
                    count += 1

            freq.append(count)

        i = 0
        quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while i < len(lst):
            quantities[int(lst[i])] = freq[i]
            i += 1

        return quantities

    mylist = regular_input()
    return mylist


def print_order_details(mylist):
    print('\n')
    print('-' * 50)
    print('ORDER DETAILS')
    print('-' * 50)

    dic = dict({0: 500, 1: 600, 2: 250, 3: 20000, 4: 30000, 5: 50000, 6: 5, 7: 10, 8: 100, 9: 45})
    dic2 = dict(
        {0: 'Tshirt', 1: 'Trousers', 2: 'Scarf', 3: 'Smartphone', 4: 'iPad', 5: 'Laptop', 6: 'Eggs', 7: 'Chocolate',
         8: 'Juice', 9: 'Milk'})
    i = 0
    j = 0
    z = 1

    while i < 10:
        if mylist[j] != 0:
            print(f'{[z]} {dic2[i]} x {mylist[j]} = Rs {dic[i]} * {mylist[j]} = Rs {dic[i] * mylist[j]}')
            z += 1
            j += 1

        else:
            j += 1
        i += 1


def calculate_category_wise_cost(quantities):
    '''
    Description: Calculates the category wise cost using the quantities
    provided. Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: A 3-tuple of integers in the following format:
    (apparels_cost, electronics_cost, eatables_cost)
    '''
    print('\n')
    print('-' * 50)
    print('CATEGORY-WISE COST')
    print('-' * 50)

    dic = dict({0: 500, 1: 600, 2: 250, 3: 20000, 4: 30000, 5: 50000, 6: 5, 7: 10, 8: 100, 9: 45})
    i = 0
    app = 0
    while i < 3:
        app += (int(quantities[i]) * dic[i])
        i += 1

    i = 3
    elec = 0
    while i < 6:
        elec += (int(quantities[i] * dic[i]))
        i += 1

    i = 6
    eat = 0
    while i < 10:
        eat += (int(quantities[i] * dic[i]))
        i += 1

    if app != 0:
        print(f'Apparels = Rs {app}')
    if elec != 0:
        print(f'Electronics = Rs {elec}')
    if eat != 0:
        print(f'Eatables = Rs {eat}')

    return app, elec, eat


def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the discounted category-wise price, if applicable.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 3-tuple of integers in the following format:
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
    '''

    print('\n')
    print('-' * 50)
    print("DISCOUNTS")
    print('-' * 50)
    x = 0
    y = 0
    z = 0
    if apparels_cost >= 2000:
        x = get_discount(apparels_cost, 0.1)
        l = apparels_cost - x
        print(f'[APPAREL] Rs {apparels_cost} - Rs {x} = Rs {l}')
    else:
        l = apparels_cost

    if electronics_cost >= 25000:
        y = get_discount(electronics_cost, 0.1)
        m = electronics_cost - y
        print(f'[ELECTRONICS] Rs {electronics_cost}  - Rs {y} = Rs {m}')
    else:
        m = electronics_cost

    if eatables_cost >= 500:
        z = get_discount(eatables_cost, 0.1)
        n = eatables_cost - z
        print(f'[EATABLES] Rs {eatables_cost} - Rs {z} = Rs {n} ')
    else:
        n = eatables_cost

    print('\n')
    print(f'TOTAL DISCOUNT = Rs {x + y + z}')
    print(f'TOTAL COST = Rs {l + m + n}')

    calculate_tax(l, m, n)
    return l, m, n


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 2-tuple of integers in the following format:
    (total_cost_including_tax, total_tax)
    '''
    print('\n')
    print('-' * 50)
    print('TAX')
    print('-' * 50)
    x = get_tax(apparels_cost, 0.1)
    y = get_tax(electronics_cost, 0.15)
    z = get_tax(eatables_cost, 0.05)

    if apparels_cost != 0:
        print(f'[APPAREL] Rs {apparels_cost} * 0.10 = Rs {x}')
    if electronics_cost != 0:
        print(f'[ELECTRONICS] Rs {electronics_cost} * 0.15 = Rs {y}')
    if eatables_cost != 0:
        print(f'[EATBLES] Rs {eatables_cost} * 0.05 = Rs {z}')
    print('\n')
    print(f'TOTAL TAX = Rs {x + y + z}')
    k = apparels_cost + electronics_cost + eatables_cost + x + y + z
    print(f'TOTAL COST = Rs {k}')

    return k, x + y + z


def apply_coupon_code(total_cost):
    '''
    Description: Takes the coupon code from the user as input (case-sensitive).
    For details, refer the PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: The total cost (integer) on which the coupon is to be applied.

    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''
    print('\n')
    print('-' * 50)
    print('COUPON CODE')
    print('-' * 50)

    def coupon_input(total_cost):
        x = input('Enter coupon code (else leave blank):')
        if x == 'HELLE25' or x == 'CHILL50':
            return x
        elif not x:
            print('No coupon code applied.')
            print('\n')
            print(f'TOTAL COUPON DISCOUNT = Rs 0')
            print(f'TOTAL COST = Rs {total_cost}')
            return
        else:
            print('Invalid coupon code. Try again.')
            print('\n')
            return coupon_input(total_cost)
    x = coupon_input(total_cost)
    a = 0
    if x == 'HELLE25':

        if total_cost >= 25000:
            a = min(5000, total_cost * 0.25)
            print(f'[HELLE25] min(5000, Rs {total_cost} * 0.25) = Rs {a}')
            print('\n')
            print(f'TOTAL COUPON DISCOUNT = Rs {a}')
            print(f'TOTAL COST = Rs {total_cost - a}')
        else:
            print('The coupon code is invalid since the total amount is less than 25,000')
            a = 0

    elif x == 'CHILL50':

        if total_cost >= 50000:
            a = min(10000, total_cost * 0.50)
            print(f'[CHILL50] min(10000, Rs {total_cost} * 0.50) = Rs {a}')
            print('\n')
            print(f'TOTAL COUPON DISCOUNT = Rs {a}')
            print(f'TOTAL COST = Rs {total_cost - a}')
        else:
            print('The coupon code is invalid since the amount is less than 50,000')
            a = 0
    y = total_cost - a
    print('\n')
    print('Thank you for visiting!')
    return y, a


def main():
    '''
    Description: This is the main function. All production level codes usually
    have this function. This function will call the functions you have written
    above to design the logic. You will see how splitting your code into specialised
    functions makes the code easier to read, write and debug. Include appropriate
    print statements to match the output with the screenshots provided in the PDF.

    Parameters: No parameters

    Returns: No return value
    '''
    show_menu()
    x = choice()
    print_order_details(x)
    y = calculate_category_wise_cost(x)
    z = calculate_discounted_prices(y[0], y[1], y[2])
    w = calculate_tax(z[0], z[1], z[2])
    b = apply_coupon_code(w[0])


if __name__ == '__main__':
    main()
