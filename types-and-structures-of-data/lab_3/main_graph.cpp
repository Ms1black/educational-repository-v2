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

#include "Graph.h"
#include "GraphException.h"

#define RESET   "\033[0m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m"
#define BLUE    "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN    "\033[36m"
#define BRIGHT_MAGENTA "\033[95m"

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

void readGraphFromFile(Graph& graph, const std::string& filename, std::ostream& errorFile) {
    std::ifstream inFile(filename);
    if (!inFile.is_open()) {
        throw GraphException(GraphException::FILE_ERROR, "Не удалось открыть файл графа: " + filename);
    }

    int N;
    if (!(inFile >> N) || N <= 0) {
        throw GraphException(GraphException::INVALID_INPUT, "Неверный формат: ожидается положительное число вершин.");
    }
    graph.setNumVertices(N);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int weight;
            std::string token;
            if (!(inFile >> token)) {
                throw GraphException(GraphException::INVALID_INPUT, "Неверный формат: ожидаются элементы матрицы, получено EOF.");
            }
            if (token == "INF") {
                weight = INF;
            } else {
                try {
                    weight = std::stoi(token);
                } catch (const std::invalid_argument& e) {
                    throw GraphException(GraphException::INVALID_INPUT, "Неверный формат: вес '" + token + "' не является числом или 'INF'.");
                } catch (const std::out_of_range& e) {
                     throw GraphException(GraphException::INVALID_INPUT, "Неверный формат: вес '" + token + "' выходит за пределы int.");
                }
            }
            graph.addEdge(i, j, weight, false);
        }
    }
    inFile.close();
}

bool solveAssignment(
    const Graph& initialGraph,
    int startCity,
    int maxDistance,
    int newRoadWeight,
    std::ostream& outputFile,
    std::ostream& errorFile,
    std::vector<std::tuple<int, int, int>>& resultingAddedRoads
) {
    int N = initialGraph.getNumVertices();
    if (N == 0) {
        errorFile << RED << "Ошибка: Граф пуст, невозможно выполнить Задачу." << RESET << std::endl;
        return false;
    }
    if (startCity < 0 || startCity >= N) {
        errorFile << RED << "Ошибка: Неверный индекс начального города (" << startCity << "). Должен быть от 0 до " << N - 1 << RESET << std::endl;
        return false;
    }

    std::vector<std::pair<int, int>> allPossiblePairs;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            allPossiblePairs.push_back({i, j});
        }
    }

    if (allPossiblePairs.size() < 3) {
         errorFile << YELLOW << "Предупреждение: Количество возможных пар городов менее 3. Невозможно добавить 3 новые дороги." << RESET << std::endl;
         return false;
    }

    bool solutionFound = false;
    
    for (size_t r1_idx = 0; r1_idx < allPossiblePairs.size(); ++r1_idx) {
        for (size_t r2_idx = r1_idx + 1; r2_idx < allPossiblePairs.size(); ++r2_idx) {
            for (size_t r3_idx = r2_idx + 1; r3_idx < allPossiblePairs.size(); ++r3_idx) {
                Graph modifiedGraph = initialGraph;
                std::vector<std::tuple<int, int, int>> currentAddedRoadsCombination;

                modifiedGraph.addEdge(allPossiblePairs[r1_idx].first, allPossiblePairs[r1_idx].second, newRoadWeight, true);
                currentAddedRoadsCombination.push_back({allPossiblePairs[r1_idx].first, allPossiblePairs[r1_idx].second, newRoadWeight});

                modifiedGraph.addEdge(allPossiblePairs[r2_idx].first, allPossiblePairs[r2_idx].second, newRoadWeight, true);
                currentAddedRoadsCombination.push_back({allPossiblePairs[r2_idx].first, allPossiblePairs[r2_idx].second, newRoadWeight});

                modifiedGraph.addEdge(allPossiblePairs[r3_idx].first, allPossiblePairs[r3_idx].second, newRoadWeight, true);
                currentAddedRoadsCombination.push_back({allPossiblePairs[r3_idx].first, allPossiblePairs[r3_idx].second, newRoadWeight});
                
                try {
                    std::vector<std::vector<int>> distances = modifiedGraph.floydWarshall();
                    
                    bool allReachableWithinDistance = true;
                    for (int i = 0; i < N; ++i) {
                        if (i == startCity) continue;
                        
                        if (distances[startCity][i] == INF || distances[startCity][i] > maxDistance) {
                            allReachableWithinDistance = false;
                            break;
                        }
                    }

                    if (allReachableWithinDistance) {
                        resultingAddedRoads = currentAddedRoadsCombination;
                        return true; 
                    }

                } catch (const GraphException& e) {
                    errorFile << YELLOW << "Предупреждение: Алгоритм Флойда-Уоршелла встретил проблему: " << e.what() << ". Продолжение поиска." << RESET << std::endl;
                }
            }
        }
    }

    return false;
}

void runApplication() {
    const std::string graphFileName = "graph.txt";
    const std::string outputFileName = "output.txt";
    const std::string errorFileName = "errors.txt";

    std::ifstream inputFile(graphFileName);
    std::ofstream outputFile(outputFileName);
    std::ofstream errorFile(errorFileName);

    if (!inputFile.is_open()) {
        std::cerr << RED << "Ошибка: Не удалось открыть входной файл " << graphFileName << RESET << std::endl;
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

    Graph myGraph;

    int choice;
    bool running = true;
    while (running) {
        try {
            std::cout << BLUE << "\n=======================================================" << RESET << std::endl;
            std::cout << BLUE << "                      ГЛАВНОЕ МЕНЮ                     " << RESET << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << MAGENTA << "  1. " << RESET << "Загрузить граф из файла '" << graphFileName << "'" << std::endl;
            std::cout << MAGENTA << "  2. " << RESET << "Вывести матрицу смежности текущего графа" << std::endl;
            std::cout << GREEN << "  3. " << RESET << "Достижимость городов (построить 3 дороги)" << std::endl;
            std::cout << RED << "  0. " << RESET << "Выход" << std::endl;
            std::cout << BLUE << "=======================================================" << RESET << std::endl;
            std::cout << YELLOW << "Введите ваш выбор: " << RESET;
            std::cin >> choice;

            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                throw GraphException(GraphException::INVALID_INPUT, "Пожалуйста, введите число для выбора пункта меню.");
            }
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

            int index; 
            int startCity;
            int maxDistance;
            int newRoadWeight = 1; 
            
            switch (choice) {
                case 1: {
                    inputFile.close();
                    inputFile.open(graphFileName);
                    if (!inputFile.is_open()) {
                        throw GraphException(GraphException::FILE_ERROR, "Не удалось открыть файл графа '" + graphFileName + "' для чтения.");
                    }
                    readGraphFromFile(myGraph, graphFileName, errorFile);
                    outputFile << "Граф загружен из файла '" << graphFileName << "'." << std::endl;
                    std::cout << BRIGHT_MAGENTA << "Граф успешно загружен из '" << graphFileName << "'." << RESET << std::endl;
                    break;
                }
                case 2: {
                    if (myGraph.getNumVertices() == 0) {
                        std::cout << YELLOW << "Граф пуст. Сначала загрузите его (Пункт 1)." << RESET << std::endl;
                    } else {
                        std::cout << BRIGHT_MAGENTA;
                        myGraph.printMatrix(std::cout);
                        outputFile << "Текущая матрица смежности:" << std::endl;
                        myGraph.printMatrix(outputFile);
                        std::cout << RESET;
                    }
                    break;
                }
                case 3: {
                    if (myGraph.getNumVertices() == 0) {
                        throw GraphException(GraphException::ALGORITHM_ERROR, "Невозможно выполнить Задачу: граф пуст. Сначала загрузите его.");
                    }
                    
                    std::cout << CYAN << "Введите начальный город (индекс от 0 до " << myGraph.getNumVertices() - 1 << "): " << RESET;
                    std::cin >> startCity;
                    if (std::cin.fail() || startCity < 0 || startCity >= myGraph.getNumVertices()) {
                        std::cin.clear();
                        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                        throw GraphException(GraphException::INVALID_INPUT, "Неверный начальный город. Введите число в пределах диапазона.");
                    }
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

                    std::cout << CYAN << "Введите максимальное расстояние (T): " << RESET;
                    std::cin >> maxDistance;
                    if (std::cin.fail() || maxDistance <= 0) {
                        std::cin.clear();
                        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                        throw GraphException(GraphException::INVALID_INPUT, "Неверное максимальное расстояние. Введите положительное число.");
                    }
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    
                    std::vector<std::tuple<int, int, int>> addedRoadsForSolution; 
                    bool foundSolution = solveAssignment(myGraph, startCity, maxDistance, newRoadWeight, outputFile, errorFile, addedRoadsForSolution);

                    if (foundSolution) {
                        std::cout << GREEN << "ДА, возможно! Путь найден с расстоянием не более " << maxDistance << "." << RESET << std::endl;
                        outputFile << "ДА, возможно!" << std::endl;
                        outputFile << "Начальный город: " << startCity << ", Максимальное расстояние (T): " << maxDistance << std::endl;
                        outputFile << "Были добавлены следующие дороги (город1, город2, вес):" << std::endl;
                        for(const auto& road : addedRoadsForSolution){
                             outputFile << "(" << std::get<0>(road) << ", " << std::get<1>(road) << ", " << std::get<2>(road) << ")" << std::endl;
                        }

                    } else {
                        std::cout << RED << "НЕТ, невозможно. Не удалось найти комбинацию из 3 дорог." << RESET << std::endl;
                        outputFile << "НЕТ, невозможно." << std::endl;
                    }
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
        } catch (const GraphException& e) {
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

    if (inputFile.is_open()) inputFile.close();
    if (outputFile.is_open()) outputFile.close();
    if (errorFile.is_open()) errorFile.close();
}

int main() {
    std::setlocale(LC_ALL, "ru_RU.UTF-8");
    runApplication();
    return 0;
}