# 正常场景
success_data = {'username': 'wudi19920122@163.com', 'password': 'wudi575093904<>?'}

# 异常场景
login_data = [
    {'username': '', 'password': 'wudi19920122', 'check': '请输入帐号'},
    {'username': 'windy_wudi', 'password': '', 'check': '请输入密码'},
    # {'username': '', 'password': '', 'check': '请输入帐号'},
    {'username': 'windy_wudi123', 'password': 'wudi19920122', 'check': '用户名或密码不正确'},
    {'username': 'windy_wudi', 'password': 'wudi19920122123', 'check': '用户名或密码不正确'}
]
