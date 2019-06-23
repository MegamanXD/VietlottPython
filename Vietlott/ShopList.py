# Add/edit/delete/view a list of Vietlott shops.
# Shop: code, address, owner, phone, email, account balance (money deposit - money issuing lottery)


class Shop:
    def __init__(self, code: str, address: str, owner: str, phone: str, email: str, account_balance: float):
        self.code = code
        self.address = address
        self.owner = owner
        self.phone = phone
        self.email = email
        self.account_balance = account_balance

    def __str__(self):
        return "Code: {}, Address: {}, Owner: {}, Phone: {}, Email: {}, Account balance: {}\n"\
            .format(self.code, self.address, self.owner, self.phone, self.email, self.account_balance)

    def __repr__(self):
        return "Shop({}, {}, {}, {}, {}, {})\n"\
            .format(self.code, self.address, self.owner, self.phone, self.email, self.account_balance)

    # ----------------------------------------------------------------------------------------------------------
    @staticmethod
    def input_shop_details():
        code = input("Shop code: ")
        address = input("Shop address: ")
        owner = input("Shop owner: ")
        phone = input("Shop phone: ")
        email = input("Shop email: ")
        try:
            account_balance = float(input("Shop account balance: "))
            return Shop(code, address, owner, phone, email, account_balance)
        except ValueError:
            print("\nInvalid! Balance must be a number")
            return None
# ----------------------------------------------------------------------------------------------------------


class ShopList:
    def __init__(self):
        self.shop_list = []

    def __str__(self):
        if len(self.shop_list) == 0:
            return "Haven't seen any shop around here :)"
        else:
            string = "\nShop List:\n"
            for i in range(0, len(self.shop_list)):
                string += "Shop {} -> {}".format(i, self.shop_list[i])
            return string

    def __len__(self):
        return len(self.shop_list)

    # ShopList CRUD
    def add_shop(self, shop: Shop):
        if shop is None:
            print("Can't add an invalid shop!")
            return
        else:
            self.shop_list.append(shop)

    def delete_shop(self, index: int):
        if len(self.shop_list) == 0:
            print("There's nothing to delete! :)")
            return
        else:
            try:
                del self.shop_list[index]
            except IndexError:
                print("Invalid index! Please check!\nData: unchanged")
                return

    def update_shop(self, shop: Shop, index: int):
        if shop is None:
            print("Inputted shop is invalid! Data: unchanged")
            return
        else:
            try:
                self.shop_list[index] = shop
            except IndexError:
                print("Invalid index! Please check!\nData: unchanged")
                return
