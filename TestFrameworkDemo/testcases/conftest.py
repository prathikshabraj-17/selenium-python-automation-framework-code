import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def setup(browser, url):
    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        service = Service(r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)

    elif browser == "edge":
        service = Service(r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError("Unsupported browser: " + str(browser))
    driver.get(url)

    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
                # always add url to report
        extras.append(pytest_html.extras.url("https://www.spicejet.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("setup")  # Access driver fixture
            if driver:
                #only add additional html on failure
              report_directory = os.path.dirname(item.config.option.htmlpath)
              file_name = report.nodeid.replace("::", "_") + ".png"
              destinationFile = os.path.join(report_directory, file_name)
              driver.save_screenshot(destinationFile)
              if file_name:
                  html = (
                  f'<div><a href="{file_name}" target="_blank">'
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:600px;height:400px;" onclick="window.open(this.src)" /></div>'
                )
                  extras.append(pytest_html.extras.html(html))
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            report.extras = extras

def pytest_html_report_title(report):
    report.title = "Spicejet Report"