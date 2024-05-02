# attach particles to nearest dummy blocks summoned later

execute at @a at @e[distance=..30,limit=10,sort=nearest,type=area_effect_cloud,tag=petrified_oakslab] align xyz positioned ~0.5 ~0.5 ~0.5 run function blockeffects:petrified_oak_slab/particles


# time counter
execute as @a[limit=1] if data entity @s {Inventory:[{Slot:-106b,id:"minecraft:petrified_oak_slab"}]} run scoreboard players add #Scanner.timer default_data 1

# detect left hand and reveal petrified_oakslab
execute if score #Scanner.timer default_data >= $Scanner.interval default_data as @a if data entity @s {Inventory:[{Slot:-106b,id:"minecraft:petrified_oak_slab"}]} at @s run function blockeffects:petrified_oak_slab/reveal

# /summon area_effect_cloud ^ ^ ^ {Duration:999999,Tags:["oakslab_scanner","onReady"]}
# /data get entity @e[type=area_effect_cloud,limit=1,distance=..30]