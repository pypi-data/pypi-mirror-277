from cookiebot import CookieAPI
import asyncio

api = CookieAPI(api_key="cb26f209-f2b4-4a25-af61-9a7ca1e9663b")


USER_ID = 203208036053942272
GUILD_ID = 1010915072694046794


async def start():
    async with api as test:
        member_count = await test.get_member_count(GUILD_ID)
        print(member_count)
        user_stats = await test.get_user_stats(USER_ID)
        print(user_stats)
        member_stats = await test.get_member_stats(USER_ID, GUILD_ID)
        print(member_stats)
        member_activity = await test.get_member_activity(USER_ID, GUILD_ID)
        print(member_activity)
        guild_activity = await test.get_guild_activity(GUILD_ID)
        print(guild_activity)
        guild_image = await test.get_guild_image(GUILD_ID)
        print(guild_image)
        guild_image = await test.get_member_image(USER_ID, GUILD_ID)
        print(guild_image)

    # await test.close()

asyncio.run(start())
