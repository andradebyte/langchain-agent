import re

async def remove_md(message: str) -> str:
    pattern:str = r"[*_~`#>+|\\]|\n"
    replacement:str = ""
    msg: str = re.sub(pattern, replacement, message)
    return msg