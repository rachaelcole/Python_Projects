# Defines a Logger object class using the Singleton design pattern that can be used to log messages to a text file

from datetime import datetime

class Logger(object):
    # Private class
    class __Logger():
        def __init__(self, file_name):
            """Return a logger object whose file_name is *file_name*"""
            self.file_name = file_name
        def __str__(self):
            return f"{self!r} {self.val}"
        def _write_log(self, level, msg):
            """Writes a message to the file_name for a specific logger instance"""
            with open(self.file_name, 'a') as log_file:
                datestamp = datetime.now()
                log_file.write(f'[{datestamp.strftime("%d-%m-%Y %H:%M:%S.%f %Z")}] [{level}] {msg}\n')
        def critical(self, msg, level='CRITICAL'):
            self._write_log(level, msg)
        def error(self, msg, level='ERROR'):
            self._write_log(level, msg)
        def warn(self, msg, level='WARNING'):
            self._write_log(level, msg)  
        def info(self, msg, level='INFO'):
            self._write_log(level, msg)
        def debug(self, msg, level='DEBUG'):
            self._write_log(level, msg)
    # Class attribute 'instance'
    instance = None
    # Class method
    def __init__(self, file_name):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(file_name)
        else:
            Logger.instance.file_name = file_name
    # Magic methods
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)



# Reference: 
# Badenhurst, Wessel. "Chapter 2: The Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 