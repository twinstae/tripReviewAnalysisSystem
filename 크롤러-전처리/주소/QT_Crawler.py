import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException,StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
import re
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

