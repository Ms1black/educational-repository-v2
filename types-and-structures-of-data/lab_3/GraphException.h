#pragma once
#include <string>
#include <exception>
#include <iostream>

#define RESET   "\033[0m"
#define RED     "\033[31m"

class GraphException : public std::exception {
private:
    std::string message;

public: 
    enum ErrorType { FILE_ERROR, INVALID_INPUT, GRAPH_ERROR, ALGORITHM_ERROR };

private: 
    ErrorType type;

public:
    GraphException(ErrorType errorType, const std::string& detail = "") : type(errorType) {
        std::string prefix = RED "Ошибка" RESET;
        switch (type) {
            case FILE_ERROR:
                message = prefix + " [ФАЙЛА]: Не удалось обработать файл. " + detail;
                break;
            case INVALID_INPUT:
                message = prefix + " [НЕКОРРЕКТНЫЙ_ВВОД]: Предоставлены неверные данные. " + detail;
                break;
            case GRAPH_ERROR:
                message = prefix + " [ГРАФА]: Проблема со структурой графа. " + detail;
                break;
            case ALGORITHM_ERROR:
                message = prefix + " [АЛГОРИТМА]: Ошибка при выполнении алгоритма. " + detail;
                break;
            default:
                message = prefix + " [НЕИЗВЕСТНО]: Произошла неизвестная ошибка. " + detail;
                break;
        }
    }

    const char* what() const noexcept override {
        return message.c_str();
    }

    ErrorType getType() const {
        return type;
    }
};