import logger
try:
    a = 1 / 0
except:
    logger.error("zero division error")



# Reference: 
# Badenhurst, Wessel. "Chapter 2: The Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_2