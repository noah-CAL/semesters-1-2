import pyperclip

emoji = input('Enter the emoji (e.g. 🙊): ').lower()
emoji_name = input('Enter the emoji name (e.g. monke): ')

str = f"{emoji} is the WORST emoji! It's horrendous and ugly. I hate it. The point of emojis is to show emotions, but what emotion does this show? Do you just wake up in the morning and think \"wow, I really feel like a massive fucking {emoji_name} today\"? It's useless. I hate it. It just provokes a deep rooted anger within me whenever I see it. I want to drive on over to the fucking emoji headquarters and kill it. If this was the emoji movie I'd push it off a fucking cliff. People just comment {emoji} as if it's funny. It's not. {emoji} deserves to die. He deserves to have his smug little {emoji_name} face smashed in with a hammer. Oh wow, it's a {emoji_name}, how fucking hilarious, I'll use it in every comment I post. NO. STOP IT. It deserves to burn in hell. Why is it so goddamn smug. You're a fucking {emoji_name}, you have no life goals, you will never accomplish anything in life apart from pissing me off. When you die no one will mourn. I hope you die."

pyperclip.copy(str)
print(str, '\n\nCopied to clipboard!')
