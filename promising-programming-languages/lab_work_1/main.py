from math import sin, pow

def function_evaluation():
   all_values = []
   x = 0.0
   step =  0.1

   while x < 1.2:
      function_value = sin(x) + pow((sin(pow(x,2))),2) + pow((sin(pow(x,3))),3)
      all_values.append((x, function_value))
      x+=step
      
   return all_values

def sum_of_the_k_lowest_digits(N, k):
   if not isinstance(N, int) or not isinstance(k, int) or N < 0:
      return 'я могу принимать только натуральные числа'
   if k == 0:
      return 0
   
   N = str(N)
   sum = 0
   
   if len(N) <= k:
      for i in N:
         sum += int(i)
      return sum
   
   k_lowest_digits = N[-k:]
   
   for i in k_lowest_digits:
      sum += int(i)
   return sum

# def four_digit_number_of_the_offender(dividers, differences, sum):
#  return number

# def counter_words_starting_with_A(text):
#  return count_of_words

# def truth_table(a, b, c):
#  return table

# def formatting_array_to_matrix(S[]):
#  return formatted_matrix

# def format_array_from_array(A[]):
#  return matrix_A, matrix_Y

# def checker_equivalence_of_numeric_and_text_values(text_of_numbers_and_letters):
#  pass # i think that tut mozhno true or false

# def matrix_formation(M):
#  return square_matrix

# def search_for_isolated_cities(N):
#  return count_isolated_cities