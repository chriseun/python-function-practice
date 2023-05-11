def max_num(a, b, c):
  return max([a,b,c])


  print(max_num(1,3,5))

def mult_list(nums):
  result = 1

  for num in nums:
    result *= num

    return result

    my_list = [2,3,4,5]
    result = mult_list(my_list)
    print("the result of the list is:", result)


def rev_string(string):
  reversed_string = string[::-1]
  return reversed_string

  my_string = "hello"
  reversed_string = rev_string(my_string)
  print("The reversed string is:", reversed_string)


def num_within(num, low, high):
  if num >=low and num <=high:
    return True
  else:
    return False

    result1 = num_within(5, 1, 10)
    print("5 is within the range of 1-10:", result1)


def pascal(n):
  for i in range(n):
    row = [1] * (i +1)
    for j in range(1, i):
      row[j] = prev_row[j-1] + prev_row[j]
    prev_row = row
    print(row)

    pascal(5)
