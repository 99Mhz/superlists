from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new website she
# goes to check out the homepage
browser.get("http://localhost:8000")

# she notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# she is invited to enter  a to-do item straight away

# she types "Buy peacock feathers" into a text box

# when she hits enter the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# there is still a text box inviting her to add another item.
# she enters "Use peacock feathers to make a fly"

# the page updates again and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees 
# that the site has generated a unique url for her -- there is some
# explanitory text to that effect

# She visits that URL - her to-do list is still there

# Satisfied, she goes back to sleep

browser.quit()



