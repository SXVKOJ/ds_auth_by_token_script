import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

TOKEN = ''

PATH_TO_DRIVER = 'C:\\Users\\di251\\Documents\\chromedriver\\chromedriver.exe'

JS_CODE = '''
function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"${token}"`;
    }, 50);

    setTimeout(() => {
        location.reload();
    }, 2500);
}
'''

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def login(token: str) -> None:
    driver.get("https://discord.com/login") 

    try:
        driver.execute_script(JS_CODE + f'\nlogin("{token}")')
    except Exception as e:
        print(e)


def main() -> None:
    login(TOKEN)


if __name__ == "__main__":
    main()
