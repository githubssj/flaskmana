from apps.models.user import MyUser


def get_user(user_ident):
    # 根据id获取
    user = MyUser.query.get(user_ident)
    if user:
        return user
    user = MyUser.query.filter(MyUser.phone == user_ident).first()
    if user:
        return user
    user = MyUser.query.filter(MyUser.username == user_ident).first()
    if user:
        return user

    return None
