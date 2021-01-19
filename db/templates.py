from db.models import User, Product, Category, Cart, session


class UserActivity:
    """
     Users should be able to view the list of multiple categories.
    - Users should be able to view all the products under a particular category.
    - Users should be able to view product details.
    - Users should be able to add products to Cart.
    - Users should be able to buy multiple products from the Cart.
    - Users should be able to remove products from the Cart.
    - If the final billing amount is greater than Rs 10,000 then Rs 500 OFF should be given to the user.
    - If the final billing amount is less than Rs 10,000 then no discount should be given to the user.
    - Bill should be generated for multiple product purchases showing the actual amount, discounted
    amount, and the final amount.

    """

    def __init__(self):
        pass

    def get_all_category(self):
        cats = session.query(Category).all()
        print()
        print("---------Categories----------")
        for cat in cats:
            print(cat)
        print("----------------------------")
        print()

    def get_products_by_category(self, category):
        category = session.query(Category).filter(Category.name == category).one()
        print()
        print("----------Products-----------")
        print(category.products)
        print("----------------------------")
        print()

    def get_product(self, name):
        product = session.query(Product).filter(Product.name == name).one()
        print()
        print("-------Product details------")
        print(product.name)
        print(product.description)
        print(product.price)
        print("----------------------------")
        print()


    def add_to_cart(self, product_id):
        cart = session.query(Product)
        session.add(cart)
        session.commit()

    def remove_product(self, product_id):
        product = session.query(Product).get(product_id)
        session.delete(product)

    def update_product(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description


class AdminActivity:
    """
    Admin should be able to add categories and products.
    - Admin should be able to see details of the products added to the cart by the user.
    - Admin should be able to see all the bills generated by all the users.
    """

    def __init__(self):
        pass

    def add_category(self, name):
        category = Category(name=name)
        session.add(category)
        session.commit()

    def get_cart(self):
        pass

    def get_bills(self):
        pass


class UserCart:

    def __init__(self):
        pass

    def add_product(self):
        pass

    def remove_product(self):
        pass


ua = UserActivity()
# print(ua.get_all_category())