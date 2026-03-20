SED fitting for AGN/host decomposition

Purpose
- Separate AGN and host-galaxy emission in multiwavelength photometry to measure AGN luminosities (including MIR monochromatic luminosities) and host properties.

Typical method
- Fit observed photometry with a linear combination of templates: reddened AGN + galaxy templates (elliptical, spiral, irregular).
- Apply extinction laws (e.g., Cardelli et al. 1989) and mask wavelengths strongly affected by uncertain templates (e.g., <3000 Å) when necessary.
- Require sufficient photometric coverage (e.g., >5 bands) and S/N thresholds; enforce AGN fraction cuts at the wavelength of interest to avoid host contamination.

Outputs
- Monochromatic AGN luminosities (rest-frame 3.4 μm, 4.6 μm), AGN fraction per band, extinction E(B−V), and uncertainties.

Caveats
- Template choice affects decomposition; MIR host contamination can remain significant if AGN fraction is low.
- Photometric depth at relevant observed wavelengths limits applicability at high redshift.
