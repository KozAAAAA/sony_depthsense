# Sony DepthSense Technology Overview

This repository serves as a guide to **Sony DepthSense** technology, explaining how key values such as **amplitude**, **phase shift**, and **depth** are derived from the raw data captured by DepthSense pixels.

> Note: This explanation is written from a software engineer’s perspective.

## Time-of-Flight (ToF) Fundamentals
Time-of-Flight (ToF) technology operates by measuring the time it takes for emitted light to reflect off an object and return to the sensor. Typically, the emitted light is modulated as a sine wave. Upon returning to the sensor, the light exhibits a phase shift that is proportional to the distance between the sensor and the object.

## DepthSense Pixel Structure
Each DepthSense pixel consists of two taps, which I will refer to as tap $C_A$ and tap $C_B$. These taps act like capacitors and switches control their current flow. When switch A is enabled, switch B is disabled, and vice versa. Thus, the two taps are always 180 degrees out of phase with each other. The equivalent circuit is shown below.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c5870980-eb6f-46fe-ae38-3a5ac48bce49" width="700">
</p>

## Simulation for Better Understanding
To facilitate understanding, a [Desmos Simulation](https://www.desmos.com/calculator/stxdkrn707) was created. The simulation models the accumulation of voltages on taps $C_A$ and $C_B$ over time.

- $A$ and $B$ represent the voltages accumulated on each capacitor.
- By calculating the difference between these values, we can remove the ambient light, always present in the returning light signal.

## Python Script
The [Desmos Simulation](https://www.desmos.com/calculator/stxdkrn707) calculates the difference between the raw $A$ and $B$ values, which can then be used to compute amplitude, phase shift, and distance. To achieve accurate measurements, the sensor must collect four micro-frames, each with a different phase shift applied either to the emitted light or the switches. The required phase shifts are 0°, 90°, 180°, and 270°. In-phase (0° and 180°) and Quadrature (90° and 270°) components are then combined to calculate the amplitude, phase shift, and depth values. The example postprocessing script is called `depthsense_postprocessing.py` and it's available in this repository.

![frame](https://github.com/user-attachments/assets/8356ff53-91f0-4971-bf8c-a1ee2e3acdcc)
