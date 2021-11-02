class Logger(object):
    """A file-based message logger with the following properties:
        - Attributes: 
            - file_name: a string representing the full path of the log file to which this 
            logger will write its messages"""
    
    def __init__(self, file_name):
        """Return a logger object whose file_name is *file_name*"""
        self.file_name = file_name
    
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



# Reference: 
# Badenhurst, Wessel. "Chapter 2: The Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_2