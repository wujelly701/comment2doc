---@module 工具
---这个模块提供了一些通用的工具函数

local utils = {}

---将数值限制在指定范围内
---@param value number 需要限制的值
---@param min number 最小值
---@param max number 最大值
---@return number 限制后的值
function utils.clamp(value, min, max)
    return math.max(min, math.min(max, value))
end

---线性插值
---@param a number 起始值
---@param b number 结束值
---@param t number 插值因子 (0-1)
---@return number 插值结果
function utils.lerp(a, b, t)
    return a + (b - a) * t
end

return utils