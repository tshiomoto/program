using Flux.Tracker

W = param(rand(2, 5))
b = param(rand(2))
parameters = Params([W, b])

f(x) = W*x .+ b

function loss(x, y)
    hat_y = predict(x)
    sum((y .- hat_y).^2)
end