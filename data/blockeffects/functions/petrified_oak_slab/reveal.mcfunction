scoreboard players set #Scanner.timer default_data 0

# 7x7
summon area_effect_cloud ^ ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}

summon area_effect_cloud ^1 ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}
summon area_effect_cloud ^-1 ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}

summon area_effect_cloud ^2 ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}
summon area_effect_cloud ^-2 ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}

summon area_effect_cloud ^3 ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}
summon area_effect_cloud ^-3 ^ ^ {Duration:20,Tags:["oakslab_scanner","onReady"]}

# 初始化
execute as @e[distance=..5, tag=onReady] at @s run function blockeffects:petrified_oak_slab/reveal_init