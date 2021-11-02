# Creates log messages and writes them to a text file

def write_log(filename, level, msg):
    with open(filename, 'a') as log_file:
        log_file.write(f'[{level}] {msg}\n')

def critical(msg):
    write_log("CRITICAL", msg)

def error(msg):
    write_log("ERROR", msg)

def warn(msg):
    write_log("WARNING", msg)

def info(msg):
    write_log("INFO", msg)

def debug(msg):
    write_log("DEBUG", msg)


# Reference: 
# Badenhurst, Wessel. "Chapter 2: The Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_2