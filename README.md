DjangoWAWSLogging
=================

Windows Azure Websites logging with Django.

Sample application demonstrating how to write to a log file on Django 
applications hosted on Windows Azure Websites.

This project was created with Visual Studio 2012 and Python Tools for Visual
Studio 2.0 Beta.

It uses ConcurrentLogHandler so that multiple instances can write to the same
log file. This requires PyWin32.

On the Windows Azure Website configuration, in the app settings section, there
must be an entry named "LOGFILE" with a value such as 
"D:\home\logfiles\django.log".

Windows Azure log streaming will display log information written to any file
in "D:\home\logfiles". At this time this is not working reliably with 
ConcurrentLogHandler, possibly, because the file stays open.

The log file also can't be downloaded via FTP: there is an error message
"550 The process cannot access the file because it is being used by another process."

If the website is stopped, the log files are flushed and closed and can be downloaded.
