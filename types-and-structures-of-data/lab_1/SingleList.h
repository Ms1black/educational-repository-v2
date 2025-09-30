#pragma once
#include <iostream>
#include <string>
#include "SLException.h"

struct Node {
    std::string data;
    Node* next;

    Node(const std::string& val) : data(val), next(nullptr) {}
};

class SingleList {
private:
    Node* top;
    int size;

    void deleteListRecurrently(Node* current);
    void printRecursiveHelper(Node* current, std::ostream& os) const;

public:
    SingleList() : top(nullptr), size(0) {}
    ~SingleList();
    Node* GetTop() const { return top; }
    int GetSize() const { return size; }
    bool IsEmpty() const { return (top == nullptr); }

    void AddItem(const std::string& _data);
    void DeleteItem(int index);
    bool IsItem(const std::string& source) const;
    void PrintList(std::ostream& os) const;
    void PrintListRecurrently(Node* _top, std::ostream& os) const;
    void DeleteList();
};

SingleList::~SingleList() {
    DeleteList();
}

void SingleList::AddItem(const std::string& _data) {
    Node* temp = new Node(_data);
    temp->next = top;
    top = temp;
    size++;
}

void SingleList::DeleteItem(int index) {
    if (index < 1 || index > size) {
        throw SLException(SLException::OUT_OF_INDEX, "Попытка удалить по индексу " + std::to_string(index) + ", но размер списка " + std::to_string(size) + ".");
    }
    if (IsEmpty()) {
        throw SLException(SLException::EMPTY_LIST, "Невозможно удалить из пустого списка.");
    }

    if (index == 1) {
        Node* temp = top;
        top = top->next;
        delete temp;
    } else {
        Node* prev = top;
        for (int i = 1; i < index - 1; ++i) {
            prev = prev->next;
        }
        Node* temp = prev->next;
        if (temp == nullptr) {
            throw SLException(SLException::OUT_OF_INDEX, "Внутренняя логическая ошибка: попытка удалить NULL.");
        }
        prev->next = temp->next;
        delete temp;
    }
    size--;
}

bool SingleList::IsItem(const std::string& source) const {
    Node* temp = top;
    while (temp != nullptr) {
        if (temp->data == source) {
            return true;
        }
        temp = temp->next;
    }
    return false;
}

void SingleList::PrintList(std::ostream& os) const {
    if (IsEmpty()) {
        os << "[Список пуст]";
        return;
    }
    Node* temp = top;
    os << "Список (" << size << " элементов): ";
    while (temp != nullptr) {
        os << temp->data << " ";
        temp = temp->next;
    }
}

void SingleList::PrintListRecurrently(Node* _top, std::ostream& os) const {
    if (IsEmpty()) {
        throw SLException(SLException::EMPTY_LIST, "Невозможно рекурсивно напечатать, список пуст.");
    }
    os << "Список (рекурсивный, начиная с узла по адресу " << _top << ", размер " << size << "): ";
    printRecursiveHelper(_top, os);
}

void SingleList::DeleteList() {
    if (IsEmpty()) {
        return;
    }
    deleteListRecurrently(top);
    top = nullptr;
    size = 0;
}

void SingleList::deleteListRecurrently(Node* current) {
    if (current == nullptr) return;
    deleteListRecurrently(current->next);
    delete current;
}

void SingleList::printRecursiveHelper(Node* current, std::ostream& os) const {
    if (current != nullptr) {
        os << current->data << " ";
        printRecursiveHelper(current->next, os);
    }
}