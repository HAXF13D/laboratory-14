#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def individual_func(string):
    def replace_string(name, surname):
        nonlocal string
        answer = string.replace("%N%", name)
        answer = answer.replace("%F%", surname)
        return answer

    return replace_string


if __name__ == "__main__":
    replacer = individual_func("Уважаемый %F%, %N%!"
                               " Вы делаете работу по замыканиям функций.")
    print(replacer('Vladimir', 'Shalnev'))
    print(replacer('Dinis', 'Proverkovich'))
    replacer = individual_func("Уважаемый %F%, %N%!")
    print(replacer('Nestikus', 'Dimov'))
