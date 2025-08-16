import rebound

sim = rebound.Simulation()
sim.add(m=1.0)           # Mặt trời
sim.add(m=1e-3, a=1.0)   # Hành tinh quay quanh

sim.integrate(10.0)      # Mô phỏng tới thời điểm t = 10

print("Vị trí hành tinh:", sim.particles[1].x, sim.particles[1].y)
