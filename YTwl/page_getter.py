from selenium import webdriver
from http.cookiejar import FileCookieJar
from os import environ

page = environ['HOME'] + "/.cache/ytfs/page.html"
prof_file = environ['HOME'] + "/.config/ytfs/profile.txt"

def main():
    prof = None
    with open(prof_file) as file:
        prof = file.read()[:-1]

    try:
        fireFoxOptions = webdriver.firefox.options.Options()
        # fireFoxOptions.headless = True
        fireFoxProfile = webdriver.FirefoxProfile(prof)
        fireFoxOptions.profile = fireFoxProfile
        brower = webdriver.Firefox(options=fireFoxOptions)

        brower.get('https://www.youtube.com/playlist?list=WL')
        with open(page, "w") as file:
            file.write(brower.page_source)

        brower.close()
    finally:
        try:
            brower.close()
        except:
            pass

if __name__ == "__main__":
    main()

