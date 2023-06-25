def or_or_f6(first_value, second_value):
    return (not first_value and second_value) or (not second_value and first_value)


def and_and_f9(first_value, second_value):
    return (first_value and second_value) or (not second_value and not first_value)


def no_f4(first_value, second_value):
    return not first_value and second_value


def no_not_f11(first_value, second_value):
    return first_value or not second_value


def operation_f4(first_value, second_value):
    result = []
    for x in range(len(first_value)):
        result.append(int(no_f4(first_value[x], second_value[x])))
    return result


def operation_f6(first_value, second_value):
    result = []
    for x in range(len(first_value)):
        result.append(int(or_or_f6(first_value[x], second_value[x])))
    return result


def operation_f9(first_value, second_value):
    result = []
    for x in range(len(first_value)):
        result.append(int(and_and_f9(first_value[x], second_value[x])))
    return result


def operation_f11(first_value, second_value):
    result = []
    for x in range(len(first_value)):
        result.append(int(no_not_f11(first_value[x], second_value[x])))
    return result
