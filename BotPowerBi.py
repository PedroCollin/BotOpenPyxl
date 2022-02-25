from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#driver.get("https://powerbi.bosch.com/publish")
driver.get("https://tube.video.bosch.com/")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.quit()
