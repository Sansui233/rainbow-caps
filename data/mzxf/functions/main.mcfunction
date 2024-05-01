# 隐形自定义商人
execute as @e[type=wandering_trader,tag=block_trader] at @s run function mzxf:jiaoyi_block
# 上层要丢的东西
execute as @e[type=item,nbt={Item:{id:"minecraft:carved_pumpkin"}}] at @s run function mzxf:jiaoyi_item
execute as @e[type=item,nbt={Item:{id:"minecraft:oak_log"}}] at @s run function mzxf:jiaoyi_item_jiaju