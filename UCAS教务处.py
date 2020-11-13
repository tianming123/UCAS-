from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class jiaowuchu:
    '''
    教务处项目
    '''
    def __init__(self):
        self.driver = None
        #教务处登陆信息
        self.username = None
        self.pwd = None


    def openBrowser(self,browser="google"):
        if browser=="google":
            self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)
    def quitBrowser(self):
        self.driver.quit()

    def course_evaluate(self):
        #课程评价
        # 进入具体的课程评价
        # 修改tr[i]即可选择响应的课程
        self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[3]/div[2]/table/tbody/tr[9]/td[8]/a').click()
        # self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[3]/div[2]/table/tbody/tr[5]/td[8]/a').click()
        # 分数评价按钮
        Lbase = '//*[@id="regfrm"]/table/tbody/tr['
        Rbase = ']/td[1]/input'
        for i in range(3):
            xpath = Lbase + str(i + 2) + Rbase
            self.driver.find_element_by_xpath(xpath).click()
        for i in range(5):
            xpath = Lbase + str(i + 6) + Rbase
            self.driver.find_element_by_xpath(xpath).click()
        for i in range(3):
            xpath = Lbase + str(i + 12) + Rbase
            self.driver.find_element_by_xpath(xpath).click()
        # 文本评价部分
        self.driver.find_element_by_xpath('//*[@id="item_243"]').send_keys("这门课程我最喜欢教师的教学风格")
        self.driver.find_element_by_xpath('//*[@id="item_244"]').send_keys("我认为本课程应从课程课件方面需要进一步改进和提高？")
        self.driver.find_element_by_xpath('//*[@id="item_245"]').send_keys("我平均每周在这门课程上花费十个多小时")
        self.driver.find_element_by_xpath('//*[@id="item_246"]').send_keys("在参与这门课之前，我对这个学科领域不太了解")
        self.driver.find_element_by_xpath('//*[@id="item_247"]').send_keys("我对该课程的课堂参与度（保证出勤、积极回答问题等）")
        print('进入下一阶段')
        time.sleep(1)
        # 选择题
        self.driver.find_element_by_xpath('//*[@id="249"]').click()
        self.driver.find_element_by_xpath('//*[@id="255"]').click()

    def teacher_evalute(self):
        self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/ul/li[2]/a').click()
        teacher_xpath_left = '//*[@id="main-content"]/div/div[3]/div[2]/table/tbody/tr['
        teacher_xpath_right = ']/td[8]/a'

        for i in range(3):
            teacher_xpath = teacher_xpath_left+str(i+2)+teacher_xpath_right
            self.driver.find_element_by_xpath(teacher_xpath).click()
            #教师评分
            for i in range(2):
                self.driver.find_element_by_xpath('//*[@id="regfrm"]/table/tbody/tr['+str(i+2)+']/td[1]/input').click()

            for i in range(2):
                self.driver.find_element_by_xpath('//*[@id="regfrm"]/table/tbody/tr['+str(i+5)+']/td[1]/input').click()
            for i in range(6):
                self.driver.find_element_by_xpath('//*[@id="regfrm"]/table/tbody/tr['+str(i+8)+']/td[1]/input').click()
            i = 100
            for i in range(2, 10):  # 也可以设置一个较大的数，一下到底
                js = "var q=document.documentElement.scrollTop={}".format(i * 70)  # javascript语句
                self.driver.execute_script(js)
            self.driver.find_element_by_xpath('//*[@id="item_291"]').send_keys("这位老师的教学，我最喜欢教师的课堂互动")
            for i in range(6):
                self.driver.find_element_by_xpath('//*[@id="regfrm"]/table/tbody/tr['+str(i+15)+']/td[1]/input').click()
            for i in range(5):
                self.driver.find_element_by_xpath('//*[@id="regfrm"]/table/tbody/tr['+str(i+22)+']/td[1]/input').click()
            self.driver.find_element_by_xpath('//*[@id="item_292"]').send_keys("我对老师的意见和建议：可以适当增加课程案例")
            for i in range(5, 50):  # 也可以设置一个较大的数，一下到底
                js = "var q=document.documentElement.scrollTop={}".format(i * 100)  # javascript语句
                self.driver.execute_script(js)
            self.driver.find_element_by_xpath('//*[@id="sb1"]').click()
            self.driver.find_element_by_xpath('//*[@id="jbox-state-state0"]/div[2]/button[1]').click()






    def login(self,username,pwd):
        #登陆模块
        self.username=username
        self.pwd=pwd
        url = "https://onestop.ucas.edu.cn/home/index"
        self.driver.get(url)
        self.driver.implicitly_wait(10)#隐式等待
        self.driver.maximize_window()
        #教务处登陆部分
        username = self.driver.find_element_by_id("menhuusername").send_keys(self.username)
        pwd = self.driver.find_element_by_id("menhupassword").send_keys(self.pwd)
        click = self.driver.find_element_by_class_name("loginbtn").click()
        #进入选课系统
        url = self.driver.find_element_by_xpath('//*[@id="main-metro"]/ul/li[3]/a[3]').click()
        self.driver.switch_to.alert.accept()#点击跳出的确认框
        #进入课程评价
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]/a').click()
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]/ul/li/a').click()#选择秋季学期
        self.teacher_evalute()


    def clear(self):
        username = self.driver.find_element_by_id("menhuusername").clear()
        pwd = self.driver.find_element_by_id("menhupassword").clear()