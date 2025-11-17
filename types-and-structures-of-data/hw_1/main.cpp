#include <iostream>
#include <fstream>
#include <string>
#include <limits>
#include <locale>
#include <vector>
#include <algorithm> 
#include <chrono>  
#include <thread>  
#include <cstdlib> 

#include "LongNum.h"         
#include "LongNumException.h"
#include "../ColorCodes.h"

void pause_and_clear_screen(int seconds = 3) {
    std::cout << BLUE << "\n=======================================================" << RESET << std::endl;
    std::cout << CYAN << "      Программа продолжит работу через " << seconds << " секунды(сек)..." << RESET << std::endl;
    std::cout << CYAN << "      Нажмите ENTER для немедленного продолжения..." << RESET << std::endl;
    std::cout << BLUE << "=======================================================" << RESET << std::endl;

    std::cout << "\n" << GREEN << "Нажмите ENTER для продолжения..." << RESET << std::endl;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getchar(); 
    
    std::system("clear"); 
}


void runApplication() {
    const std::string outputFileName = "output_longnum.txt";
    const std::string errorFileName = "errors_longnum.txt";

    std::ofstream outputFile(outputFileName);
    std::ofstream errorFile(errorFileName);

    if (!outputFile.is_open()) {
        std::cerr << RED << "Ошибка: Не удалось открыть выходной файл " << outputFileName << RESET << std::endl;
        return;
    }
    if (!errorFile.is_open()) {
        std::cerr << RED << "Ошибка: Не удалось открыть файл ошибок " << errorFileName << RESET << std::endl;
        return;
    }

    thuge numA, numB;
    bool numbersLoaded = false;

    const int MAN_LEN = 30;

    int choice;
    bool running = true;
    while (running) {
        try {
            std::cout << BLUE << "\n=======================================================" << RESET << std::endl;
            std::cout << BLUE << "           МЕНЮ: Операции над длинными числами         " << RESET << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << MAGENTA << "  1. " << RESET << "Ввести два длинных числа (A и B)" << std::endl;
            std::cout << MAGENTA << "  2. " << RESET << "Вывести число A" << std::endl;
            std::cout << MAGENTA << "  3. " << RESET << "Вывести число B" << std::endl;
            std::cout << GREEN << "  4. " << RESET << "ЗАДАНИЕ 13: Выполнить вычитание (A - B)" << std::endl;
            std::cout << RED << "  0. " << RESET << "Выход" << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << YELLOW << "Введите ваш выбор: " << RESET;
            std::cin >> choice;

            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                throw createLongNumException(LongNumException::INVALID_INPUT, "Пожалуйста, введите число для выбора пункта меню.");
            }
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
            
            std::string input_num_str;

            switch (choice) {
                case 1: {
                    std::cout << CYAN << "Введите длинное число A (до 30 цифр): " << RESET;
                    std::cin >> input_num_str;
                    if (std::cin.fail()) {
                        std::cin.clear(); std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                        throw createLongNumException(LongNumException::INVALID_INPUT, "Неверный ввод числа A.");
                    }
                    readHuge(numA, input_num_str);
                    
                    std::cout << CYAN << "Введите длинное число B (до 30 цифр): " << RESET;
                    std::cin >> input_num_str;
                     if (std::cin.fail()) {
                        std::cin.clear(); std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                        throw createLongNumException(LongNumException::INVALID_INPUT, "Неверный ввод числа B.");
                    }
                    readHuge(numB, input_num_str);
                    
                    numbersLoaded = true;
                    outputFile << "Загружены числа A: "; writeHuge(numA, MAN_LEN, outputFile); outputFile << " и B: "; writeHuge(numB, MAN_LEN, outputFile); outputFile << std::endl;
                    std::cout << BRIGHT_MAGENTA << "Числа A и B успешно введены." << RESET << std::endl;
                    break;
                }
                case 2: {
                    if (!numbersLoaded) {
                        throw createLongNumException(LongNumException::ARITHMETIC_ERROR, "Числа A и B не загружены. Выберите 1-й пункт меню.");
                    }
                    std::cout << CYAN << "\nЧисло A: " << RESET;
                    writeHuge(numA, MAN_LEN, std::cout); std::cout << std::endl;
                    outputFile << "\nЧисло A: "; writeHuge(numA, MAN_LEN, outputFile); outputFile << std::endl;
                    break;
                }
                case 3: {
                    if (!numbersLoaded) {
                        throw createLongNumException(LongNumException::ARITHMETIC_ERROR, "Числа A и B не загружены. Выберите 1-й пункт меню.");
                    }
                    std::cout << CYAN << "\nЧисло B: " << RESET;
                    writeHuge(numB, MAN_LEN, std::cout); std::cout << std::endl;
                    outputFile << "\nЧисло B: "; writeHuge(numB, MAN_LEN, outputFile); outputFile << std::endl;
                    break;
                }
                case 4: {
                    if (!numbersLoaded) {
                        throw createLongNumException(LongNumException::ARITHMETIC_ERROR, "Числа A и B не загружены. Выберите 1-й пункт меню.");
                    }

                    thuge resultNum;
                    std::memcpy(resultNum, numA, sizeof(thuge)); 

                    if (compare(resultNum, numB) < 0) {
                        throw createLongNumException(LongNumException::ARITHMETIC_ERROR, "Уменьшаемое число A меньше вычитаемого B. Вычитание для отрицательного результата не реализовано согласно методичке.");
                    }

                    std::cout << GREEN << "\nВыполнение ЗАДАНИЯ 13: Вычитание (A - B)..." << RESET << std::endl;
                    outputFile << "\nВыполнение ЗАДАНИЯ 13: Вычитание (A - B)..." << std::endl;

                    subtract(resultNum, numB);

                    std::cout << BRIGHT_MAGENTA << "\nРезультат (A - B): ";
                    writeHuge(resultNum, MAN_LEN, std::cout); std::cout << RESET << std::endl;
                    outputFile << "\nРезультат (A - B): "; writeHuge(resultNum, MAN_LEN, outputFile); outputFile << std::endl;

                    std::cout << GREEN << "\nВычитание чисел завершено успешно." << RESET << std::endl;
                    outputFile << "\nВычитание чисел завершено успешно." << std::endl;
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
        } catch (const LongNumException& e) {
            std::cerr << e.what() << std::endl;
            errorFile << e.what() << std::endl;
            std::cout << RED << "Произошла ошибка: " << e.what() << RESET << std::endl;
        } catch (const std::exception& e) {
            std::cerr << RED << "Необработанное стандартное исключение: " << e.what() << RESET << std::endl;
            errorFile << "Необработанное стандартное исключение: " << e.what() << std::endl;
            std::cout << RED << "Необработанное исключение. Завершение работы." << RESET << std::endl;
            running = false;
        }

        if (running && choice != 0) {
            pause_and_clear_screen();
        }
    }

    if (outputFile.is_open()) outputFile.close();
    if (errorFile.is_open()) errorFile.close();
}

int main() {
    std::setlocale(LC_ALL, "ru_RU.UTF-8");
    runApplication();
    return 0;
}