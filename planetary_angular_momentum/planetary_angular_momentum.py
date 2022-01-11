from vpython import color, cross, gcurve, graph, mag, norm, rate, sphere, vector


G = 6.67e-11
RES = 1.5e11
MS = 2e30
ME = 5e29
ve = 3.4e4

g1 = graph(xtitle="t [s]", ytitle="Lz [kg*m^2/s]", width=450, height=200, ymin=0)
fp = gcurve(color=color.blue)
fs = gcurve(color=color.red)
ft = gcurve(color=color.green)

sun = sphere(pos=vector(0, 0, 0), radius=RES/10, color=color.yellow)
planet = sphere(pos=vector(RES, 0, 0), radius=RES/20, color=color.cyan, make_trail=True)

sun.m = MS
planet.m = ME
planet.p = planet.m*vector(0, ve, 0)
sun.p = -planet.p
point_x = vector(2*RES, 0, 0)

t = 0
dt = 36000
Lnorm = mag(cross(planet.pos, planet.p))

while t < 3e8:
    rate(1000)
    r = planet.pos - sun.pos
    Fe = -G*sun.m*planet.m*norm(r)/mag(r)**2
    planet.p = planet.p + Fe*dt
    sun.p = sun.p - Fe*dt
    planet.pos = planet.pos + planet.p*dt/planet.m
    sun.pos = sun.pos + sun.p*dt/sun.m
    rpx = planet.pos - point_x
    rsx = sun.pos - point_x
    planet.L = cross(rpx, planet.p)
    sun.L = cross(rsx, sun.p)
    t = t +dt
    fp.plot(t, planet.L.z/Lnorm)
    fs.plot(t, sun.L.z/Lnorm)
    ft.plot(t, (sun.L.z+planet.L.z)/Lnorm)
