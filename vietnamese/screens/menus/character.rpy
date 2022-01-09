﻿# TODO: Translation updated at 2021-12-24 07:09

translate vietnamese strings:

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"

    # game/screens/menus/character.rpy:45
    old "{gold}--- State ---{/gold}"
    new "{gold}--- State ---{/gold}"

    # game/screens/menus/character.rpy:53
    old "{color=#d26a6a}Health:{/color}"
    new "{color=#d26a6a}Health:{/color}"

    # game/screens/menus/character.rpy:54
    old "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"
    new "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"

    # game/screens/menus/character.rpy:55
    old "\n{gold}--- Mental State ---{/gold}"
    new "\n{gold}--- Mental State ---{/gold}"

    # game/screens/menus/character.rpy:63
    old "Sanity:\nCorruption:"
    new "Sanity:\nCorruption:"

    # game/screens/menus/character.rpy:64
    old "[player.sanity]%\n[player.corruption]%"
    new "[player.sanity]%\n[player.corruption]%"

    # game/screens/menus/character.rpy:65
    old "\n{gold}--- Physical Stats ---{/gold}"
    new "\n{gold}--- Physical Stats ---{/gold}"

    # game/screens/menus/character.rpy:73
    old "Strength:\nAgility:\nVitality:"
    new "Strength:\nAgility:\nVitality:"

    # game/screens/menus/character.rpy:74
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]"

    # game/screens/menus/character.rpy:75
    old "\n{gold}--- Mental Stats ---{/gold}"
    new "\n{gold}--- Mental Stats ---{/gold}"

    # game/screens/menus/character.rpy:83
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Intelligence:\nWisdom:\nCharisma:"

    # game/screens/menus/character.rpy:84
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]"

    # game/screens/menus/character.rpy:85
    old "\n{gold}--- Other ---{/gold}"
    new "\n{gold}--- Other ---{/gold}"

    # game/screens/menus/character.rpy:93
    old "Luck:"
    new "Luck:"

    # game/screens/menus/character.rpy:94
    old "[player.luck]"
    new "[player.luck]"

    # game/screens/menus/character.rpy:99
    old "\n{gold}--- Buffs ---{/gold}"
    new "\n{gold}--- Buffs ---{/gold}"

