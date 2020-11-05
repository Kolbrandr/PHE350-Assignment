import Basic_Functions
import Common_Variables
import math
import numpy


def eccentricity_vector(velocity, momentum, radius):
    cross_vh = Basic_Functions.cross(velocity, momentum)
    cross_over_mu = []
    for component in cross_vh:
        cross_over_mu.append(component / Common_Variables.mu_Earth)

    radial_term = []
    for component in radius:
        radial_term.append(component * (-1) / Basic_Functions.vector_absolute(radius))

    ecc_vec = []
    lst = range(3)
    for i in lst:
        ecc_vec.append(cross_over_mu[i] + radial_term[i])
    e_vector = (ecc_vec[0], ecc_vec[1], ecc_vec[2])

    return e_vector


def momentum_calc(velocity, radius):
    momentum_vec = Basic_Functions.cross(radius, velocity)
    return momentum_vec


def perigee_coord(r_p, e_vector):
    #only works in 2D
    theta = numpy.arctan2(e_vector[1], e_vector[0])
    r_p_x = r_p*numpy.cos(theta)
    r_p_y = r_p*numpy.sin(theta)
    perigee = (r_p_x,r_p_y)
    return perigee


def parameter(momentum):
    p = Basic_Functions.vector_absolute(momentum)**2/Common_Variables.mu_Earth
    return p


def semi_major(parameter, eccentricity):
    semi_major_length = parameter / (1-eccentricity**2)
    return semi_major_length


def radii_calc(semi_major, eccentricity):
    r_p = semi_major*(1-eccentricity)
    r_a = semi_major*(1+eccentricity)
    return r_p, r_a


def orbital_period(semi_major):
    period_s = 2 * math.pi * semi_major ** 1.5 * Common_Variables.mu_Earth ** (-0.5)
    period_h = period_s/3600
    return period_h


def inclination(momentum):
    i = math.acos(momentum[2]/Basic_Functions.vector_absolute(momentum))
    i_deg = i*180/math.pi
    return i_deg


def raan(momentum):
    omega = numpy.arctan2(momentum[0], (-1)*momentum[1])
    omega_deg = omega*180/math.pi
    return omega_deg


def argument_periapsis(momentum, eccentricity):
    N = Basic_Functions.cross((0, 0, 1), momentum)
    constant = Basic_Functions.dot(N, eccentricity)/(Basic_Functions.vector_absolute(N)*Basic_Functions.vector_absolute(eccentricity))
    temp_wobble_u = math.acos(constant)
    if eccentricity[2] >= 0:
        wobble_u = temp_wobble_u
    else:
        wobble_u = 2*math.pi - temp_wobble_u
    wobble_u_deg = wobble_u*180/math.pi
    return wobble_u_deg

