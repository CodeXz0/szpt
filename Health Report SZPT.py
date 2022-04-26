import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

def autofile(user,passwd):
    
    chromedriver=r'.\driver.exe'
    web=webdriver.Chrome(chromedriver)

    url = "https://ehall.szpt.edu.cn/publicappfile/sys/szptpubxsjkxxbs/index.do?openflag&THEME=indigo#/mrxxbs"
    web.get(url)
    time.sleep(1)
#登录功能
    text=web.find_element_by_css_selector("input[id='username'")
    text.send_keys(user)
    password=web.find_element_by_css_selector("input[id='password'")
    password.send_keys(passwd)
    password.send_keys(Keys.ENTER)
    time.sleep(2)#等待加载按钮
#点击填报
    input_dj=web.find_element_by_css_selector("button[class='bh-btn bh-btn-primary'")
    input_dj.click()
#勾选复选框
    time.sleep(5)
    submit=web.find_element_by_css_selector("input[data-caption='我承诺：以上填报信息真实准确，无瞒报误报！'")
    submit.send_keys(Keys.SPACE)
    time.sleep(1)
    submit.send_keys(Keys.SPACE)
    submit.click()
#提交
    input_dj=web.find_element_by_css_selector('button[data-action="submit"]')
    time.sleep(1)#等待两秒等待定位
    input_dj.click()
    time.sleep(0.5)
#再次提交
    input_dj=web.find_element_by_css_selector('a[class="bh-dialog-btn bh-bg-primary bh-color-primary-5"]')
    input_dj.click()  
    time.sleep(1)
    print("填报完了欧~")
user=eval(input('请输入学号欧~：'))
passwd=str(input('请输入密码欧~：'))
autofile(user,passwd)

# 设计初衷:解放双手
# 因疫情原因，深职院要求学生每天填写健康填报
# 程序使用利用web driver定位网页元素进行操作
# By:CodeXz
# 更新时间2022.4.21
