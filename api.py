import requests

def get_Data(limit: int) -> dict:
    """Get data about x number of objects.
    Keyword arguments:
    limit:int - x
    Return:dict - JSON data
    """
    url = "https://fakestoreapi.com/products"
    params = {"limit": limit}
    response = requests.get(f"{url}", params)
    return (response.json())

import requests

BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "category": 'electronic'
}

response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())


# if __name__ == '__main__':
#    # url = "https://fakestoreapi.com/products"
#    # x = int(input("Enter x "))
#    # params = {"limit": x}
#    # response = requests.get(f"{url}", params)
#    # print(response.json())
#    x = int(input("Enter x"))
#    data = str(get_Data(x))
#    print(data)
