# Galactic Stellar Halo Luminosity Function

**Authors:** Sarah A. Bird; Chris Flynn; Rudra Sekhri; Hai-Jun Tian; Juntai Shen; Xiang-Xiang Xue; Chao Liu; Gang Zhao

**arXiv ID:** 2603.11354

**DOI:** https://doi.org/10.48550/arXiv.2603.11354

**Submitted:** 2026-03-11

**Status:** submitted to ApJ

## Abstract (summary)

Bird et al. (2026) measure the luminosity function (LF) of the Milky Way's stellar halo using a magnitude-complete, distance-limited sample from Gaia DR3. They isolate halo stars via a high tangential-velocity cut (V_t > 250 km/s), yielding a high-purity sample of 24,471 stars (G < 17, within 1 kpc). The LF is measured continuously from faint halo subdwarfs (M_G ~ 13) up to bright giants (M_G ~ -3). They report a local halo number density of 1.7×10^-4 stars pc^-3, a disk-to-halo stellar number ratio of ~480:1, and a V-band luminosity density ≃1.5×10^-5 L_☉ pc^-3. Integrating a broken power-law halo model gives ~4.6×10^9 halo stars and a total halo luminosity ≃4.6×10^8 L_☉ (M_G ≃ -17.0).

---

## Key claims (3–5) and evidence from the full paper

1. Claim: Gaia DR3 enables the first continuous measurement of the local stellar halo LF from M_G ≈ 13 (dim subdwarfs) to M_G ≈ -3 (bright giants).
   - Evidence: The sample selection and LF construction are described in Sect. II and III; Figures 1–3 show the CMDs and the LF panels spanning this full magnitude range. The authors state explicitly that the Gaia sample "yields the first measurement of the LF continuously from the dimmest main sequence halo stars (subdwarfs) at an absolute M_G magnitude near 13 mag to bright giants at M_G ∼ -3." (Abstract, Sect. I–III).

2. Claim: The local stellar halo number density is 1.7×10^-4 stars pc^-3, and the local disk-to-halo number density ratio is ≃480:1.
   - Evidence: In Sect. III the authors integrate their corrected LF and report "By integrating our stellar halo LF, we obtain a robust measurement of the local stellar halo number density, 1.7×10^-4 stars pc^-3... disk-to-halo ratio by stellar density of 480:1." (Sect. III, surrounding Fig. 2/3).

3. Claim: The measured halo LF shows the same characteristic features seen in the disk LF (Wielen dip near M_G ∼ 7 and a strong peak near M_G ∼ 10).
   - Evidence: Sect. III and IV.3 compare the halo LF to the well-measured disk LF (Gaia Collaboration et al. 2021) and note the Wielen dip (M_G ∼ 5–9) and the LF maximum at M_G ∼ 10; these features are visible in Fig. 2 (LF panels) and Fig. 4 (halo vs disk comparison).

4. Claim: Halo star selection using a transverse-velocity cutoff (V_t > 250 km/s) yields a high-purity halo sample but excludes roughly half of halo stars; they correct for this with a kinematic model producing a correction factor of ≃2.0.
   - Evidence: Sect. II.2 describes the V_t selection (250 km/s cutoff) and Sect. II.3.2 explains the tangential-velocity completeness correction. The authors write that simulations/modeling (Appendix C) lead to a correction factor of 2.0 which is applied to the LF calculations.

5. Claim: Using a broken power-law halo density profile (α_inner = -2.5, α_outer = -4.0, break at 20 kpc) and normalizing to the local LF yields a total Milky Way halo star count ≃4–4.6×10^9 and halo luminosity ≃4.1–4.6×10^8 L_☉ (V/G bands), giving an absolute magnitude M ≃ -16.7 to -17.0.
   - Evidence: Sect. III (integration and extrapolation) reports the numeric totals for both the G and V bands and explains the assumed broken power-law profile and integration limits (0.1–100 kpc) used to estimate the global halo properties.

---

## Brief critique / notes

- Strengths:
  - Very large, homogeneous Gaia DR3 sample with parallaxes and proper motions makes the LF measurement robust across a wide magnitude range.
  - Careful completeness corrections (volume and tangential-velocity) are described and applied; authors explicitly quote correction factors and uncertainties.

- Caveats / open points:
  - The V_t > 250 km/s selection improves purity but relies on kinematic modeling to recover the missing fraction; results depend on the assumed kinematic decomposition (halo vs Gaia-Enceladus-Sausage etc.).
  - The faint-end behavior beyond M_G ≳ 11.5 remains uncertain due to increasing uncertainties and incompleteness (authors note this explicitly).

---

## Suggested wiki pages to create/update

1. Stellar Halo (concept)
2. Stellar Luminosity Function (concept)
3. Gaia DR3 (data note / dataset page)
4. Halo Kinematics (concept)

---

## Files created by subagent

- Paper analysis: data/papers/bird2026_galactic_stellar_halo_lf.md
- Paper page: src/pages/pages/bird_2026_galactic_stellar_halo_lf.astro
- Concept pages: src/pages/pages/stellar_halo.astro, src/pages/pages/luminosity_function.astro


