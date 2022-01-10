from vpython import box, color, rate, sphere, vector


ball = sphere(pos=vector(0, .1, 0), radius=0.05, color=color.yellow, make_trail=True)
ground = box(pos=vector(0, 0, 0), size=vector(0.5, 0.02, 0.25))

g = vector(0, -9.8, 0)
ball.m = 0.05
v0 = 3.5
ball.v = vector(0, v0, 0)

t = 0
dt = 0.01

while t < 0.75:
    rate(50)
    F = ball.m * g
    a = F / ball.m
    ball.v = ball.v + a * dt
    ball.pos = ball.pos + ball.v * dt
    t = t + dt
