#!/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import csv
import sys

USAGE = "usage: {prog} input.csv"

class Teacher(object):

    PARAMS = 5
    PARAM_DICT = {'а': 0, 'б': 1, 'в': 2}
    EPS = 0.00001

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.count = 0
        self.params = [[0, 0, 0] for i in range(self.PARAMS)]

    def vote(self, data):

        self.count += 1

        for i in range(self.PARAMS):
            j = self.PARAM_DICT.get(data[i], -1)

            if j != -1:

                self.params[i][j] += 1

    def score(self, i):
        if self.count < 5:
            return 'н/д'
        if self.params[i][2] / self.count >= 0.5 - self.EPS:
            return 2 # '2 ({c}/{a} = {p:.0f}%)'.format(c=self.params[i][2], a=self.count, p=100 * self.params[i][2] / self.count)
        elif (self.params[i][1] + self.params[i][2]) / self.count >= 0.5 - self.EPS:
            return 3 # '3 ({c}/{a} = {p:.0f}%)'.format(c=self.params[i][1] + self.params[i][2], a=self.count, p=100 * (self.params[i][1] + self.params[i][2]) / self.count)
        elif self.params[i][0] / self.count >= 1.0 - self.EPS:
            return 5
        elif self.params[i][0] / self.count > 0.5 + self.EPS:
            return 4 # '4 ({c}/{a} = {p:.0f}%)'.format(c=self.params[i][0], a=self.count, p=100 * self.params[i][0] / self.count)
        else:
            return 'н/д'

    def status(self):
        result = []

        for i in range(self.PARAMS):
            result.append(self.score(i))

        return result


def mutate(c, mutate_dict):
    return mutate_dict.get(c, c)

class Lecturer(Teacher):

    def vote(self, data):
        data[0] = mutate(data[0], {'б': 'в', 'в': '-'})
        data[1] = mutate(data[1], {'б': 'в', 'в': '-'})
        data[4] = mutate(data[4], {'а': 'в', 'б': 'а', 'в': '-'})

        super().vote(data)

def main():
    if len(sys.argv) != 2:
        print(USAGE.format(prog=sys.argv[0]), file=sys.stderr)
        exit(1)

    teachers = {}

    with open(sys.argv[1], 'r') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)

        for i, row in enumerate(reader):
            if i > 0:
                name, subject, data = row[3], row[2], row[4:9]

                t = teachers.get(name, None)

                if t is None:
                    t = teachers[name] = Lecturer(name, subject)

                t.vote(data)

    result = []
    for key in sorted(teachers.keys()):
        t = teachers[key]
        result.append([t.subject, t.name, *t.status()])
    result.sort()

    csv.writer(sys.stdout).writerows(result)

if __name__ == "__main__":
    main()
