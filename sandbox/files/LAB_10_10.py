try:
    user_num = int(input())
    div_num = int(input())
    print(user_num // div_num)
except ZeroDivisionError as excpt:
    print(f"Zero Division Exception: {excpt}")
except ValueError as excpt:
    print(f"Input Exception: {excpt}")
