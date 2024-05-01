# 隐形自定义商人
execute as @e[type=wandering_trader,tag=block_trader] at @s run function merchants:wanderer_block
# 上层要丢的东西
execute as @e[type=item,nbt={Item:{id:"minecraft:carved_pumpkin"}}] at @s run function merchants:detect-items/carved_pumpkin
execute as @e[type=item,nbt={Item:{id:"minecraft:oak_log"}}] at @s run function merchants:detect-items/oak_log
execute as @e[type=item,nbt={Item:{id:"minecraft:iron_ingot"}}] at @s run function merchants:detect-items/iron_ingot
execute as @e[type=item,nbt={Item:{id:"minecraft:dirt"}}] at @s run function merchants:detect-items/dirt