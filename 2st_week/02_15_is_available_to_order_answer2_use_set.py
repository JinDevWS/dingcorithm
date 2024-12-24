# 이 문제는 단순히 특정한 문자열이 배열에 존재하는지만 확인하면 됩니다!

# 정렬을 할 필요없이, 집합 자료형을 사용하면 쉽게 해결할 수 있습니다.

# * 집합은 중복을 허용하지 않는 자료형입니다.

# 알고리즘은 항상 효율적인 것이 없다. 모든 상황에 항상 효율적인 알고리즘이란 없기 때문에,
# 적재적소에 맞는 도구를 선택하는 것이 중요하다.



shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    # O(N) + O(M) + O(1) =  O(N+M)

    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order not in menus_set: # O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)