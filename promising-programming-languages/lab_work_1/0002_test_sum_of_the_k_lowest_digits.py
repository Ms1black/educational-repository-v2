import pytest
from main import sum_of_the_k_lowest_digits 


@pytest.mark.parametrize("N_input, k_input, expected_result", [
    (12345, 2, 9),    
    (987, 3, 24),         
    (100, 1, 0),      
    (5, 1, 5),           
    (123, 5, 6),     
    (7, 3, 7),           
    (0, 1, 0),           
    (0, 5, 0),            
    ("12345", "2", 9), 
    ("0", "1", 0),
    (1, 1, 1),
    (1, 10, 1),
    (987654321, 5, 15)    
])
def test_correct_inputs(N_input, k_input, expected_result):
    assert sum_of_the_k_lowest_digits(N_input, k_input) == expected_result

@pytest.mark.parametrize("N_input, k_input, expected_error_message", [
    (123, 0, 0),                              
    (123, -1, 0),                            
    ("456", "-5", 0),                         
    (123, 3.14, "Ошибка: k должно быть целым числом."),    
    (123, "text", "Ошибка: k должно быть целым числом."),   
    ("789", None, "Ошибка: k должно быть целым числом."),   
    (123, [1, 2], "Ошибка: k должно быть целым числом."), 
])
def test_k_invalid_values(N_input, k_input, expected_error_message):
    assert sum_of_the_k_lowest_digits(N_input, k_input) == expected_error_message

@pytest.mark.parametrize("N_input, k_input, expected_error_message", [
    (-123, 2, 'Ошибка: число N должно быть неотрицательным.'),      
    ("-456", "3", 'Ошибка: число N должно быть неотрицательным.'),    
    (3.14, 2, "Ошибка: N должно быть целым числом."),              
    ("abc", 2, "Ошибка: N должно быть целым числом."),               
    (None, "2", "Ошибка: N должно быть целым числом."),             
    ([1, 2], 2, "Ошибка: N должно быть целым числом."),           
])
def test_N_invalid_values(N_input, k_input, expected_error_message):
    assert sum_of_the_k_lowest_digits(N_input, k_input) == expected_error_message

def test_failing_sum_demonstration():
    assert sum_of_the_k_lowest_digits(10, 1) == 500