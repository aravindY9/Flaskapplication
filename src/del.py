#!/bin/python3

import math
import os
import random
import re
import sys


# Enter your code here. Read input from STDIN. Print output to STDOUT4


class Employee:
    def __init__(self, name, id, age, gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender


class Organisation:

    def __init__(self, orgname, employee_list):
        self.orgname = orgname
        self.employeelist = employee_list

    def addEmployee(self, name, id, age, gender):
        emp_obj = Employee(name, id, age, gender)
        self.employeelist.append(emp_obj)

    def getEmployeeCount(self):
        count = len(self.employeelist)
        return count

    def findEmployeeAge(self, id):
        for empobject in self.employeelist:
            if empobject.id == id:
                return empobject.age
            else:
                return -1

    def countEmployees(self, age):
        count = 0
        for empobject in self.employeelist:
            if empobject.age > age:
                count += 1
        return count


if __name__ == '__main__':
    employees = []
    o = Organisation('XYZ', employees)
    n = int(input("count:"))
    for i in range(n):
        name = input("name")
        id = int(input("id:"))
        age = int(input("age:"))
        gender = input("gender:")
        o.addEmployee(name, id, age, gender)

    id = int(input())
    age = int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))