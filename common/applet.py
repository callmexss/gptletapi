from gptbase import basev2


BASIC_CHAT_PARAMS = basev2.CompletionParameters(stream=True)


class Applet:
    def __init__(self, name: str, system_prompt: str, prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.prompt = prompt
    
    def ask(
        self,
        content,
        chat_params: basev2.CompletionParameters = BASIC_CHAT_PARAMS,
    ):
        assistant = basev2.Assistant()

        chat_comp = assistant.ask(
            self.prompt.format(content=content),
            system_prompt=self.system_prompt,
            params=chat_params
        )

        return chat_comp
