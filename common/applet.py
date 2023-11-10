import re
import bs4
import requests
from gptbase import base, const


BASIC_CHAT_PARAMS = base.CompletionParameters(stream=True, model=const.GPT_35_TURBO_1106)


class Applet:
    def __init__(self, name: str, system_prompt: str, prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.prompt = prompt

    def ask(
        self,
        content,
        chat_params: base.CompletionParameters = BASIC_CHAT_PARAMS,
    ):
        assistant = base.BaseChat()

        chat_comp = assistant.ask(
            self.prompt.format(content=content),
            system_prompt=self.system_prompt,
            params=chat_params,
        )

        return chat_comp


def is_gpts_url(url):
    pattern = r'https:\/\/chat\.openai\.com\/g\/[a-zA-Z0-9-]+'
    
    if re.match(pattern, url):
        return True
    else:
        return False


def extract_info_from_link(link_url: str):
    if not is_gpts_url(link_url):
        return

    wb_content = requests.get(link_url)
    soup = bs4.BeautifulSoup(wb_content.text)
    image_url = soup.select_one('img').get('src')
    name_e = soup.find('div', class_='text-center text-2xl font-medium')
    name = name_e.text
    desc_e = name_e.find_next()
    description = desc_e.text
    return {
        'name': name,
        'description': description,
        'image_url': image_url,
        'link_url': link_url
    }
