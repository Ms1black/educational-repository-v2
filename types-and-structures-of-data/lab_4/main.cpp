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
#include <tuple>

#include "SparseMatrixSherman.h"
#include "SparseMatrixException.h"
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


void loadMatricesFromHardcodedData(SparseMatrixSherman& matrixA, SparseMatrixSherman& matrixB, std::ostream& outputFile) {
    // Данные для A (UDA, UNA, IUA, JUA, IJA)
    std::vector<int> UDA = { 1,2,3,4,5,6,7,8,9,10 }; 
    std::vector<int> UNA = { 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27}; 
    std::vector<int> IUA = { 1,4,6,8,9,11,14,16,17,18,18 }; 
    std::vector<int> JUA = { 3,7,10,6,9,8,9,10,8,9,10 }; 
    std::vector<int> IJA = { 1,4,2,5,2,6,9,10,11 }; 
    
    // Данные для B (UDB, UNB, IUB, JUB, IJB)
    std::vector<int> UDB = { 10,9,8,7,6,5,4,3,2,1 };
    std::vector<int> UNB = { 27,15,5,8,4,30,1,9,3,7,21,19,2 };
    std::vector<int> IUB = { 1,2,5,7,9,11,12,13,14,14,14 };
    std::vector<int> JUB = { 4,8,10,6,9,7,8 };
    std::vector<int> IJB = { 4,1,4,6,2,5,3,3 };

    matrixA.loadFromArrays(UDA, UNA, IUA, JUA, IJA);
    matrixB.loadFromArrays(UDB, UNB, IUB, JUB, IJB);

    outputFile << "Матрицы A и B загружены из предопределенных данных." << std::endl;
    std::cout << BRIGHT_MAGENTA << "Матрицы A и B успешно загружены из предопределенных данных." << RESET << std::endl;
}

void runApplication() {
    const std::string outputFileName = "output_sparse.txt";
    const std::string errorFileName = "errors_sparse.txt";

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

    SparseMatrixSherman matrixA;
    SparseMatrixSherman matrixB;

    bool matricesLoaded = false;

    int choice;
    bool running = true;
    while (running) {
        try {
            std::cout << BLUE << "\n=======================================================" << RESET << std::endl;
            std::cout << BLUE << "               МЕНЮ: Разреженные Матрицы             " << RESET << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << MAGENTA << "  1. " << RESET << "Загрузить матрицы A и B (предопределенные данные)" << std::endl;
            std::cout << MAGENTA << "  2. " << RESET << "Вывести матрицу A (схема Шермана / полный вид)" << std::endl;
            std::cout << MAGENTA << "  3. " << RESET << "Вывести матрицу B (схема Шермана / полный вид)" << std::endl;
            std::cout << GREEN << "  4. " << RESET << "ЗАДАНИЕ 13: Сложить матрицы A и B (схема Шермана)" << std::endl;
            std::cout << RED << "  0. " << RESET << "Выход" << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << YELLOW << "Введите ваш выбор: " << RESET;
            std::cin >> choice;

            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                throw SparseMatrixException(SparseMatrixException::INVALID_INPUT, "Пожалуйста, введите число для выбора пункта меню.");
            }
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
            
            switch (choice) {
                case 1: {
                    loadMatricesFromHardcodedData(matrixA, matrixB, outputFile);
                    matricesLoaded = true;
                    break;
                }
                case 2: {
                    if (!matricesLoaded) {
                        throw SparseMatrixException(SparseMatrixException::MATRIX_ERROR, "Матрицы A и B не загружены. Выберите 1-й пункт.");
                    }
                    std::cout << CYAN << "\nМатрица A (формат Шермана):" << RESET << std::endl;
                    matrixA.printShermanFormat(std::cout);
                    outputFile << "\nМатрица A (формат Шермана):" << std::endl;
                    matrixA.printShermanFormat(outputFile);

                    std::cout << CYAN << "\nМатрица A (полный вид для проверки):" << RESET << std::endl;
                    matrixA.printFullMatrix(std::cout);
                    outputFile << "\nМатрица A (полный вид для проверки):" << std::endl;
                    matrixA.printFullMatrix(outputFile);
                    break;
                }
                case 3: {
                    if (!matricesLoaded) {
                        throw SparseMatrixException(SparseMatrixException::MATRIX_ERROR, "Матрицы A и B не загружены. Выберите 1-й пункт.");
                    }
                    std::cout << CYAN << "\nМатрица B (формат Шермана):" << RESET << std::endl;
                    matrixB.printShermanFormat(std::cout);
                    outputFile << "\nМатрица B (формат Шермана):" << std::endl;
                    matrixB.printShermanFormat(outputFile);

                    std::cout << CYAN << "\nМатрица B (полный вид для проверки):" << RESET << std::endl;
                    matrixB.printFullMatrix(std::cout);
                    outputFile << "\nМатрица B (полный вид для проверки):" << std::endl;
                    matrixB.printFullMatrix(outputFile);
                    break;
                }
                case 4: {
                    if (!matricesLoaded) {
                        throw SparseMatrixException(SparseMatrixException::MATRIX_ERROR, "Матрицы A и B не загружены. Выберите 1-й пункт.");
                    }
                    std::cout << GREEN << "\nВыполнение ЗАДАНИЯ 13: Сложение матриц A и B..." << RESET << std::endl;
                    outputFile << "\nВыполнение ЗАДАНИЯ 13: Сложение матриц A и B..." << std::endl;

                    SparseMatrixSherman matrixC = matrixA.add(matrixB);

                    std::cout << BRIGHT_MAGENTA << "\nМатрица C (A + B) в формате Шермана:" << RESET << std::endl;
                    matrixC.printShermanFormat(std::cout);
                    outputFile << "\nМатрица C (A + B) в формате Шермана:" << std::endl;
                    matrixC.printShermanFormat(outputFile);
                    
                    std::cout << BRIGHT_MAGENTA << "\nМатрица C (A + B) в полном виде (для проверки):" << RESET << std::endl;
                    matrixC.printFullMatrix(std::cout);
                    outputFile << "\nМатрица C (A + B) в полном виде (для проверки):" << std::endl;
                    matrixC.printFullMatrix(outputFile);
                    
                    std::cout << GREEN << "\nСложение матриц завершено успешно." << RESET << std::endl;
                    outputFile << "\nСложение матриц завершено успешно." << std::endl;
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
        } catch (const SparseMatrixException& e) {
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