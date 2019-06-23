from Vietlott import CustomerList, Lottery, ShopList
jackpot = {}

def perform_option(option: int, customer_list: CustomerList.CustomerList, shop_list: ShopList.ShopList):
    # Add customer
    if option == 1:
        new_customer = CustomerList.Customer.input_customer_details()
        customer_list.add_customer(new_customer)
        print(customer_list)

    # Delete customer
    elif option == 2:
        print(customer_list)
        if len(customer_list) == 0:
            return
        else:
            try:
                delete_customer_index = int(input("Which customer to delete (0 - {}): ".format(len(customer_list)-1)))
                customer_list.delete_customer(delete_customer_index)
            except ValueError:
                print("Invalid input! Please enter a number!")
            finally:
                print(customer_list)

    # Update customer
    elif option == 3:
        print(customer_list)
        if len(customer_list) == 0:
            return
        else:
            try:
                update_customer_index = int(input("Which customer do you want to update (0 - {}): "
                                                  .format(len(customer_list)-1)))
                updated_customer = CustomerList.Customer.input_customer_details()
                customer_list.update_customer(updated_customer, update_customer_index)
            except ValueError:
                print("Invalid input! Please enter a number!")
            finally:
                print(customer_list)

    # View customer list
    elif option == 4:
        print(customer_list)
    # -------------------------------------------------------------------------------------------------------------
    # Add shop
    elif option == 5:
        new_shop = ShopList.Shop.input_shop_details()
        shop_list.add_shop(new_shop)
        print(shop_list)

    # Delete shop
    elif option == 6:
        print(shop_list)
        if len(shop_list) == 0:
            return
        else:
            try:
                delete_shop_index = int(input("Which shop to delete (0 - {}): ".format(len(shop_list)-1)))
                shop_list.delete_shop(delete_shop_index)
            except ValueError:
                print("Invalid input! Please enter a number!")
            finally:
                print(shop_list)

    # Update shop
    elif option == 7:
        print(shop_list)
        if len(shop_list) == 0:
            return
        else:
            try:
                update_shop_index = int(input("Which shop to update (0 - {}): ".format(len(shop_list)-1)))
                updated_shop = ShopList.Shop.input_shop_details()
                shop_list.update_shop(updated_shop, update_shop_index)
            except ValueError:
                print("Invalid input! Please enter a number!")
            finally:
                print(shop_list)

    # View shop list
    elif option == 8:
        print(shop_list)
    # -------------------------------------------------------------------------------------------------------------
    # Draw jackpot
    elif option == 9:
        global jackpot
        jackpot = Lottery.draw_jackpot()
        print("Jackpot is: {}".format(jackpot))

    # Buy until obtained jackpot
    elif option == 10:
        Lottery.buy_till_jackpot(jackpot)

    # 5 times average of jackpot buying
    elif option == 11:
        Lottery.five_time_average(jackpot)
    # -------------------------------------------------------------------------------------------------------------
    # Quit program
    elif option == 12:
        pass

    # Default case
    else:
        print("Please enter a number from 1 to 12 only!")
