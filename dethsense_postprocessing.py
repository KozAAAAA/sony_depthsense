'''
This script calculates amplitude, phase shift and distance 
based on the raw A-B frames with 0, 90, 180, 270 degree 
phase shifts created using the Desmos simulation.

sim: https://www.desmos.com/calculator/stxdkrn707
'''
import numpy as np


def main():
    F = 1  # Hz
    C = 299792458  # m/s (speed of light)
    TAP_PHASE_SHIFT_MODE = True  # True - tap mode, False - emit mode

    frame0 = 1.39671602696
    frame90 = 0.763029443134
    frame180 = -1.39671602696
    frame270 = -0.763029443134

    I = frame0 - frame180
    if TAP_PHASE_SHIFT_MODE:
        Q = frame90 - frame270
    else:
        Q = frame270 - frame90

    amp = np.sqrt(I**2 + Q**2)
    phase = np.arctan2(Q, I)  # [-pi, pi]
    phase = np.mod(phase, 2 * np.pi)  # [0, 2pi]

    max_range = C / (2 * F)
    ratio = phase / (2 * np.pi)
    distance = max_range * ratio

    print("Amplitude: ", amp)
    print("Phase Shift [rad]: ", phase)
    print("Distance [m]: ", distance)

if __name__ == "__main__":
    main()
