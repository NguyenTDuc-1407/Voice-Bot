#
# from datetime import datetime
#
# now = datetime.now() # current date and time
#
# a = str(9)
# b = now.strftime(a)
# date_time = now.strftime("%H:%M")
# c = str(date_time)
# print("date and time:",date_time)
# print(c)
# print(b)

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.youtube.com/")
#
# search_box = driver.find_element('xpath', '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
# search_box.send_keys('everything goes on')
#
# search_button = driver.find_element('xpath', '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
# search_button.click()
#
# time.sleep(2)
# driver.find_element('xpath', '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
#
# time.sleep(1000)




# from datetime import datetime
#
# # Dạng string time
# x = input()
# y = input()
# date_string = x+':'+y
# now = datetime.now()
# # Strptime
# format = '%H:%M'
# date_time_python = datetime.strptime(date_string, format)
# print(date_time_python)
# now_time = now.strftime("%H:%M")
# a = date_time_python-now_time
# print(a)

from datetime import datetime
now = datetime.now()
d0 = now.strftime("%m/%d")
d1 = datetime.datetime.strptime('09/06', '%m/%d')
delta = abs(d0 - d1)
print(delta.days)

