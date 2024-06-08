def jia(*numbers):
    return sum(numbers)
def jian(*numbers):
    return numbers[0] - sum(numbers[1:])
def cheng(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
def chu(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result
def cifang(base,exponent):
 result = base ** exponent
 return result
def zuidazhi(*numbers):
  return max(numbers)
def zuixiaozhi(*numbers):
  return min(numbers)
def pingjunzhi(*numbers):
  return sum(numbers)
result = pingjunzhi(8, 4) 
print(result)