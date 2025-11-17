#include <iostream>
#include <fstream>
#include <string>
#include <limits>
#include <locale>
#include <vector>
#include <algorithm>

#include "SingleList.h"
#include "SLException.h"
#include "../ColorCodes.h"

std::vector<std::string> getUtf8Characters(const std::string& s) {
    std::vector<std::string> chars;
    if (s.empty()) return chars;

    for (size_t i = 0; i < s.length(); ) {
        int char_len = 1;
        unsigned char c = s[i];

        if ((c & 0x80) == 0) {
            char_len = 1;
        } else if ((c & 0xE0) == 0xC0) {
            char_len = 2;
        } else if ((c & 0xF0) == 0xE0) {
            char_len = 3;
        } else if ((c & 0xF8) == 0xF0) {
            char_len = 4;
        } else {
            char_len = 1;
        }

        if (i + char_len > s.length()) {
            char_len = 1;
        }

        chars.push_back(s.substr(i, char_len));
        i += char_len;
    }
    return chars;
}

std::string readSequenceFromFile(std::ifstream& inputFile, std::ostream& errorFile) {
    std::string inputSequence;
    if (inputFile.is_open()) {
        std::getline(inputFile, inputSequence);
        if (inputSequence.empty()) {
            errorFile << "Предупреждение: Входная строка для задачи пуста." << std::endl;
        }
        return inputSequence;
    } else {
        throw SLException(SLException::FILE_ERROR, "Входной файл не открыт для чтения данных для задачи.");
    }
}

SingleList* processSequence(const std::string& inputString) {
    SingleList* resultList = new SingleList();
    if (inputString.empty()) {
        return resultList;
    }

    std::vector<std::string> characters = getUtf8Characters(inputString);
    
    for (int i = characters.size() - 1; i >= 0; --i) {
        const std::string& currentUtf8Char = characters[i];
        if (!resultList->IsItem(currentUtf8Char)) {
            resultList->AddItem(currentUtf8Char);
        }
    }
    return resultList;
}

void runApplication() {
    const std::string inputFileName = "input.txt";
    const std::string outputFileName = "output.txt";
    const std::string errorFileName = "errors.txt";

    std::ifstream inputFile(inputFileName);
    std::ofstream outputFile(outputFileName);
    std::ofstream errorFile(errorFileName);

    if (!inputFile.is_open()) {
        std::cerr << RED << "Ошибка: Не удалось открыть входной файл " << inputFileName << RESET << std::endl;
        return;
    }
    if (!outputFile.is_open()) {
        std::cerr << RED << "Ошибка: Не удалось открыть выходной файл " << outputFileName << RESET << std::endl;
        if (errorFile.is_open()) errorFile << "Ошибка: Не удалось открыть выходной файл " << outputFileName << std::endl;
        return;
    }
    if (!errorFile.is_open()) {
        std::cerr << RED << "Ошибка: Не удалось открыть файл ошибок " << errorFileName << RESET << std::endl;
        return;
    }

    SingleList myList;

    int choice;
    bool running = true;
    while (running) {
        try {
            std::cout << BLUE << "\n=======================================================" << RESET << std::endl;
            std::cout << BLUE << "                      ГЛАВНОЕ МЕНЮ                     " << RESET << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << MAGENTA << "  1. " << RESET << "Добавить элемент в основной список (символ UTF-8)" << std::endl;
            std::cout << MAGENTA << "  2. " << RESET << "Удалить элемент из основного списка по индексу" << std::endl;
            std::cout << MAGENTA << "  3. " << RESET << "Проверить наличие элемента в основном списке (символ UTF-8)" << std::endl;
            std::cout << MAGENTA << "  4. " << RESET << "Вывести основной список (итеративно)" << std::endl;
            std::cout << MAGENTA << "  5. " << RESET << "Вывести основной список (рекурсивно)" << std::endl;
            std::cout << MAGENTA << "  6. " << RESET << "Очистить основной список" << std::endl;
            std::cout << GREEN << "  7. " << RESET << "ЗАПУСТИТЬ ИНДИВИДУАЛЬНУЮ ЗАДАЧУ (из '" << inputFileName << "')" << std::endl;
            std::cout << RED << "  0. " << RESET << "Выход" << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << YELLOW << "Введите ваш выбор: " << RESET;
            std::cin >> choice;

            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                throw SLException(SLException::INVALID_INPUT, "Пожалуйста, введите число для выбора пункта меню.");
            }
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

            std::string utf8_char_from_input;
            int index;
            SingleList* taskResultList = nullptr;

            switch (choice) {
                case 1: {
                    std::cout << CYAN << "Введите символ UTF-8 для добавления: " << RESET;
                    std::string temp_input_str;
                    std::cin >> std::ws;
                    std::getline(std::cin, temp_input_str); 
                    
                    std::vector<std::string> parsed_chars = getUtf8Characters(temp_input_str);
                    if (parsed_chars.size() != 1) { 
                         throw SLException(SLException::INVALID_INPUT, "Неверный ввод: ожидался ровно один UTF-8 символ для добавления.");
                    }
                    utf8_char_from_input = parsed_chars[0];

                    myList.AddItem(utf8_char_from_input); 
                    outputFile << "Добавлен элемент в основной список: '" << utf8_char_from_input << "'" << std::endl;
                    std::cout << BRIGHT_MAGENTA << "Элемент '" << utf8_char_from_input << "' добавлен." << RESET << std::endl;
                    break;
                }
                case 2: {
                    std::cout << CYAN << "Введите индекс для удаления: " << RESET;
                    std::cin >> index;
                    if (std::cin.fail()) throw SLException(SLException::INVALID_INPUT, "Неверный ввод индекса для DeleteItem.");
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    myList.DeleteItem(index);
                    outputFile << "Удален элемент по индексу " << index << " из основного списка." << std::endl;
                    std::cout << BRIGHT_MAGENTA << "Элемент по индексу " << index << " удален." << RESET << std::endl;
                    break;
                }
                case 3: {
                    std::cout << CYAN << "Введите символ UTF-8 для проверки: " << RESET;
                    std::string temp_input_str;
                    std::cin >> std::ws;
                    std::getline(std::cin, temp_input_str);

                    std::vector<std::string> parsed_chars = getUtf8Characters(temp_input_str);
                    if (parsed_chars.size() != 1) {
                         throw SLException(SLException::INVALID_INPUT, "Неверный ввод: ожидался ровно один UTF-8 символ для проверки.");
                    }
                    utf8_char_from_input = parsed_chars[0];

                    if (myList.IsItem(utf8_char_from_input)) { 
                        std::cout << BRIGHT_MAGENTA << "'" << utf8_char_from_input << "' ЕСТЬ в основном списке." << RESET << std::endl;
                        outputFile << "'" << utf8_char_from_input << "' ЕСТЬ в основном списке." << std::endl;
                    } else {
                        std::cout << BRIGHT_MAGENTA << "'" << utf8_char_from_input << "' НЕТ в основном списке." << RESET << std::endl;
                        outputFile << "'" << utf8_char_from_input << "' НЕТ в основном списке." << std::endl;
                    }
                    break;
                }
                case 4:
                    std::cout << BRIGHT_MAGENTA;
                    myList.PrintList(std::cout);   std::cout << RESET << std::endl;
                    myList.PrintList(outputFile); outputFile << std::endl;
                    break;
                case 5:
                    std::cout << BRIGHT_MAGENTA;
                    if (myList.GetTop() != nullptr) {
                        myList.PrintListRecurrently(myList.GetTop(), std::cout);   std::cout << RESET << std::endl;
                        myList.PrintListRecurrently(myList.GetTop(), outputFile); outputFile << std::endl;
                    } else {
                         std::cout << "[Список пуст]" << RESET << std::endl;
                         outputFile << "[Список пуст]" << std::endl;
                    }
                    break;
                case 6:
                    myList.DeleteList();
                    std::cout << BRIGHT_MAGENTA << "Основной список очищен." << RESET << std::endl;
                    outputFile << "Основной список очищен." << std::endl;
                    break;
                case 7: {
                    std::cout << GREEN << "Запуск индивидуальной задачи (используются символы из файла '" << inputFileName << "')..." << RESET << std::endl;
                    outputFile << "Запуск индивидуальной задачи (используются символы из входного файла '" << inputFileName << "')..." << std::endl;

                    inputFile.close();
                    inputFile.open(inputFileName);
                    if (!inputFile.is_open()) {
                        throw SLException(SLException::FILE_ERROR, "Не удалось повторно открыть входной файл для задачи '" + inputFileName + "'.");
                    }

                    std::string charSequence = readSequenceFromFile(inputFile, errorFile);
                    outputFile << "Входная последовательность для задачи: \"" << charSequence << "\"" << std::endl;
                    std::cout << CYAN << "Входная последовательность: \"" << charSequence << "\"" << RESET << std::endl;

                    SingleList* taskResultList = processSequence(charSequence);

                    std::cout << GREEN << "Результат задачи (последние вхождения, в порядке): ";
                    outputFile << "Результат задачи (последние вхождения, в порядке): ";
                    if (taskResultList->IsEmpty()) {
                        std::cout << "[Список результатов пуст]" << RESET;
                        outputFile << "[Список результатов пуст]";
                    } else {
                        taskResultList->PrintList(std::cout);
                        taskResultList->PrintList(outputFile);
                    }
                    std::cout << RESET << std::endl; outputFile << std::endl;

                    delete taskResultList;
                    taskResultList = nullptr;
                    break;
                }
                case 0:
                    running = false;
                    std::cout << RED << "Выход из приложения." << RESET << std::endl;
                    outputFile << "Приложение завершило работу." << std::endl;
                    break;
                default:
                    std::cout << YELLOW << "Неверный выбор. Пожалуйста, попробуйте еще раз." << RESET << std::endl;
                    outputFile << "Неверный выбор меню: " << choice << std::endl;
            }
        } catch (const SLException& e) {
            std::cerr << e.what() << std::endl;
            errorFile << e.what() << std::endl;
            if (e.getType() == SLException::FILE_ERROR || e.getType() == SLException::INVALID_INPUT) {
                 std::cerr << RED << "Произошла критическая ошибка. Приложение завершает работу." << RESET << std::endl;
                 errorFile << "Произошла критическая ошибка. Приложение завершает работу." << std::endl;
                 running = false;
            }
        } catch (const std::exception& e) {
            std::cerr << RED << "Необработанное стандартное исключение: " << e.what() << RESET << std::endl;
            errorFile << "Необработанное стандартное исключение: " << e.what() << std::endl;
            running = false;
        }
    }

    if (inputFile.is_open()) inputFile.close();
    if (outputFile.is_open()) outputFile.close();
    if (errorFile.is_open()) errorFile.close();
}

int main() {
    std::setlocale(LC_ALL, "ru_RU.UTF-8");
    runApplication();
    return 0;
}