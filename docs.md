
# Lua Documentation Generator Documentation

Version: 0.1.0


---@module 核心
## Module: 核心

这个模块提供了游戏引擎的核心功能


### Tables


#### simpleTable

(Local table)

这是一个简单的表






### Functions



#### core.initialize



初始化游戏引擎


Parameters:

- **config**: [table](#table) - 引擎配置选项




Returns:

- [boolean](#boolean) - 初始化是否成功










#### core.update



运行游戏主循环


Parameters:

- **delta_time**: [number](#number) - 上一帧到当前帧的时间间隔












---@module core\math.lua
## Module: core\math.lua





### Functions



#### math.add



Calculates the sum of two numbers


Parameters:

- **a**: [number](#number) - The first number

- **b**: [number](#number) - The second number




Returns:

- [number](#number) - The sum of a and b




Usage:
```lua
local result = math.add(5, 3)


Examples:
luaCopy
local sum = math.add(10, 20)
print(sum)  -- Output: 30


See also:


[math.subtract](#mathsubtract)






---@module 工具
## Module: 工具

这个模块提供了一些通用的工具函数



### Functions



#### utils.clamp



将数值限制在指定范围内


Parameters:

- **value**: [number](#number) - 需要限制的值

- **min**: [number](#number) - 最小值

- **max**: [number](#number) - 最大值




Returns:

- [number](#number) - 限制后的值










#### utils.lerp



线性插值


Parameters:

- **a**: [number](#number) - 起始值

- **b**: [number](#number) - 结束值

- **t**: [number](#number) - 插值因子 (0-1)




Returns:

- [number](#number) - 插值结果










---@module 渲染器
## Module: 渲染器

这个模块负责游戏的图形渲染



### Functions



#### renderer.initialize



初始化渲染器


Parameters:

- **options**: [渲染选项](#渲染选项) - 渲染器的配置选项




Returns:

- [boolean](#boolean) - 初始化是否成功










#### renderer.draw_sprite



绘制精灵


Parameters:

- **sprite_id**: [string](#string) - 精灵的唯一标识符

- **x**: [number](#number) - 精灵的 X 坐标

- **y**: [number](#number) - 精灵的 Y 坐标

- **rotation**: [number](#number) - 精灵的旋转角度（弧度）












---@module 碰撞检测
## Module: 碰撞检测

这个模块提供了基本的碰撞检测功能



### Functions



#### collision.check_rect_collision



检测两个矩形是否相交


Parameters:

- **rect1**: [矩形](#矩形) - 第一个矩形

- **rect2**: [矩形](#矩形) - 第二个矩形




Returns:

- [boolean](#boolean) - 是否相交










#### collision.point_in_rect



检测点是否在矩形内


Parameters:

- **x**: [number](#number) - 点的 X 坐标

- **y**: [number](#number) - 点的 Y 坐标

- **rect**: [矩形](#矩形) - 要检测的矩形




Returns:

- [boolean](#boolean) - 点是否在矩形内











Type Index

table
Used in:


[init](#init): core.initialize (parameter)



boolean
Used in:


[init](#init): core.initialize (return)


[renderer](#renderer): renderer.initialize (return)


[collision](#collision): collision.check_rect_collision (return)


[collision](#collision): collision.point_in_rect (return)



number
Used in:


[init](#init): core.update (parameter)


[math](#math): math.add (parameter)


[math](#math): math.add (parameter)


[math](#math): math.add (return)


[utils](#utils): utils.clamp (parameter)


[utils](#utils): utils.clamp (parameter)


[utils](#utils): utils.clamp (parameter)


[utils](#utils): utils.clamp (return)


[utils](#utils): utils.lerp (parameter)


[utils](#utils): utils.lerp (parameter)


[utils](#utils): utils.lerp (parameter)


[utils](#utils): utils.lerp (return)


[renderer](#renderer): renderer.draw_sprite (parameter)


[renderer](#renderer): renderer.draw_sprite (parameter)


[renderer](#renderer): renderer.draw_sprite (parameter)


[collision](#collision): collision.point_in_rect (parameter)


[collision](#collision): collision.point_in_rect (parameter)



渲染选项
Used in:


[renderer](#renderer): renderer.initialize (parameter)



string
Used in:


[renderer](#renderer): renderer.draw_sprite (parameter)



矩形
Used in:


[collision](#collision): collision.check_rect_collision (parameter)


[collision](#collision): collision.check_rect_collision (parameter)


[collision](#collision): collision.point_in_rect (parameter)




Function Index


[init.core.initialize](#initcoreinitialize)


[init.core.update](#initcoreupdate)


[math.math.add](#mathmathadd)


[utils.utils.clamp](#utilsutilsclamp)


[utils.utils.lerp](#utilsutilslerp)


[renderer.renderer.initialize](#rendererrendererinitialize)


[renderer.renderer.draw_sprite](#rendererrendererdraw_sprite)


[collision.collision.check_rect_collision](#collisioncollisioncheck_rect_collision)


[collision.collision.point_in_rect](#collisioncollisionpoint_in_rect)


Table Index


[init.simpleTable](#initsimpletable)
