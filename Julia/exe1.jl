#=
This is a example code of Julia.
exe1 program checks behavior of math calculation and String.
=#

a = 10 + 7
println(a)

b = 10 - 7
println(b)

c = 10 * 7
println(c)

d = 10 / 7
println(d)

#=
str1 = 'string'
println(str1, typeof(str1))
=#

str2 = "string"
println(str2, typeof(str2))

str3 = """string"""
println(str3, typeof(str3))

str4 = str2 * str3
print(str4)

while true
    input = readline()
    input == "0" && break
end