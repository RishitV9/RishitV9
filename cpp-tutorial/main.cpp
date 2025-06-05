#include <iostream>
#include "person.h"

Person yesh(20, "Yesh");

int main() {
    yesh.say_hi();
    std::cout << yesh.getAge() << std::endl;
}