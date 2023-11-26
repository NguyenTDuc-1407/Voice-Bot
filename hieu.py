# you = "124"
#
# if you =="":
#     robot_brain="aasd"
# elif you=="hello":
#     robot_brain="hello acs"
# elif you=="day":
#     robot_brain = ""
# else:
#     robot_brain="try"
# print(robot_brain)
# import webbrowser
#
# webbrowser.open_new_tab("http://www.google.com")

from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://google.co.in")
