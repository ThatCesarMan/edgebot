from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "!edge-"
OWNER_IDS = [715259224367562762]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
        

    async def run(self, version):
        self.version = VERSION

        with open("./lib/bot/token.0", "r", encoding="utf=8")
        self.TOKEN = tf.read()

        print("Carregando...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect():
        print("Entramos no ar!")

    async def on_disconnect():
        print("Saímos. :(")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(809573354054746162)
            print("Estamos preparados!")

        elif:
            print("Reconectamos!")

    async def on_message(self, message):
        pass


bot = Bot()