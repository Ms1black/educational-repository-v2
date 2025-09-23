#include <iostream>
#include <fstream>
#include <string>
#include <limits>
#include <locale>
#include "SingleList.h"
#include "SLException.h"

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

SingleList* processSequence(const std::string& s) {
    SingleList* resultList = new SingleList();
    if (s.empty()) {
        return resultList;
    }

    for (int i = s.length() - 1; i >= 0; --i) {
        char currentChar = s[i];
        if (!resultList->IsItem(currentChar)) {
            resultList->AddItem(currentChar);
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
        std::cerr << "Ошибка: Не удалось открыть входной файл " << inputFileName << std::endl;
        return;
    }
    if (!outputFile.is_open()) {
        std::cerr << "Ошибка: Не удалось открыть выходной файл " << outputFileName << std::endl;
        if (errorFile.is_open()) errorFile << "Ошибка: Не удалось открыть выходной файл " << outputFileName << std::endl;
        return;
    }
    if (!errorFile.is_open()) {
        std::cerr << "Ошибка: Не удалось открыть файл ошибок " << errorFileName << std::endl;
        return;
    }

    SingleList myList;

    int choice;
    bool running = true;
    while (running) {
        try {
            std::cout << "\n [ М Е Н Ю ]" << std::endl;
            std::cout << "1. Добавить элемент в основной список (символ)" << std::endl;
            std::cout << "2. Удалить элемент из основного списка по индексу (символ)" << std::endl;
            std::cout << "3. Проверить наличие элемента в основном списке (символ)" << std::endl;
            std::cout << "4. Вывести основной список (итеративно, символ)" << std::endl;
            std::cout << "5. Вывести основной список (рекурсивно, символ)" << std::endl;
            std::cout << "6. Очистить основной список (символ)" << std::endl;
            std::cout << "7. ЗАПУСТИТЬ ИНДИВИДУАЛЬНУЮ ЗАДАЧУ (символы из файла '" << inputFileName << "')" << std::endl;
            std::cout << "0. Выход" << std::endl;
            std::cout << "Введите ваш выбор: ";
            std::cin >> choice;

            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                throw SLException(SLException::INVALID_INPUT, "Пожалуйста, введите число для выбора пункта меню.");
            }
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

            char charData;
            int index;
            SingleList* taskResultList = nullptr;

            switch (choice) {
                case 1:
                    std::cout << "Введите символ для добавления: ";
                    std::cin >> std::ws;
                    std::cin.get(charData);
                    if (std::cin.fail()) throw SLException(SLException::INVALID_INPUT, "Неверный ввод символа для AddItem.");
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    myList.AddItem(charData);
                    outputFile << "Добавлен элемент в основной список: '" << charData << "'" << std::endl;
                    std::cout << "Элемент '" << charData << "' добавлен." << std::endl;
                    break;
                case 2:
                    std::cout << "Введите индекс для удаления: ";
                    std::cin >> index;
                    if (std::cin.fail()) throw SLException(SLException::INVALID_INPUT, "Неверный ввод индекса для DeleteItem.");
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    myList.DeleteItem(index);
                    outputFile << "Удален элемент по индексу " << index << " из основного списка." << std::endl;
                    std::cout << "Элемент по индексу " << index << " удален." << std::endl;
                    break;
                case 3:
                    std::cout << "Введите символ для проверки: ";
                    std::cin >> std::ws;
                    std::cin.get(charData);
                    if (std::cin.fail()) throw SLException(SLException::INVALID_INPUT, "Неверный ввод символа для IsItem.");
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    if (myList.IsItem(charData)) {
                        std::cout << "'" << charData << "' ЕСТЬ в основном списке." << std::endl;
                        outputFile << "'" << charData << "' ЕСТЬ в основном списке." << std::endl;
                    } else {
                        std::cout << "'" << charData << "' НЕТ в основном списке." << std::endl;
                        outputFile << "'" << charData << "' НЕТ в основном списке." << std::endl;
                    }
                    break;
                case 4:
                    myList.PrintList(std::cout);   std::cout << std::endl;
                    myList.PrintList(outputFile); outputFile << std::endl;
                    break;
                case 5:
                    if (myList.GetTop() != nullptr) {
                        myList.PrintListRecurrently(myList.GetTop(), std::cout);   std::cout << std::endl;
                        myList.PrintListRecurrently(myList.GetTop(), outputFile); outputFile << std::endl;
                    } else {
                         std::cout << "[Список пуст]" << std::endl;
                         outputFile << "[Список пуст]" << std::endl;
                    }
                    break;
                case 6:
                    myList.DeleteList();
                    std::cout << "Основной список очищен." << std::endl;
                    outputFile << "Основной список очищен." << std::endl;
                    break;
                case 7:
                    std::cout << "Запуск индивидуальной задачи (используются символы из входного файла '" << inputFileName << "')..." << std::endl;
                    outputFile << "Запуск индивидуальной задачи (используются символы из входного файла '" << inputFileName << "')..." << std::endl;

                    inputFile.close();
                    inputFile.open(inputFileName);
                    if (!inputFile.is_open()) {
                        throw SLException(SLException::FILE_ERROR, "Не удалось повторно открыть входной файл для задачи '" + inputFileName + "'.");
                    }

                    std::string charSequence = readSequenceFromFile(inputFile, errorFile);
                    outputFile << "Входная последовательность для задачи: \"" << charSequence << "\"" << std::endl;
                    std::cout << "Входная последовательность: \"" << charSequence << "\"" << std::endl;

                    taskResultList = processSequence(charSequence);

                    std::cout << "Результат задачи (последние вхождения, в порядке): ";
                    outputFile << "Результат задачи (последние вхождения, в порядке): ";
                    if (taskResultList->IsEmpty()) {
                        std::cout << "[Список результатов пуст]";
                        outputFile << "[Список результатов пуст]";
                    } else {
                        taskResultList->PrintList(std::cout);
                        taskResultList->PrintList(outputFile);
                    }
                    std::cout << std::endl; outputFile << std::endl;

                    delete taskResultList;
                    taskResultList = nullptr;
                    break;
                case 0:
                    running = false;
                    std::cout << "Выход из приложения." << std::endl;
                    outputFile << "Приложение завершило работу." << std::endl;
                    break;
                default:
                    std::cout << "Неверный выбор. Пожалуйста, попробуйте еще раз." << std::endl;
                    outputFile << "Неверный выбор меню: " << choice << std::endl;
            }
        } catch (const SLException& e) {
            std::cerr << e.what() << std::endl;
            errorFile << e.what() << std::endl;
            if (e.getType() == SLException::FILE_ERROR || e.getType() == SLException::INVALID_INPUT) {
                 std::cerr << "Произошла критическая ошибка. Приложение завершает работу." << std::endl;
                 errorFile << "Произошла критическая ошибка. Приложение завершает работу." << std::endl;
                 running = false;
            }
        } catch (const std::exception& e) {
            std::cerr << "Необработанное стандартное исключение: " << e.what() << std::endl;
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