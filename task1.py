from typing import List, Tuple


def find_min_max(numbers: List[float]) -> Tuple[float, float]:
    """
    Пошук мінімуму та максимуму масиву методом «розділяй і володарюй».

    Args:
        numbers: масив чисел довільної довжини

    Returns:
        Кортеж (мінімум, максимум)
    """
    if not numbers:
        raise ValueError("Масив не може бути порожнім")

    def divide(low: int, high: int) -> Tuple[float, float]:
        # базові випадки: один або два елементи
        if low == high:
            return numbers[low], numbers[low]
        if high - low == 1:
            a, b = numbers[low], numbers[high]
            return (a, b) if a < b else (b, a)

        # ділимо навпіл і об'єднуємо результати підмасивів
        mid = (low + high) // 2
        left_min, left_max = divide(low, mid)
        right_min, right_max = divide(mid + 1, high)
        return min(left_min, right_min), max(left_max, right_max)

    return divide(0, len(numbers) - 1)


if __name__ == "__main__":
    test_cases = [
        [3, 7, 2, 9, 1, 5, 8, 4],
        [-10, -3, -25, -7, -1],
        [42],
        [5, 5, 5, 5],
        [1.5, -2.3, 8.8, 0.0, 4.1],
    ]

    for arr in test_cases:
        minimum, maximum = find_min_max(arr)
        print(f"Масив: {arr}")
        print(f"Мінімум: {minimum}, Максимум: {maximum}")
        assert (minimum, maximum) == (min(arr), max(arr))
        print()
