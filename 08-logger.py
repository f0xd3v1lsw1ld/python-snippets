#!/usr/bin/env python

# simple example of python logging module
# for more see:
# python 2.x https://docs.python.org/2/howto/logging.html
# python 3.x https://docs.python.org/3/howto/logging.html

__author__="f0xd3v1lsw1ld@gmail.com"

import time
import logging


class App:

  def __init__(self, logfile):

    self.logfile = logfile

    # create logger object and define default log level
    self.logger = logging.getLogger('example_logger')
    self.logger.setLevel(logging.DEBUG)

    # create console handler of type StreamHandler and set level to info
    # only INFO logs and higher logs are print to the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)

    #create logging formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(name)s: %(message)s')

    #add FORMATTER to both handlers
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add both handler to logger
    self.logger.addHandler(ch)
    self.logger.addHandler(fh)
    #start logging, only in the logfile
    self.logger.debug("start")
    return

  def run(self):
      #this will be printed on the console and to the logfile
      self.logger.critical("This is a critical message")
      #this will be printed on the console and to the logfile
      self.logger.error("This is an error message")
      #this will be printed on the console and to the logfile
      self.logger.warning("This is a warning message")
       #this will be printed on the console and to the logfile
      self.logger.info("This is an info message")
       #this will be printed only on the console
      self.logger.debug("This is a debug message")

if __name__ == '__main__':
    App("example.log").run()
