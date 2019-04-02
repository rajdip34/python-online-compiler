import django
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
#sys.path.append('/Users/dhirajgarg/project/indexappdjango/')


sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = "indexapp.settings"
django.setup()








