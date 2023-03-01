#ifndef VECTOR_H
#define VECTOR_H

class Vector
{
private:
public:
    float *array;
    unsigned int shape[2];
    unsigned int size;

    Vector(float*, bool);
};

Vector add(Vector*, Vector*);
Vector sub(Vector*, Vector*);
Vector scalar_mult(Vector*, float);

#endif // VECTOR_H