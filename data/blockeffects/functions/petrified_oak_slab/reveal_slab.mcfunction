summon area_effect_cloud ~ ~ ~ {Duration:20,Tags:["petrified_oakslab","marker"]}
execute as @e[limit=1,distance=..0.1,type=area_effect_cloud,tag=marker] at @s align xyz run tp ~ ~ ~