def raise_to_power(base_val, exponent_val):
    if exponent_val == 0:
        result_val = 1
    else:
        result_val = base_val * raise_to_power(base_val, exponent_val - 1)
    
    return result_val
    
user_base = int(input())
user_exponent = int(input())
print(f"{user_base}^{user_exponent} = {raise_to_power(user_base, user_exponent)}")
