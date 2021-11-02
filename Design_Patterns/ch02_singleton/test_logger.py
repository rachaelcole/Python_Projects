from logger_singleton import Logger

logger = Logger('logger_singleton.txt')

logger.info("This is an info message")
logger.debug("This is a debug message")




# Reference: 
# Badenhurst, Wessel. "Chapter 2: The Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_2