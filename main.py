import Advanced_Functions
import Basic_Functions

radius = (6472.7, -7470.8, -2469.8)    # km
velocity = (3.9914, 2.7916, -3.2948)    # km/s

h = Advanced_Functions.momentum_calc(velocity, radius)
p = Advanced_Functions.parameter(h)
e_vec = Advanced_Functions.eccentricity_vector(velocity, h, radius)
e_scalar = Basic_Functions.vector_absolute(e_vec)
e_unit = Basic_Functions.unit_vec(e_vec, e_scalar)
a = Advanced_Functions.semi_major(p, e_scalar)
i = Advanced_Functions.inclination(h)
Omega = Advanced_Functions.raan(h)
wobble_u = Advanced_Functions.argument_periapsis(h, e_vec)
# T = Advanced_Functions.orbital_period(a)
# rp, ra = Advanced_Functions.radii_calc(a, e_scalar)
# perigee_coords = Advanced_Functions.perigee_coord(rp, e_unit)

print(f"The semi-major axis is {a} km")
print(f"The eccentricity is {e_scalar}")
# print(f"The momentum vector is {h}")
print(f"The inclination is {i}")
print(f"The RAAN is {Omega}")
print(f"The argument of periapsis is {wobble_u}")
# print(f"rp equals {rp} km")
# print(f"ra equals {ra} km")
# print(f"The orbital period is {T} hours")
# print(f"The eccentricity vector is {e_vec}")
# print(f"The perigee is located at {perigee_coords} km")
