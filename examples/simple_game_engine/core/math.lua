---This is a module for mathematical operations

---Calculates the sum of two numbers
---@param a number The first number
---@param b number The second number
---@return number The sum of a and b
---@usage local result = math.add(5, 3)
---@example
---local sum = math.add(10, 20)
---print(sum)  -- Output: 30
---@see math.subtract
function math.add(a, b)
    return a + b
end