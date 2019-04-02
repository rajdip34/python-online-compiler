import os, sys
import site, time, signal

sys.stdout = sys.stderr

new_path = '/media/mnt/env/INDEXAPP/lib/python2.7/site-packages'

prev_sys_path = list(sys.path)

site.addsitedir(new_path)
# add the app's directory to the PYTHONPATH
sys.path.append('/media/mnt/repo/dhiraj/')
sys.path.append('/var/www')


# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'tajrummy.settings'

from django.core.wsgi import get_wsgi_application

#from django.core.handlers.wsgi import WSGIHandler
#application = WSGIHandler()

try:
    application = get_wsgi_application()
except Exception:
    time.sleep(0.25)
    os.kill(os.getpid(), signal.SIGINT)
application = get_wsgi_application()
