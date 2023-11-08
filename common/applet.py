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
