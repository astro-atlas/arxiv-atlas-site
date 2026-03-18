# Very long-term relaxation of harmonic 1D self-gravitating systems

**Authors:** Kerwann Tep, Jean-Baptiste Fouvry, Christophe Pichon

**arXiv ID:** 2603.11238

**Date:** 2026-03-11

**Status:** Submitted to A&A

## Abstract Summary

Tep et al. investigate the long-term, self-consistent relaxation of one-dimensional (1D) self-gravitating systems, focusing on the extreme case of a harmonic potential (all orbits share the same orbital frequency). Using an exact collision-driven N-body integrator and large ensembles of realizations, they measure thermalization times using an ensemble-averaged Kolmogorov–Smirnov distance (D_KS) to the thermodynamical equilibrium.

## Key Findings (3–5 claims with evidence)

1. Harmonic (fully degenerate) systems relax extremely slowly: trel ∝ N^2 t_dyn.
   - Evidence: Section 3.3 and Figure 2 show trel vs N for Plummer, Compact and Harmonic potentials. Harmonic data follow a clear N^2 scaling (dashed line) while non-degenerate models follow ∝ N. The authors state this is the main result of the paper.
   - Measurement details: relaxation time is defined by the ensemble-averaged KS distance crossing a threshold D0=0.015 (eqs. 7–8, Sec. 3.2). Simulations used N in [21,141] and ensembles chosen so that N×N_r ≈ 1e5 (Sec. 3.3).

2. Partially degenerate (``Anharmonic'') systems show two regimes: for small N they follow the N^2 scaling, but transition to the N scaling for larger N.
   - Evidence: Figure 3 (Sec. 3.3) shows trel(N) for Anharmonic potentials as the degeneracy parameter ε is varied. The transition N increases as ε→0 (more degenerate), showing degeneracy delays relaxation.

3. Non-degenerate systems (Plummer, Compact) relax on trel ∝ N t_dyn, but compact radial support increases the prefactor significantly.
   - Evidence: Figure 2 shows Plummer and Compact following linear scaling, with Compact relaxing ~10× more slowly than Plummer. The authors attribute the large prefactor to quasi-kinetic blocking and the need for high-order resonances (Sec. 3.3).

4. The standard quasilinear kinetic theories (Landau / Balescu–Lenard and 1/N^2 extensions) break down for fully degenerate (flat-frequency) systems because phase-mixing assumptions fail; thermodynamic blocking and other non-quasilinear effects are likely responsible for the delayed relaxation.
   - Evidence: Discussion in Sec. 3.1–3.3 and the Conclusions (Sec. 4). The paper notes BL is ill-posed for harmonic systems (Resonance δD(kΩ−k'Ω') is ill-defined when Ω(E) is constant), and points to the thermodynamic blocking idea (Deme & Fouvry 2025) as a promising explanation (Sec. 4.2).

## Simulation / methods notes (important evidence)

- Integration: exact collision-driven 1D integrator (Noullez et al. 2003), double-float (80-bit) precision to limit round-off (Appendix A).
- Relaxation metric: ensemble-averaged Kolmogorov–Smirnov distance D_KS(t) (eqs. 6–8) with threshold D0=0.015.
- Parameter ranges: N between 21 and 141; ensemble sizes chosen to keep N×N_r ≈ 1e5. Longest run (Harmonic N=141) took ≈50 hours on one core.

## Implications

- Dynamically degenerate cores (e.g., harmonic-like density cores) will thermalize much more slowly than standard kinetic theory predicts; this impacts dynamical friction and core stalling in dwarf galaxy centers.
- The result motivates new theoretical work beyond quasilinear kinetic theory (renormalisation, time-averaging, three-body/collective effects, thermodynamic blocking).

## References (selected)

- Tep, K., Fouvry, J.-B., & Pichon, C. (2026). Very long-term relaxation of harmonic 1D self-gravitating systems. arXiv:2603.11238. https://arxiv.org/abs/2603.11238
- Roule, M., Fouvry, J.-B., et al. (2022). On quasi kinetic blocking (discussed in text).
- Deme, B. & Fouvry, J.-B. (2025). Thermodynamic blocking (cited as a perspective).

## Wiki pages to create/update

- 1D self-gravitating systems
- Harmonic cores / harmonic potentials
- Balescu–Lenard equation (kinetic theory)
- Thermodynamic blocking


