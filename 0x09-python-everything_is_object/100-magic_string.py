#!/usr/bin/python3
class Myclass:
    func_time_call = -1
def magic_string():
    Myclass.func_time_call +=1
    return "BestSchool, " * Myclass.func_time_call + "BestSchool"