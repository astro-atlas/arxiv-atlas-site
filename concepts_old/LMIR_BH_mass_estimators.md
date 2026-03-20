LMIR-based BH mass estimators

Definition
- BH mass estimators that use monochromatic mid-infrared (MIR) luminosities (e.g., rest-frame 3.4 μm or 4.6 μm) as a proxy for the broad-line region (BLR) size combined with broad emission line (BEL) velocity widths (FWHMs) to derive single-epoch virial black hole masses.

Motivation
- Optical continuum luminosities (e.g., L5100) can be heavily suppressed by dust extinction; MIR luminosities are far less affected and provide a more extinction-insensitive tracer of the AGN accretion power and BLR size.
- Important for dusty AGNs where optical-based BH mass estimates would be biased low.

Method
- Perform multi-component SED fitting (AGN + host galaxy templates) to measure extinction-corrected monochromatic luminosities at rest-frame MIR wavelengths (typically 3.4 μm and 4.6 μm).
- Measure BEL FWHMs from optical/IR spectra (C IV, Mg II, Hβ, Hα as available).
- Use an empirical calibration (e.g., Kim et al. 2023) relating LMIR and FWHM to BLR size and virial mass: MBH ∝ (FWHM)^2 × (LMIR)^α (α determined by calibration against reverberation-mapped AGNs).

Caveats
- MIR luminosity can have host-galaxy contamination (especially NIR); require SED decomposition and AGN fraction cuts (e.g., AGN fraction > 0.5 at the relevant wavelength).
- Calibration depends on the AGN template and extinction law assumptions.
- At high redshift, rest-frame MIR moves out of observed bands; require adequate photometry.

Key references
- Kim et al., 2023 (established the LMIR-based estimators and calibration)
- Kim et al., 2024–2026 (applications and tests in NEP-Wide field)

Use in ArXiv Atlas
- Tag papers using MIR-based BH mass estimates; store typical calibrations and limitations; link to datasets with SED decompositions.
