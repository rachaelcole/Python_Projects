class SingletonObject(object):
    # Private class
    class __SingletonObject():
        def __init__(self):
            self.val = None
        def __str__(self):
            return f"{self!r} {self.val}"
        def _write_log(self, level, msg):
            """Writes a message to the file_name for a specific logger instance"""
            with open(self.file_name, 'a') as log_file:
                log_file.write(f'[{level}] {msg}\n')
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
    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance
    # Magic methods
    def __getattr__(self,name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)




# Reference: 
# Badenhurst, Wessel. "Chapter 2: Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_2