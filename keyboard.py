from vkbottle import Keyboard, KeyboardButtonColor, Text


KEYBOARD_SELECT_RACE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Человек"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Демон"), color= KeyboardButtonColor.NEGATIVE)
    .add(Text("Эльф"))
    .get_json()
)

KEYBOARD_SELECT_ROLE = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Танк"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Хил"), color= KeyboardButtonColor.NEGATIVE)
    .add(Text("ДД"))
    .get_json()
)

KEYBOARD_CITY = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Воевать с монстрами"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Домой"), color= KeyboardButtonColor.NEGATIVE)
    .get_json()
)

KEYBOARD_IN_THE_COUNTRY = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Искать монстра"))
    .add(Text("В город"))
    .get_json()
)