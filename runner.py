from UCAS教务处 import jiaowuchu

jiaowuchu = jiaowuchu()
jiaowuchu.openBrowser("google")
#多用户登陆
login_list = ["********"]#此处修改用户名
for username in login_list:
    jiaowuchu.login(username,"******")#此处修改密码

