from math import sin, pow
import random

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


def four_digit_number_of_the_offender():
   common_divisor = 2 * 7 * 11
   
   start = 1000 // common_divisor
   if 1000 % common_divisor != 0:
       start += 1
   
   end = 9999 // common_divisor

   for multiplier in range(start, end + 1):
      number = common_divisor * multiplier
      s_number = str(number)
      
      unique_digits = []
      for char in s_number:
         current_digit = int(char)
         is_distinct = True
         for existing_digit in unique_digits:
            if current_digit == existing_digit:
               is_distinct = False
               break
         if is_distinct:
            unique_digits.append(current_digit)
      
      if len(unique_digits) != 2:
         continue
      
      digit_sum = 0
      for char in s_number:
         digit_sum += int(char)
      
      if digit_sum != 30:
         continue
      
      return number
      
   return None


def counter_words_starting_with_A(text):
 
 text = text.lower()
 words = text.split()
 count_of_words = 0

 for word in words:
     if word.startswith('a') or word.startswith('A') or word.startswith('а') or word.startswith('А'):
      count_of_words +=1

 return count_of_words

def truth_table():
    rows = [] 
    
    header = ["A", "B", "C", "A ИЛИ B", "НЕ(A ИЛИ B)", "A Экв. C", "НЕ(A ИЛИ B) & (A Экв. C)"]
    rows.append(header)

    for a in range(0, 2):
        for b in range(0, 2):
            for c in range(0, 2):
                
                a_bool = bool(a)
                b_bool = bool(b)
                c_bool = bool(c)

                a_or_b_val = a_bool or b_bool
                not_a_or_b_val = not a_or_b_val
                a_xor_c_val = a_bool != c_bool 

                final_function_val = not_a_or_b_val and a_xor_c_val

                rows.append([
                    a,  
                    b,
                    c,
                    int(a_or_b_val),         
                    int(not_a_or_b_val),
                    int(a_xor_c_val),
                    int(final_function_val)
                ])
    column_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]

    for i, header_item in enumerate(rows[0]):
        print(f"{header_item:<{column_widths[i]}}", end="  ")
    print()

    for row in rows[1:]:
        for i, item in enumerate(row):
            print(f"{item:<{column_widths[i]}}", end="  ")
        print()


def formatting_array_to_matrix(S):
 first_row = []
 second_row = []

 for i in range(len(S)):
   if i % 2 == 0:
     first_row.append(S[i])
   else: 
     second_row.append(S[i])

 return [first_row, second_row]


def format_array_from_array():
 
 array_A = []
 array_Y = []

 for i in range(75):
    array_A.append(random.randint(-5,40))
   
 for num in array_A:
    if num < 20:
       array_Y.append(num)

 return array_A, array_Y


def checker_equivalence_of_numeric_and_text_values(text_of_numbers_and_letters):
 digit_sum = 0
 for char in text_of_numbers_and_letters:
   if char.isdigit():
     digit_sum += int(char)
 return digit_sum == len(text_of_numbers_and_letters)

def matrix_formation(M):
 square_matrix = []
 for row in range(M):
    current_row = []
    for col in range(M):
       if col > row:
          current_row.append(0)
       else:
          current_row.append(row - col + 1)
    square_matrix.append(current_row)
 return square_matrix

def search_for_isolated_cities(N, connectivity_matrix):

    isolated_cities = []

    for i in range(N): 
        is_isolated = True
        for j in range(N):
            if i == j: 
                continue
            if connectivity_matrix[i][j] == 1 or connectivity_matrix[j][i] == 1:
                is_isolated = False 
                break 
        
        if is_isolated:
            isolated_cities.append(i + 1) 
            
    return isolated_cities
