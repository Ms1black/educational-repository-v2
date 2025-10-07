#pragma once
#include <string>
#include <exception>
#include <iostream>

#define RESET   "\033[0m"
#define RED     "\033[31m"      
#define YELLOW  "\033[33m"     
#define BLUE    "\033[34m"      
#define MAGENTA "\033[35m"     
#define CYAN    "\033[36m"     

class SLException : public std::exception {
private:
    std::string message;

public: 
    enum ErrorType { EMPTY_LIST, OUT_OF_INDEX, FILE_ERROR, INVALID_INPUT };

private: 
    ErrorType type;

public:
    SLException(ErrorType errorType, const std::string& detail = "") : type(errorType) {
        std::string prefix = RED "Ошибка" RESET;
        switch (type) {
            case EMPTY_LIST:
                message = prefix + " [ПУСТОЙ_СПИСОК]: Список пуст. " + detail;
                break;
            case OUT_OF_INDEX:
                message = prefix + " [ВНЕ_ДИАПАЗОНА]: Индекс вне границ. " + detail;
                break;
            case FILE_ERROR:
                message = prefix + " [ФАЙЛА]: Не удалось обработать файл. " + detail;
                break;
            case INVALID_INPUT:
                message = prefix + " [НЕКОРРЕКТНЫЙ_ВВОД]: Предоставлены неверные данные. " + detail;
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