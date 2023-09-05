#!/usr/bin/python3
def magic_string():
    magic_string.func_time_call = getattr(magic_string,"func_time_call", 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.func_time_call)])
