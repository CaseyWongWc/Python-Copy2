try:
    total_avocados = int(input())
    avocados_requested = int(input())

    if total_avocados <= 0:
        raise ValueError("Number of avocados available must be positive")

    if avocados_requested < 0 or avocados_requested > total_avocados:
        raise ValueError("Number of avocados requested must be within range")

    avocados_remaining = total_avocados - avocados_requested
    print(f"Avocados remaining: {avocados_remaining}")
except ValueError as excpt:
    print(f"Error: {excpt}")
