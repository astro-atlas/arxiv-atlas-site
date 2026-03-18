# The TRGB-SBF Project. IV. A Color Calibration of the TRGB in the JWST F090W+F150W Filters

**Authors:** M. I. Chazov, D. I. Makarov, R. B. Tully, G. S. Anand, L. N. Makarova, Y. Cohen, J. P. Blakeslee, M. Cantiello, J. B. Jensen, G. Raimondo

**arXiv ID:** 2603.11160

**Date:** 2026-03-11 (v1) — ApJ accepted

## Abstract Summary

Chazov et al. establish a color calibration for the tip of the red giant branch (TRGB) in JWST's F090W+F150W filters. They analyze 17 nearby galaxies using maximum likelihood estimation (MLE) of TRGB positions across color slices of the RGB. The key finding: the TRGB is constant at M_F090W ≃ -4.40 mag (Vega) for (F090W-F150W)₀ < 1.65 mag, then becomes fainter at higher metallicities. Distances to 16 galaxies relative to NGC 4258 (maser distance anchor) are determined.

## Key findings (3–5 concise claims with evidence)

1. TRGB absolute magnitude in F090W is M_F090W^TRGB = -4.40 ± 0.03 mag (Vega) at low/intermediate metallicities ((F090W-F150W)₀ < 1.65 mag).
   - Evidence: Maximum likelihood fits to RGB luminosity functions in multiple galaxies (NGC 4258 + 16 others); values remain constant blueward of the color break with <0.03 mag uncertainty per galaxy.

2. TRGB magnitude declines at higher metallicities: a break in slope occurs at (F090W-F150W)₀ ≃ 1.65 mag, corresponding to [M/H] ≃ -0.57 (for 10 Gyr isochrones).
   - Evidence: Color slicing analysis of RGB in elliptical galaxies (Virgo/Fornax cluster members) reveals a consistent transition; redward of 1.65 mag, the TRGB becomes fainter with increasing color; theoretical PARSEC/Teramo isochrones support this metallicity assignment.

3. Revised distance moduli (using thin/thick slice methods) are on average 1.5% smaller (Δμ ≃ -0.03 mag) than previously published values from the same raw data.
   - Evidence: Systematic differences between new color-aware MLE fits and prior analyses (Anand et al. 2024a,b, 2025) that did not account for the TRGB color dependence; differences driven by updated JWST pipeline calibrations and DOLPHOT versions.

4. The calibration extends the TRGB distance method to high-metallicity (high-[M/H]) stellar populations, critical for the Hubble Constant ladder via the Population II method.
   - Evidence: 17-galaxy sample spanning wide metallicity ranges; new Python/NET tools enable robust segmentation of RGB color slices for accurate TRGB detection.

## Methods & Data Notes

- Galaxies: 17 total — NGC 4258 (maser-anchored zero point), 13 Virgo/Fornax cluster ellipticals, plus WLM, NGC 253, NGC 1549, NGC 5643.
- Observations: JWST/NIRCam F090W + F150W photometry from GO–1638, GO–1685, GO–3055; PSF photometry via DOLPHOT.
- TRGB detection: Maximum likelihood estimation (MLE) of RGB luminosity function (split power-law model) applied to color-sliced CMD regions.
- Calibration: NGC 4258 maser distance modulus μ = 29.397 ± 0.032 mag sets absolute scale.
- Metallicity inference: Theoretical isochrones (PARSEC, Teramo SPoT) identify [M/H] at color transition.

## Implications

- Improves precision of Population II distance ladder; smaller revisions to published Hubble constant values.
- Demonstrates that accurate TRGB distances require accounting for color-dependent metallicity effects at high [M/H].
- New RGB color-segmentation methodology enables future applications to higher-metallicity galaxy populations (nearby clusters, higher-z).

## Wiki pages to create / update

- pages/chazov_2026_trgb_jwst (paper page)
- pages/trgb_distance_indicator (concept; create/update)
- pages/distance_ladder (concept; create/update)
- pages/metallicity_effects (concept; create)

## References

Chazov, M. I., et al. (2026). "The TRGB-SBF Project. IV. A Color Calibration of the TRGB in the JWST F090W+F150W Filters." arXiv:2603.11160. ApJ accepted. DOI: https://doi.org/10.48550/arXiv.2603.11160

(Full bibliography: see paper PDF.)
