try:
    raise ValueError("This is a ValueError.")
except NameError:
    print("NameError exception caught.")
except (ValueError, NameError) as excpt:
    print(f"ValueError or NameError exception caught: {excpt}")
except:
    print("An exception was caught.")
