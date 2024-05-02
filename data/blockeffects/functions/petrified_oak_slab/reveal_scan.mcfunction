scoreboard players add #Scanner.iterated default_data 1

execute positioned ~ ~ ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab
execute positioned ~ ~1 ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab
execute positioned ~ ~2 ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab
execute positioned ~ ~3 ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab
execute positioned ~ ~-1 ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab
execute positioned ~ ~-2 ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab
execute positioned ~ ~-3 ~ align xyz if block ~ ~ ~ minecraft:petrified_oak_slab[type=top] unless entity @e[distance=..0.1,type=area_effect_cloud,tag=marker] run function blockeffects:petrified_oak_slab/reveal_slab

tp ^ ^ ^0.6

execute unless score #Scanner.iterated default_data >= $Scanner.life default_data at @s run function blockeffects:petrified_oak_slab/reveal_scan
execute if score #Scanner.iterated default_data >= $Scanner.life default_data at @s run function blockeffects:petrified_oak_slab/reveal_end_scan