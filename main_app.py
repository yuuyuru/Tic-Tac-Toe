from module import User, App

if __name__ == '__main__':
    user1 = User(1)
    user2 = User(2)

    app = App(first_user=user1, second_user=user2)
    app.play()
