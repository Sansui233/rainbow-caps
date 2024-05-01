effect give @s invisibility 2 255 true
effect give @s regeneration 2 255 true
particle enchant ~ ~1.8 ~ 0.25 0.15 0.25 0 1 force

execute as @s[tag=carved_pumpkin] at @s unless block ~ ~ ~ carved_pumpkin run particle soul ~ ~1.6 ~ 0 0 0 0 1 force
execute as @s[tag=carved_pumpkin] at @s unless block ~ ~ ~ carved_pumpkin run tp @s ~ ~-1000 ~
execute as @s[tag=carved_pumpkin] at @s unless block ~ ~ ~ carved_pumpkin run kill @s