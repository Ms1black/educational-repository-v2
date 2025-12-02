#pragma once
#include <string>
#include <exception>
#include <iostream>

#define RESET   "\033[0m"
#define RED     "\033[31m"

class LongNumException : public std::exception {


public:
    enum ErrorType { INVALID_INPUT, ARITHMETIC_ERROR, OVERFLOW_ERROR };

private:
    std::string message;
    ErrorType type;

private:
    LongNumException(ErrorType errorType, const std::string& detail = "") : type(errorType) {
        std::string prefix = RED "Ошибка" RESET;
        switch (type) {
            case INVALID_INPUT:
                message = prefix + " [НЕКОРРЕКТНЫЙ_ВВОД]: " + detail;
                break;
            case ARITHMETIC_ERROR:
                message = prefix + " [АРИФМЕТИКА]: " + detail;
                break;
            case OVERFLOW_ERROR:
                message = prefix + " [ПЕРЕПОЛНЕНИЕ]: " + detail;
                break;
            default:
                message = prefix + " [НЕИЗВЕСТНО]: Произошла неизвестная ошибка. " + detail;
                break;
        }
    }

    friend LongNumException createLongNumException(ErrorType type, const std::string& detail);


public:
    static LongNumException create(ErrorType type, const std::string& detail = "") {
        return LongNumException(type, detail);
    }

    const char* what() const noexcept override {
        return message.c_str();
    }

    ErrorType getType() const {
        return type;
    }
};

inline LongNumException createLongNumException(LongNumException::ErrorType type, const std::string& detail = "") {
    return LongNumException::create(type, detail);
}