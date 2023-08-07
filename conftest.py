from selenium import webdriver
import pytest
import logging


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_configure():

    logging.basicConfig(filename='test_run.log',
                        filemode='a+', format='%(created)f - %(levelname)s - %(message)s',
                        level=logging.INFO
                        )
