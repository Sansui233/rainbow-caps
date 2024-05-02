# 设置检测变量，防止粒子太多每 tick 都在执行而卡死
scoreboard objectives add default_data dummy
scoreboard players set $Scanner.interval default_data 20
scoreboard players set $Scanner.life default_data 15

tellraw @a {"text":"§6§l粒子效果数据包加载成功","italic":false}

#debug
# scoreboard objectives setdisplay sidebar default_data