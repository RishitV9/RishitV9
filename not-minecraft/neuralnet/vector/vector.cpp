#include "vector.h"
#include <iostream>
using std::cout;
using std::endl;

Vector::Vector(float *arr, bool vertical):array(arr)
{
    size = sizeof(arr) / sizeof(arr[0]);
    if (vertical) { shape[0] = 1; shape[1] = size; } 
    else {shape[1] = 1; shape[0] = size;}
}

Vector add(Vector* v1, Vector* v2)
{
    if (v1->shape[1] != v2->shape[1] && v1->shape[0] != v2->shape[0]) {
        cout << "Error, dimensions don't match" << endl;
        exit(1);
    }
    float cont[v1->size];
    for (int i = 0; i < v1->size; i++) {
        cont[i] = v1->array[i] + v2->array[i];
    }
    bool vert;
    if (v1->shape[1] != 1) { vert = false; }
    else { vert = true; }

    Vector o(cont, vert);
    return o;
};

Vector sub(Vector* v1, Vector* v2)
{
    if (v1->shape[1] != v2->shape[1] && v1->shape[0] != v2->shape[0]) {
        cout << "Error, dimensions don't match" << endl;
        exit(1);
    }
    float cont[v1->size];
    for (int i = 0; i < v1->size; i++) {
        cont[i] = v1->array[i] - v2->array[i];
    }
    bool vert;
    if (v1->shape[1] != 1) { vert = false; }
    else { vert = true; }

    Vector o(cont, vert);
    return o;
};

Vector scalar_mult(Vector* v1, float s)
{
    float cont[v1->size];
    for (int i = 0; i < v1->size; i++) {
        cont[i] = v1->array[i] * s;
    }
    bool vert;
    if (v1->shape[1] != 1) { vert = false; }
    else { vert = true; }

    Vector o(cont, vert);
    return o;
}
