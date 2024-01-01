import os


class Limit:
    limit: int

    @classmethod
    def set_limit(cls, x: int):
        cls.limit = x

    @classmethod
    def get_limit(cls):
        return cls.limit

'''
Message template for copy/paste:

Product {name} cannot be created. Maximum {Limit.get_limit()} products allowed
'''

class UserLimitExceeded(Exception):
    """write exception code"""
    def __init__(self, msg):
        raise(msg)


class Product:
    """write class implementation"""
    def __init__(self, name):
        self.name = name
        
    def __del__(self):
        

def main(path="/dev/stdout") -> None:
    max_limit = int(input())
    Limit.set_limit(max_limit)
    products = {}

    def new_product(product_name: str) -> str:
        product = Product(product_name)
        products[product_name] = product
        return f"{product.name} created"

    def del_product(product_name: str) -> str:
        product = products.get(product_name, f"{product_name} not found")
        if isinstance(product, Product):
            del products[product_name]
            return f"{product_name} deleted successfully"
        raise Exception(product)

    def print_product(product_name: str) -> str:
        product = products.get(product_name, f"{product_name} not found")
        if isinstance(product, Product):
            return f"{product.name} found"
        raise Exception(product)

    def change_limit(limit: int) -> str:
        limit = int(limit)
        Limit.set_limit(limit)
        return f"limit updated to {limit}"

    func_map = {
        "new": new_product,
        "del": del_product,
        "print": print_product,
        "limit": change_limit,
    }

    num_operations = int(input())

    for i in range(num_operations):
        cmd, arg = input().split()

        try:
            res = func_map[cmd](arg)
            print(res)
        except UserLimitExceeded as ule:
            print(ule)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    path = "/dev/stdout"
    if "OUTPUT_PATH" in os.environ.keys():
        path = os.environ["OUTPUT_PATH"]
    main(path=path)
