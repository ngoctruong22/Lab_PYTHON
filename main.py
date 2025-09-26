# Функция, которую будем тестировать
def twoSum(nums, target):
<<<<<<< HEAD
    # Проверка, что все элементы являются целыми числами
=======
    # push github
    if not nums:
        return None
>>>>>>> 3f4694486348720836c5d2585a331ca606c3b1ef
    if not all(isinstance(num, int) for num in nums):
        return None

    # Основной алгоритм поиска индексов
    for i in range(len(nums)):
        # Внутренний цикл начинается со следующего элемента
        for j in range(i + 1, len(nums)):
            # Проверяем, равна ли сумма целевому значению
            if nums[i] + nums[j] == target:
                # Возвращаем индексы элементов
                return [i, j]