# 
import os
import sys
sys.path.insert(0, '/var/www/env/Flas')

from flaskr import create_app 

application = create_app()
application.root_path = '/var/www/env/Flas'
#application.secret_key = 'any secret string'
