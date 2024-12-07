from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time
import random

search_queries = [
    "Python programming tutorials",
    "Latest technology trends 2024",
    "How to learn machine learning",
    "Top 10 programming languages",
    "Best laptops for coding",
    "Artificial intelligence applications",
    "What is cloud computing",
    "Web development frameworks comparison",
    "Data science project ideas",
    "Blockchain technology explained",
    "How to create a mobile app",
    "Best Python libraries for data analysis",
    "Front-end vs back-end development",
    "Career opportunities in AI",
    "Basics of cybersecurity",
    "Top freelancing websites for developers",
    "Best IDEs for Python programming",
    "Introduction to DevOps",
    "How to start a YouTube channel",
    "Tips for effective time management",
    "Best online coding bootcamps",
    "How to prepare for coding interviews",
    "What is quantum computing",
    "Guide to writing clean code",
    "How to build a portfolio website",
    "Latest advancements in robotics",
    "How to learn ethical hacking",
    "Best project management tools",
    "How to make money online",
    "Introduction to Internet of Things (IoT)"
]

temp = search_queries.copy()

#Paste your browser's WebDriver's address right here
address = r"Paste the path to WebDriver"

#Sets up the browser
service = Service(address)
browser = webdriver.Edge(service=service)
browser.maximize_window()


for i in range(30):
    #Opens up the search engine
    browser.get("https://www.bing.com")
    search = random.choice(temp)

    #Locates the search bar and enters the search query
    search_bar = browser.find_element(By.NAME, "q")
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)

    #5 seconds delay
    time.sleep(5)
    temp.remove(search)

    print(f"Search {i + 1}: {search}")
    print("Page Title:", browser.title)

#Resets the list again for another day
temp = search_queries.copy()
browser.quit()
