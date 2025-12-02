#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <limits>

#include "GraphException.h"

const int INF = 1000000000;

class Graph {
private:
    std::vector<std::vector<int>> adjMatrix;
    int numVertices;

public:
    Graph() : numVertices(0) {}

    Graph(int N) : numVertices(N) {
        if (N <= 0) {
            throw GraphException(GraphException::GRAPH_ERROR, "Число вершин должно быть положительным.");
        }
        adjMatrix.resize(N, std::vector<int>(N));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (i == j) {
                    adjMatrix[i][j] = 0;
                } else {
                    adjMatrix[i][j] = INF;
                }
            }
        }
    }

    void setNumVertices(int N) {
        if (N <= 0) {
            throw GraphException(GraphException::GRAPH_ERROR, "Число вершин должно быть положительным.");
        }
        numVertices = N;
        adjMatrix.resize(N, std::vector<int>(N));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (i == j) adjMatrix[i][j] = 0;
                else adjMatrix[i][j] = INF;
            }
        }
    }
    
    int getNumVertices() const {
        return numVertices;
    }

    void addEdge(int u, int v, int weight, bool bidirectional = true) {
        if (u < 0 || u >= numVertices || v < 0 || v >= numVertices) {
            throw GraphException(GraphException::GRAPH_ERROR, "Неверный индекс вершины для добавления ребра.");
        }
        
        adjMatrix[u][v] = std::min(adjMatrix[u][v], weight);
        if (bidirectional) {
            adjMatrix[v][u] = std::min(adjMatrix[v][u], weight);
        }
    }

    const std::vector<std::vector<int>>& getAdjMatrix() const {
        return adjMatrix;
    }
    
    void printMatrix(std::ostream& os) const {
        os << "Матрица смежности графа (" << numVertices << "x" << numVertices << "):" << std::endl;
        for (int i = 0; i < numVertices; ++i) {
            for (int j = 0; j < numVertices; ++j) {
                if (adjMatrix[i][j] == INF) {
                    os << "INF\t";
                } else {
                    os << adjMatrix[i][j] << "\t";
                }
            }
            os << std::endl;
        }
    }

    std::vector<std::vector<int>> floydWarshall() const {
        if (numVertices == 0) {
            throw GraphException(GraphException::ALGORITHM_ERROR, "Невозможно выполнить алгоритм на пустом графе.");
        }

        std::vector<std::vector<int>> dist = adjMatrix;

        for (int k = 0; k < numVertices; ++k) {
            for (int i = 0; i < numVertices; ++i) {
                for (int j = 0; j < numVertices; ++j) {
                    if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < INF) {
                        dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }
        for(int i = 0; i < numVertices; ++i){
            if(dist[i][i] < 0){
                 throw GraphException(GraphException::ALGORITHM_ERROR, "Обнаружен отрицательный цикл после алгоритма Флойда-Уоршелла. Алгоритм неприменим.");
            }
        }
        return dist;
    }
};