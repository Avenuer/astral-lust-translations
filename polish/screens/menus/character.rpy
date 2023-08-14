﻿# TODO: Translation updated at 2021-05-15 22:53

translate polish strings:

    # game/screens/menus/character.rpy:27
    old "{color=#A71930}Health{/color} - how much damage you can take.\n\n{color=#C6E2FF}Spirituality{/color} - consumed when using cards in combat. Recovers at the beginning of new turn."
    new "{color=#A71930}Zdrowie{/color} - ile obrażeń możesz przyjąć.\n\n{color=#C6E2FF}Duchowość{/color} - zużywane podczas używania kart w walce. Regeneruje się na początku nowej tury.{#mtl}{#tl}"

    # game/screens/menus/character.rpy:31
    old "{color=#A71930}Health:{/color}\n{color=#C6E2FF}Spirituality:{/color}"
    new "{color=#A71930}Zdrowie:{/color}\n{color=#C6E2FF}Duchowość:{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:32
    old "{color=#A71930}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}"
    new "{color=#A71930}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:33
    old "\n{color=#FFD700}--- Mental State ---{/color}"
    new "\n{color=#FFD700}--- Stan psychiczny ---{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:37
    old "{color=#DAD1BF}Sanity{/color} - how capable of logical reasoning you are. Reaching 0% leads to game over.\n\n{color=#800080}Corruption{/color} - how degenerated you are. Reaching 100% leads to game over."
    new "{color=#DAD1BF}Poczytalność{/color} - na ile jesteś zdolny do logicznego rozumowania. Osiągnięcie 0% prowadzi do końca gry.\n\n{color=#800080}Korupcja{/color} - jak bardzo jesteś zdegenerowany. Osiągnięcie 100% prowadzi do końca gry.{#mtl}{#tl}"

    # game/screens/menus/character.rpy:41
    old "Sanity:\nCorruption:"
    new "Poczytalność:\nZniszczenie:{#mtl}{#tl}"

    # game/screens/menus/character.rpy:42
    old "[player.sanity]%\n[player.corruption]%"
    new "[player.sanity]%\n[player.corruption]%{#mtl}{#tl}"

    # game/screens/menus/character.rpy:43
    old "\n{color=#FFD700}--- Physical Stats ---{/color}"
    new "\n{color=#FFD700}--- Statystyki fizyczne ---{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:47
    old "{color=#F4C25E}Strength{/color} - increases damage dealt in combat by 1 every 5 points.\n\n{color=#32CD32}Agility{/color} - every point gives 1% of avoiding damage and increases chance to escape combat by 2%.\n\n{color=#A71930}Vitality{/color} - every point increases your maximum health by 3.\n\nIncreased at the gym."
    new "{color=#F4C25E}Siła{/color} - zwiększa obrażenia zadawane w walce o 1 co 5 punktów.\n\n{color=#32CD32}Zwinność{/color} - każdy punkt daje 1% obrażeń do uniknięcia i zwiększa szansę na ucieczkę od walki o 2%.\n\n{color=#A71930}Żywotność{/color} - każdy punkt zwiększa twoje maksymalne zdrowie o 3.\n\nZwiększone na siłowni.{#mtl}{#tl}"

    # game/screens/menus/character.rpy:51
    old "Strength:\nAgility:\nVitality:"
    new "Siła:\nZwinność:\nWitalność:{#mtl}{#tl}"

    # game/screens/menus/character.rpy:52
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]{#mtl}{#tl}"

    # game/screens/menus/character.rpy:53
    old "\n{color=#FFD700}--- Mental Stats ---{/color}"
    new "\n{color=#FFD700}--- Statystyki mentalne ---{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:57
    old "{color=#B29EC1}Intelligence{/color} - coming soon.\n\n{color=#C6E2FF}Wisdom{/color} - every 10 point increase maximum spirituality by 1 point.\n\n{color=#FF958F}Charisma{/color} - no effect on combat. Used to make others agree with you during conversation.\n\nIncreased in the player room."
    new "{color=#B29EC1}Inteligencja{/color} - wkrótce.\n\n{color=#C6E2FF}Mądrość{/color} - co 10 punktów zwiększa maksymalną duchowość o 1 punkt.\n\n{color=#FF958F}Charyzma{/color} - brak wpływu na walkę Używane, aby inni zgodzili się z tobą podczas rozmowy.\n\nWiększość w pokoju gracza.{#mtl}{#tl}"

    # game/screens/menus/character.rpy:61
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Inteligencja:\nMądrość:\nCharyzma:{#mtl}{#tl}"

    # game/screens/menus/character.rpy:62
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]{#mtl}{#tl}"

    # game/screens/menus/character.rpy:63
    old "\n{color=#FFD700}--- Other ---{/color}"
    new "\n{color=#FFD700}--- Inne ---{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:67
    old "{color=#E4CA48}Luck{/color} - increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.\n\nCard draw - amount of cards you start your round with.\n\nMax hand - amount of cards you can hold simultaneously in combat."
    new "{color=#E4CA48}Szczęście{/color} - zwiększa szansę na dobre karty, zmniejsza szansę na spotkanie silnych przeciwników. Zwiększona za pomocą kodów z Discorda lub handlu z określonymi istotami.\n\nDobieranie kart — liczba kart, z którymi rozpoczynasz rundę.\n\nMaksymalna ręka — liczba kart, które możesz trzymać jednocześnie w walce.{#mtl}{#tl}"

    # game/screens/menus/character.rpy:71
    old "Luck:\nCard draw:\nMax hand:"
    new "Szczęście:\nDobieranie kart:\nMaksymalna ręka:{#mtl}{#tl}"

    # game/screens/menus/character.rpy:72
    old "[player.luck]\n[player.card_draw]\n[player.max_hand]"
    new "[player.luck]\n[player.card_draw]\n[player.max_hand]{#mtl}{#tl}"

# TODO: Translation updated at 2021-07-11 16:45

translate polish strings:

    # game/screens/menus/character.rpy:32
    old "{color=#d26a6a}Health{/color} - how much damage you can take.\n\n{color=#C6E2FF}Spirituality{/color} - consumed when using cards in combat. Recovers at the beginning of new turn."
    new "{color=#d26a6a}Zdrowie{/color} - ile obrażeń możesz przyjąć.\n\n{color=#C6E2FF}Duchowość{/color} - zużywane podczas używania kart w walce. Regeneruje się na początku nowej tury.{#mtl}{#tl}"

    # game/screens/menus/character.rpy:36
    old "{color=#d26a6a}Health:{/color}\n{color=#C6E2FF}Spirituality:{/color}"
    new "{color=#d26a6a}Zdrowie:{/color}\n{color=#C6E2FF}Duchowość:{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:37
    old "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}"
    new "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}{#mtl}{#tl}"

# TODO: Translation updated at 2022-01-31 15:20

translate polish strings:

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Zdrowie{/color}{/u}{/b}\n{small}Ile obrażeń możesz przyjąć.{/small}\n\n{b}{u}{color=#C6E2FF}Duchowość{/color}{/u}{/b}\n{small}Zużywana podczas używania karty w walce. Regeneruje się na początku nowej tury.{/small}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Poczytalność{/color}{/u}{/b}\n{small}Jak bardzo jesteś zdolny do logicznego rozumowania. Osiągnięcie 0% prowadzi do zakończenia gry.{/small}\n\n{b}{u}{color=#800080}Korupcja{/color}{/u}{/b}\n{small}Jak bardzo jesteś zdegenerowany. Osiągnięcie 100% prowadzi do końca gry.{/small}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Siła{/color}{/u}{/b}\n{small}Zwiększa obrażenia zadawane w walce o 1 co 5 punktów.{/small}\n\n{b}{u}{color=#32CD32}Zwinność{/color}{/u}{/b}\n{small}Każdy punkt daje 1% obrażeń do uniknięcia i zwiększa szansę na uniknięcie walki o 2%.{/small}\n\n{b}{u}{color=#A71930}Witalność{/color}{/u}{/b}\n{small}Każdy punkt zwiększa twoje maksymalne zdrowie o 3.{/small}\n\n{small}Wzrost na siłowni.{/small}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Inteligencja{/color}{/b}{/u}\n{small}Używana w niektórych testach.{/small}\n\n{b}{u}{color=#C6E2FF}Mądrość{/color}{/b}{/u}\n{small}Maksymalnie co 10 punktów duchowość o 1 punkt.{/small}\n\n{b}{u}{color=#FF958F}Charyzma{/color}{/b}{/u}\n{small}Używana w wielu testach. Używane, aby inni zgodzili się z tobą podczas rozmowy.{/small}\n\n{small}Zwiększony w pokoju gracza.{/small}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}Szczęście{/color}{/b}{/u}\n{small}Zwiększa szansę na dobre karty, zmniejsza szansę na spotkanie silnych przeciwników. Zwiększona za pomocą kodów z Discorda lub handlu z określonymi istotami.{/small}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:45
    old "State"
    new "Stan{#mtl}{#tl}"

    # game/screens/menus/character.rpy:53
    old "{color=#d26a6a}Health:{/color}"
    new "{color=#d26a6a}Zdrowie:{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:54
    old "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"
    new "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}{#mtl}{#tl}"

    # game/screens/menus/character.rpy:55
    old "Mental State"
    new "Stan Psychiczny{#mtl}{#tl}"

    # game/screens/menus/character.rpy:65
    old "Physical Stats"
    new "Atrybuty Fizyczne{#mtl}{#tl}"

    # game/screens/menus/character.rpy:75
    old "Mental Stats"
    new "Statystyki psychiczne{#mtl}{#tl}"

    # game/screens/menus/character.rpy:85
    old "Other"
    new "Inny{#mtl}{#tl}"

    # game/screens/menus/character.rpy:93
    old "Luck:"
    new "Szczęście:{#mtl}{#tl}"

    # game/screens/menus/character.rpy:94
    old "[player.luck]"
    new "[player.luck]{#mtl}{#tl}"

    # game/screens/menus/character.rpy:99
    old "Buffs"
    new "Buffy{#mtl}{#tl}"
