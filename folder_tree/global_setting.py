import sys
import os

__author__ = 'jbui'

# from enum import Enum, unique
USER_COMPANY_ADMIN = 0
USER_WORKER = 1
USER_READONLY = 2

USER_PRIVELAGE = ((USER_COMPANY_ADMIN, 'Administrated Access'),
                  (USER_WORKER, 'Write Access'),
                  (USER_READONLY, 'View Access'))

if sys.platform == 'nt' or sys.platform == 'win32':
    LOCATION_APPLICATION_ANACONDA_PYTHON = r"C:\Anaconda\python.exe"
elif sys.platform == 'linux' or sys.platform == 'linux2':
    LOCATION_APPLICATION_ANACONDA_PYTHON = os.path.join('usr', 'bin', 'python27')

if sys.platform == 'nt' or sys.platform == 'win32':
    LOCATION_APPLICATION_WHAM = r"C:\DEVEL\wam\wam\wham.py"
elif sys.platform == 'linux' or sys.platform == 'linux2':
    LOCATION_APPLICATION_WHAM = os.path.join(os.sep, "home", "jbui", "DEVEL", "pec_ssh", "pec_ssh", "p_ssh.py")

if sys.platform == 'nt' or sys.platform == 'win32':
    LOCATION_USER_STORAGE = r"C:\STORAGE"
elif sys.platform == 'linux' or sys.platform == 'linux2':
    LOCATION_USER_STORAGE = os.path.join(os.sep, "home", "jbui", "DEVEL", "pec_ssh", "pec_ssh", "temp")

if sys.platform == 'nt' or sys.platform == 'win32':
    LOCATION_TEST_USER_STORAGE = r"C:\STORAGE\TEST_USER"
elif sys.platform == 'linux' or sys.platform == 'linux2':
    LOCATION_TEST_USER_STORAGE = os.path.join(os.sep, "home", "jbui", "TEST")

# Job Type
JOB_TYPE_TEXT_WHAM = 0

JOB_TYPE = ((JOB_TYPE_TEXT_WHAM, "Wham"),)

# Job Status
JOB_STATUS_TEXT_CREATED = 0
JOB_STATUS_TEXT_QUEUE = 1
JOB_STATUS_TEXT_STAGED = 2
JOB_STATUS_TEXT_RUNNING = 3
JOB_STATUS_TEXT_COMPLETED = 4
JOB_STATUS_TEXT_ERROR = 5

JOB_STATUS = ((JOB_STATUS_TEXT_CREATED,     "Created"),
              (JOB_STATUS_TEXT_QUEUE,       "Queue"),
              (JOB_STATUS_TEXT_STAGED,      "Staged"),
              (JOB_STATUS_TEXT_RUNNING,     "Running"),
              (JOB_STATUS_TEXT_COMPLETED,   "Completed"),
              (JOB_STATUS_TEXT_ERROR,       "Error In Running"))

# Type
FILE_TYPE_UNKNOWN = -1
FILE_TYPE_TXT = 0

FILE_TYPE_PNG = 1
FILE_TYPE_JPG = 2
FILE_TYPE_JPEG = 3
FILE_TYPE_GIF = 4
FILE_TYPE_BMP = 5

FILE_TYPE_MPG = 6
FILE_TYPE_MPEG = 7
FILE_TYPE_MOV = 8
FILE_TYPE_AVI = 9
FILE_TYPE_WMV = 10

FILE_TYPE_CSV = 11
FILE_TYPE_PDF = 12
FILE_TYPE_XLS = 13
FILE_TYPE_XLSX = 14
FILE_TYPE_DOC = 15
FILE_TYPE_DOCX = 16
FILE_TYPE_PPT = 17
FILE_TYPE_PPTX = 18

             #ID,                   #extention      #MIME
FILE_LIST = ((FILE_TYPE_TXT,        'txt',          'text/plain'),

             (FILE_TYPE_PNG,        'png',          'image/png'),
             (FILE_TYPE_JPG,        'jpg',          'image/jpeg'),
             (FILE_TYPE_JPEG,       'jpeg',         'image/jpeg'),
             (FILE_TYPE_GIF,        'gif',          'image/gif'),
             (FILE_TYPE_BMP,        'bmp',          'image/bmp'),

             (FILE_TYPE_MPG,        'mpg',          'video/mpeg'),
             (FILE_TYPE_MPEG,       'mpeg',         'video/mpeg'),
             (FILE_TYPE_MOV,        'mov',          'video/qt'),
             (FILE_TYPE_AVI,        'avi',          'video/x-msvideo'),
             (FILE_TYPE_WMV,        'wmv',          'video/x-ms-wmv'),

             (FILE_TYPE_CSV,        'csv',          'text/csv'),
             (FILE_TYPE_PDF,        'pdf',          'application/pdf'),
             (FILE_TYPE_XLS,        'xls',          'application/vnd.ms-excel'),
             (FILE_TYPE_XLSX,       'xlsx',         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
             (FILE_TYPE_DOC,        'doc',          'application/msword'),
             (FILE_TYPE_DOCX,       'docx',         'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
             (FILE_TYPE_PPT,        'ppt',          'application/vnd.ms-powerpoint'),
             (FILE_TYPE_PPTX,       'pptx',         'application/vnd.openxmlformats-officedocument.presentationml.slideshow'),

             (FILE_TYPE_UNKNOWN,    "unknown",      'text/plain'))

IMAGE_TYPE = (
    (FILE_TYPE_PNG,        'png'),
    (FILE_TYPE_JPG,        'jpg'),
    (FILE_TYPE_JPEG,       'jpeg'),
    (FILE_TYPE_GIF,        'gif'),
    (FILE_TYPE_BMP,        'bmp'),
)

FILE_TYPE = ((FILE_TYPE_TXT,        'txt'),

             (FILE_TYPE_PNG,        'png'),
             (FILE_TYPE_JPG,        'jpg'),
             (FILE_TYPE_JPEG,       'jpeg'),
             (FILE_TYPE_GIF,        'gif'),
             (FILE_TYPE_BMP,        'bmp'),

             (FILE_TYPE_MPG,        'mpg'),
             (FILE_TYPE_MPEG,       'mpeg'),
             (FILE_TYPE_MOV,        'mov'),
             (FILE_TYPE_AVI,        'avi'),
             (FILE_TYPE_WMV,        'wmv'),

             (FILE_TYPE_CSV,        'csv'),
             (FILE_TYPE_PDF,        'pdf'),
             (FILE_TYPE_XLS,        'xls'),
             (FILE_TYPE_XLSX,       'xlsx'),
             (FILE_TYPE_DOC,        'doc'),
             (FILE_TYPE_DOCX,       'docx'),
             (FILE_TYPE_PPT,        'ppt'),
             (FILE_TYPE_PPTX,       'pptx'),

             (FILE_TYPE_UNKNOWN,    "unknown"))


def get_mime(tid):
    """
    Get the mime type.
    :param tid:
    :return:
    """
    for ids, ext, mimes in FILE_LIST:
        if ids == tid:
            return mimes


def get_mime_from_extention(extention):
    """

    :param extention:
    :return:
    """
    for ids, ext, mimes in FILE_LIST:
        if ext == extention:
            return mimes