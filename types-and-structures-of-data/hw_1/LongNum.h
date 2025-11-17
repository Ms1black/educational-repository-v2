#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <cstring>

#include "LongNumException.h"

#define DMAX 31
const int BASE = 10;
const char* digitFormat = "%.1d";


typedef int thuge[DMAX + 1];

int compare(const thuge a, const thuge b) {
    if (a[0] < b[0]) {
        return -1;
    }
    if (a[0] > b[0]) {
        return 1;
    }

    for (int i = a[0]; i >= 1; --i) {
        if (a[i] < b[i]) {
            return -1;
        }
        if (a[i] > b[i]) {
            return 1;
        }
    }
    return 0;
}

void readHuge(thuge a, const std::string& s_num) {
    if (s_num.empty() || s_num.length() > DMAX) {
        throw createLongNumException(LongNumException::INVALID_INPUT, "Неверный ввод числа или превышена максимальная длина (" + std::to_string(DMAX-1) + " цифр).");
    }

    std::memset(a, 0, sizeof(thuge));

    a[0] = s_num.length();
    int str_idx = a[0];

    for (int i = 1; i <= a[0]; ++i) {
        if (str_idx == 0) {
             throw createLongNumException(LongNumException::INVALID_INPUT, "Ошибка при парсинге строки.");
        }
        a[i] = s_num[str_idx-1] - '0';
        if (a[i] < 0 || a[i] > 9) {
            throw createLongNumException(LongNumException::INVALID_INPUT, "Введены нецифровые символы.");
        }
        str_idx--;
    }

    while (a[0] > 1 && a[a[0]] == 0) {
        --a[0];
    }
}

void subtract(thuge a, const thuge b) {
    int borrow = 0;

    if (compare(a, b) < 0) {
        throw createLongNumException(LongNumException::ARITHMETIC_ERROR, "Результат вычитания отрицательный (a < b).");
    }

    for (int i = 1; i <= a[0]; ++i) {
        int diff = a[i] - (i <= b[0] ? b[i] : 0) - borrow;


        if (diff < 0) {
            borrow = 1;
            diff += BASE;
        } else {
            borrow = 0;
        }
        a[i] = diff;
    }

    while (a[0] > 1 && a[a[0]] == 0) { 
        --a[0];
    }
}

void writeHuge(const thuge a, int m_len, std::ostream& os) {
    if (a[0] == 0) {
        os << "0.0 E 0";
        return;
    }

    int N_order = a[0]; 

    os << "+";

    os << "0.";

    int count_printed = 0;
    for (int i = a[0]; i >= 1 && count_printed < m_len; --i) {
        os << a[i];
        count_printed++;
    }

    for (int i = count_printed; i < m_len; ++i) {
        os << 0;
    }
    
    os << " E " << N_order;
}