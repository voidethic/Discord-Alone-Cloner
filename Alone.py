from utils.innit import *
from func.cloner import *
from func.clone_stickers import *
from func.clone_emojis import *
from func.guild_info import *
from func.token_checker import *

async def menu():
    while True:
        clear()
        logo()
        o = f"""
                {w}[{r}01{w}]{r} Clone Server    {w}[{r}04{w}]{r} Server Info
                {w}[{r}02{w}]{r} Clone Sticker's {w}[{r}05{w}]{r} Token Checker
                {w}[{r}03{w}]{r} Clone Emoji's"""
        print(o)
        cs = input(f"                {w}[{r}ALONE{w}]{r} >> ")

        if cs == "1":
            await cloner()
        elif cs == "2":
            await sticker_cloner()
        elif cs == "3":
            await emoji_cloner()
        elif cs == "4":
            await guild_info()
        elif cs == "5":
            await token_checker()


if __name__ == "__main__":
    asyncio.run(menu())