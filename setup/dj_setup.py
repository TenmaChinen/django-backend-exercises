import django ,os, sys

current_path = os.path.dirname(__file__)
top_path = os.path.dirname(current_path)
sys.path.append(top_path + '/mock-project/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
