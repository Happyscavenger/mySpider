from random import choice


class Use_Agent(object):

    def __init__(self):
        self.user_agent_pool = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"]

    def choice_usa(self):
        use_agent = choice(self.user_agent_pool)
        yield use_agent

if __name__ == '__main__':
    ua = Use_Agent()
    ua.choice_usa()

