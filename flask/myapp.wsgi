import sys

# Add the directory containing your Flask app to the Python path
sys.path.insert(0, '/var/www/flask')

# Change to the directory containing your Flask app
# os.chdir('/var/www/flask')

from flask_server import app as application
