# Purpose is to record progress and problems
# debug, info, warning, error, critical

# dir() shows the inbuilts
# ALL CAPS are constants
# Capitalized are classes
# lower cases are methods

import logging
import math

# Create and configure logger. If file doesn't exist, python will create it
# basicConfig sets the default log level to WARNING = 30
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\Users\\Csirke\\greenfox\\Test Automation\\Python Practice\\logging.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")
logger = logging.getLogger()

# Test the logger
# Level    ||  Numeric Value
# NOTSET   ||  0
# DEBUG    ||  10
# INFO     ||  20
# WARNING  ||  30
# ERROR    ||  40
# CRITICAL ||  50

logger.info("First message.")
print(logger.level)

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info")
logger.warning("I'm sorry, but I can't do that.")
logger.error("Did you just try to divideby zero!?")
logger.critical("Extinction is nigh!")


def quadratic_formula(a, b, c):
    """Return the solution to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminent
    logger.debug("# Compute the discriminent")
    disc = b ** 2 - 4 * a * c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)


roots = quadratic_formula(1, 0, -4)
print(roots)
