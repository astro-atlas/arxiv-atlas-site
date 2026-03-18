# An Updated SynthPop Model for Microlensing Simulations I: Model Description, Evaluation, and Microlensing Event Rates Near the Galactic Center

**Authors:** Macy J. Huston, Alison L. Crisp, et al.

**arXiv ID:** 2603.12219

**Date:** 2026-03-13

**Survey:** Roman GBTDS preparation

## Abstract Summary

This paper presents an updated Galactic model implementation within the SynthPop framework, optimized for simulating the Nancy Grace Roman Space Telescope's Galactic Bulge Time Domain Survey (GBTDS). The model (SP-H25) combines components from existing models and is evaluated against stellar catalogs and kinematics.

### Key Components:

1. **Stellar Densities & Kinematics:**
   - Bulge: Cao et al. (2013) E3 triaxial model
   - Kinematics: Koshimoto et al. (2021) Gaussian distribution
   - Disk: Koshimoto et al. (2021) 7-age thin disk + thick disk
   - Nuclear Stellar Disk: Sormani et al. (2022) model
   - Halo: Besançon model (Robin et al. 2003)

2. **Stellar Properties:**
   - IMF: Kroupa (2001), 0.08-100 M⊙
   - Isochrones: MIST v1.2
   - Ages: Bulge/NSD (10 Gyr), Halo (14 Gyr), Thick disk (12 Gyr)
   - Metallicity: Component-specific distributions

3. **Extinction:**
   - 2D map: Surot et al. (2020) at 8.15 kpc
   - 3D scaling: Galaxia dust disk scheme
   - Custom SODC extinction law, Rv=2.5

### Model Performance:

**Good Agreement (|b| > 0.5°):**
- WFC3 Bulge Treasury fields: within ~20% for most bins
- OGLE star counts: ~25% agreement for |b| > 1°
- RGBTDS fields: underpredicts by 2% (I<18) and 7% (I<21)
- Kinematics: Good agreement with WFC3 and Gaia proper motions

**Poor Agreement (|b| < 0.5°):**
- GNS fields: overpredicts by ~50%
- Arches field: overpredicts by ~100%
- Quintuplet field: overpredicts by 0-50%

### Implications:

1. Model performs well for Roman GBTDS contiguous lower bulge fields
2. Significant issues near Galactic plane affect Galactic center field predictions
3. Extinction model limitations for nearby disk stars
4. Need for completeness-corrected observational data

### Future Work:

- Roman's GBTDS and Galactic Plane Survey will help resolve model inconsistencies
- Paper II will examine detailed GBTDS simulations with this model

## Wiki Pages to Create/Update:

1. Gravitational Microlensing (update with Roman GBTDS context)
2. Galactic Models (new page on population synthesis models)
3. Nancy Grace Roman Space Telescope
4. Nuclear Stellar Disk
5. SynthPop (modeling framework)