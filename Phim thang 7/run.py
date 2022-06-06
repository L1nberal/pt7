from phim import app


if __name__ == '__main__':
    app.run(debug=True)


# Lệnh python database:
# from phim import db
# from phim.models import User
# User.query.get(2)
# User.query.all()
# User.query.filter_by(username='linh') 
# user3= User(username='Linhcute', email='Linh@linh.com', password='password')
# user3