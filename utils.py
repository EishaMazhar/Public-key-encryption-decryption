import time

def start_time():
    return  time.time()

def end_time():
    return time.time()

def format_time(start,end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    return hours, minutes, seconds