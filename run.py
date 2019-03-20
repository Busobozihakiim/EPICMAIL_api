from api import create_app
from flask_jwt_extended import JWTManager

app = create_app('development')
jwt = JWTManager(app)
if __name__ == '__main__':
    app.run(debug=True)