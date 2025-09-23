#pragma once
#include <string>
#include <exception>
#include <iostream>

class SLException : public std::exception {
private:
    std::string message;
    enum ErrorType { EMPTY_LIST, OUT_OF_INDEX, FILE_ERROR, INVALID_INPUT };
    ErrorType type;

public:
    SLException(ErrorType errorType, const std::string& detail = "") : type(errorType) {
        switch (type) {
            case EMPTY_LIST:
                message = "Ошибка [ПУСТОЙ_СПИСОК]: Список пуст. " + detail;
                break;
            case OUT_OF_INDEX:
                message = "Ошибка [ВНЕ_ДИАПАЗОНА]: Индекс вне границ. " + detail;
                break;
            case FILE_ERROR:
                message = "Ошибка [ФАЙЛА]: Не удалось обработать файл. " + detail;
                break;
            case INVALID_INPUT:
                message = "Ошибка [НЕКОРРЕКТНЫЙ_ВВОД]: Предоставлены неверные данные. " + detail;
                break;
            default:
                message = "Ошибка [НЕИЗВЕСТНО]: Произошла неизвестная ошибка. " + detail;
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