---@module 核心
---这个模块提供了游戏引擎的核心功能

local core = {}

--- 这是一个简单的表
local simpleTable = {
    key1 = "value1",
    key2 = 123
}

---初始化游戏引擎
---@param config table 引擎配置选项
---@return boolean 初始化是否成功
function core.initialize(config)
    -- 实现初始化逻辑
    print("游戏引擎初始化中...")
    return true
end

---运行游戏主循环
---@param delta_time number 上一帧到当前帧的时间间隔
function core.update(delta_time)
    -- 实现游戏主循环逻辑
    print("游戏更新中，时间间隔: " .. delta_time)
end

return core