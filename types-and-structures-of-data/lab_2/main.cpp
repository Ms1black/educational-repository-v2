#include <iostream>
#include <vector>
#include <algorithm>

int MaxHeight(int h1, int h2) {
    return h1 > h2 ? h1 : h2;
}

struct AvlTree {
    int _data;
    int _height;
    AvlTree* _left;
    AvlTree* _right;

    AvlTree(int val) : _data(val), _height(0), _left(nullptr), _right(nullptr) {}
};

int Height(AvlTree* t) {
    return (t != nullptr) ? t->_height : -1;
}

void UpdateHeight(AvlTree* t) {
    if (t != nullptr) {
        t->_height = MaxHeight(Height(t->_left), Height(t->_right)) + 1;
    }
}

int GetBalance(AvlTree* t) {
    return (t != nullptr) ? Height(t->_left) - Height(t->_right) : 0;
}

AvlTree* RightRotate(AvlTree* t) {
    AvlTree* leftChild = t->_left;
    t->_left = leftChild->_right;
    leftChild->_right = t;

    UpdateHeight(t);
    UpdateHeight(leftChild); 

    return leftChild; 
}

AvlTree* LeftRotate(AvlTree* t) {
    AvlTree* rightChild = t->_right;
    t->_right = rightChild->_left;
    rightChild->_left = t;

    UpdateHeight(t);
    UpdateHeight(rightChild);

    return rightChild;
}

AvlTree* LeftRightRotate(AvlTree* t) {
    t->_left = LeftRotate(t->_left); 
    return RightRotate(t);           
}

AvlTree* RightLeftRotate(AvlTree* t) {
    t->_right = RightRotate(t->_right);
    return LeftRotate(t);
}

AvlTree* BalanceNode(AvlTree* t) {
    if (t == nullptr) return nullptr;

    UpdateHeight(t);

    int balanceFactor = GetBalance(t);

    if (balanceFactor > 1) {

        if (GetBalance(t->_left) >= 0) { 
            return RightRotate(t);
        }
        else {
            return LeftRightRotate(t);
        }
    }
    else if (balanceFactor < -1) {
        if (GetBalance(t->_right) <= 0) { 
            return LeftRotate(t);
        }
        else {
            return RightLeftRotate(t);
        }
    }
    return t; 
}

AvlTree* Insert(AvlTree* t, int data) {
    if (t == nullptr) {
        return new AvlTree(data); 
    }

    if (data < t->_data) {
        t->_left = Insert(t->_left, data);
    } else if (data > t->_data) {
        t->_right = Insert(t->_right, data);
    } else {
        return t;
    }

    return BalanceNode(t);
}

AvlTree* FindMin(AvlTree* t) {
    if (t == nullptr) return nullptr;
    while (t->_left != nullptr) {
        t = t->_left;
    }
    return t;
}

AvlTree* Delete(AvlTree* t, int data) {
    if (t == nullptr) {
        return nullptr;
    }

    if (data < t->_data) {
        t->_left = Delete(t->_left, data);
    } else if (data > t->_data) {
        t->_right = Delete(t->_right, data);
    } else {
        if (t->_left == nullptr || t->_right == nullptr) {
            AvlTree* temp = (t->_left != nullptr) ? t->_left : t->_right;

            if (temp == nullptr) {
                temp = t;
                t = nullptr;
            } else {
                *t = *temp; 
            }
            delete temp;
        }
        else {
            AvlTree* temp = FindMin(t->_right);
            t->_data = temp->_data;
            t->_right = Delete(t->_right, temp->_data);
        }
    }

    if (t == nullptr) {
        return nullptr;
    }

    return BalanceNode(t);
}


void printInOrder(AvlTree* node) {
    if (node != nullptr) {
        printInOrder(node->_left);
        std::cout << node->_data << " (h=" << node->_height << ") ";
        printInOrder(node->_right);
    }
}

void printTreeVisual(AvlTree* node, int level, const std::string& prefix, bool isLeft) {
    if (node != nullptr) {
        std::cout << prefix;
        std::cout << (isLeft ? "├──" : "└──"); 
        std::cout << node->_data << " (h=" << node->_height << ", bf=" << GetBalance(node) << ")" << std::endl;

        std::string childPrefix = prefix + (isLeft ? "│   " : "    ");

        if (node->_right) {
            printTreeVisual(node->_right, level + 1, childPrefix, true);
        }
        if (node->_left) {
            printTreeVisual(node->_left, level + 1, childPrefix, false);
        }
    }
}

void printTree(AvlTree* root) {
    if (root == nullptr) {
        std::cout << "Дерево пусто." << std::endl;
        return;
    }
    std::cout << "Корень: " << root->_data << " (h=" << root->_height << ", bf=" << GetBalance(root) << ")" << std::endl;

    if (root->_right) {
        printTreeVisual(root->_right, 0, "", true);
    }

    if (root->_left) {
        printTreeVisual(root->_left, 0, "", false);
    }
}

void DeleteTreeNodes(AvlTree* node) {
    if (node != nullptr) {
        DeleteTreeNodes(node->_left);
        DeleteTreeNodes(node->_right);
        delete node;
    }
}

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8"); 

    AvlTree* root = nullptr;

    std::cout << "Построение AVL-дерева с числами от 1 до 20...\n";
    for (int i = 1; i <= 20; ++i) {
        root = Insert(root, i);
    }

    std::cout << "\n--- AVL-дерево после вставки чисел 1-20 (In-order обход) ---\n";
    printInOrder(root);
    std::cout << std::endl;

    std::cout << "\n--- Визуализация AVL-дерева до удаления четных чисел ---\n";
    printTree(root);
    std::cout << "Высота дерева: " << Height(root) << std::endl;


    std::cout << "\nНачинаем удаление всех четных чисел (2, 4, ..., 20)...\n";
    for (int i = 2; i <= 20; i += 2) {
        std::cout << "Удаление числа: " << i << std::endl;
        root = Delete(root, i);
    }

    std::cout << "\n--- AVL-дерево после удаления всех четных чисел (In-order обход) ---\n";
    printInOrder(root);
    std::cout << std::endl;

    std::cout << "\n--- Визуализация AVL-дерева после удаления четных чисел ---\n";
    printTree(root);
    std::cout << "Высота дерева: " << Height(root) << std::endl;

    std::cout << "\nПроверка оставшихся элементов: \n";
    std::vector<int> expected = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};

    DeleteTreeNodes(root);

    return 0;
}