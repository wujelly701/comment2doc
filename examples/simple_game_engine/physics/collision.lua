---@module 碰撞检测
---这个模块提供了基本的碰撞检测功能

local collision = {}

---@class 矩形
---@field x number 左上角的 X 坐标
---@field y number 左上角的 Y 坐标
---@field width number 矩形的宽度
---@field height number 矩形的高度

---检测两个矩形是否相交
---@param rect1 矩形 第一个矩形
---@param rect2 矩形 第二个矩形
---@return boolean 是否相交
function collision.check_rect_collision(rect1, rect2)
    return rect1.x < rect2.x + rect2.width and
           rect1.x + rect1.width > rect2.x and
           rect1.y < rect2.y + rect2.height and
           rect1.y + rect1.height > rect2.y
end

---检测点是否在矩形内
---@param x number 点的 X 坐标
---@param y number 点的 Y 坐标
---@param rect 矩形 要检测的矩形
---@return boolean 点是否在矩形内
function collision.point_in_rect(x, y, rect)
    return x >= rect.x and x <= rect.x + rect.width and
           y >= rect.y and y <= rect.y + rect.height
end

return collision