## @package Log
#  Provides logging functionality
#
#  @author Kevin Wierman
#
#  Typical usage is to:
#    - Set the logfile:
#      - Log.set_logger_file("yourlogfile.log") 
#    - Log a header:
#      - Log.log(Log.Severity.Header, "Your Header")
#    - Log a line:
#      - Log.log_line()
#    - Log a normal message:
#      - Log.log(Log.Severity.Normal, "Your Message")
#    - Etc...

import time
import Common
import os

## Denotes the severity of the message
Severity = Common.enum(Header=0, Normal=1, OK=2, Warning=3, Fail=4)

_logger_output_file=None
_logfile_name='log.log'

## Opens a file for logging output. 
#  @warning This overwrites the current
#  @param name the name of the output file. No formatting done
def set_logger_file(name = "log.log"):
	global _logger_output_file
	global _logfile_name
	_logfile_name=name
	_logger_output_file = open(_logfile_name,'w')

_colors = ["\033[95m","\033[94m","\033[92m","\033[93m","\033[91m","\033[0m"]

## Logs a message to the terminal with the given severity and outputs to file if, already set
#  @note Each line in the log file will be tagged with the date and time
#  @param severity Use the Severity enum to set the severity of the message
#  @param message The message to be logged
def log(severity=Severity.Normal, message=""):
	global _logger_output_file
	tmpmessage=str(message)
	for i in range(severity):
		tmpmessage='  '+tmpmessage
	print _colors[severity], tmpmessage,_colors[5]
	tmpmessage+="\r\n"
	if (type(_logger_output_file)!=type(None)):
		timestamp="["+time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+"] "
		_logger_output_file.write(timestamp+tmpmessage)
		_logger_output_file.flush()
		os.fsync(_logger_output_file)

## Creates a line 67 characters long
#  The Severity this is set to is header
def log_line():
	log(Severity.Header,"-------------------------------------------------------------------")

## The debug function for this module
def _debug():
	log_line()
	log(Severity.Header, "This is a Header")
	log(Severity.Normal, "This is Body Text")
	log(Severity.OK, "This is Positive Feedback")
	log(Severity.Warning, "This is a Warning")
	log(Severity.Fail, "This is a Failure")
	log_line()
	set_logger_file("debug.txt")
	log_line()
	log(Severity.Header, "This is a Header")
	log(Severity.Normal, "This is Body Text")
	log(Severity.OK, "This is Positive Feedback")
	log(Severity.Warning, "This is a Warning")
	log(Severity.Fail, "This is a Failure")
	log_line()





	
