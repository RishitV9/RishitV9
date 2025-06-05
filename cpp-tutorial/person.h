// everything related to a class...

#ifndef PERSON_H
#define PERSON_H

#include <iostream>
#include <string>

class Person {
private:
    int age;
    std::string name;
public:
    Person(int age, std::string name) {
        this->name = name;
        this->age = age;
    }

    void say_hi() {
        std::cout << "Hi!" << std::endl;
    }

    int getAge() {
        return age;
    }
};

#endif