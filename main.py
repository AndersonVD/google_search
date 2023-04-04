#  Código de busca para o Google / Projeto Workana by Anderson Viana
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

BUSCA = "naruto"  # palavra-chave para a busca
LOOPS = 3  # número de loops para a busca
URL = "https://www.netflix.com/br/title/70205012"  # URL para a busca


def loop_links(BUSCA, LOOPS, URL):
    # loop para procurar a URL na página de resultados de busca
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # navega para o www.google.com
    driver.get("https://www.google.com")

    # localiza o campo de busca, insere a palavra-chave e executa a busca
    search_field = driver.find_element_by_name("q")
    search_field.send_keys(BUSCA)
    search_field.send_keys(Keys.RETURN)
    for i in range(LOOPS):
        try:
            if not driver.find_element_by_css_selector(f'a[href*="{URL}"]'):
                print("Não encontrado na página atual")
            url_element = driver.find_element_by_css_selector(f'a[href*="{URL}"]')
            driver.execute_script(
                "window.open('{}', '_blank');".format(url_element.get_attribute("href"))
            )
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(e)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.quit()


if __name__ == "__main__":
    loop_links(BUSCA, LOOPS, URL)
