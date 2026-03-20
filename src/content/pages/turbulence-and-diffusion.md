---
title: "Turbulence & Diffusion Regimes"
pageType: concept
status: done
---

<h1 class="page-title">Turbulence &amp; Diffusion Regimes</h1>
<div class="infobox">
  <h3 class="infobox-title">Turbulence &amp; Particle Diffusion</h3>
  <table>
    <tr>
      <th>Type:</th>
      <td>Plasma physics / transport theory</td>
    </tr>
    <tr>
      <th>Key regimes:</th>
      <td>Bohm (&delta; = 1), Kraichnan (&delta; = 1/2), Kolmogorov (&delta; = 1/3)</td>
    </tr>
    <tr>
      <th>Key papers:</th>
      <td>
        Subedi et al. (2017), Dundovic et al. (2020),<br />
        <a href="/pages/2603-16647" class="wikilink">Peretti et al. (2026)</a>
      </td>
    </tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/diffusive-shock-acceleration" class="wikilink">Diffusive Shock Acceleration</a><br />
        <a href="/pages/recollimation-shocks" class="wikilink">Recollimation Shocks</a><br />
        <a href="/pages/shock-waves" class="wikilink">Shock Waves</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Turbulence and diffusion regimes</strong> govern how charged particles scatter and propagate in magnetized astrophysical plasmas. The spectrum of <a href="/pages/turbulence" class="wikilink">magnetic turbulence</a> sets the spatial diffusion coefficient &kappa;(p), which in turn controls the acceleration timescale and maximum energy achievable by <a href="/pages/diffusive-shock-acceleration" class="wikilink">diffusive shock acceleration</a> <a href="#ref1">[1]</a><a href="#ref2">[2]</a>. Different turbulence cascades — Kolmogorov, Kraichnan, or Bohm-like — predict diffusion coefficients with distinct momentum scalings, leading to orders-of-magnitude variation in predicted maximum particle energies <a href="#ref3">[3]</a>.
</p>
<h2 id="turbulence-cascades">Magnetic Turbulence Cascades</h2>
<h3>Kolmogorov Cascade</h3>
<p>
  The Kolmogorov (1941) cascade describes incompressible hydrodynamic turbulence with an energy spectrum E(k) &prop; k<sup>&minus;5/3</sup>, where energy is injected at large scales and cascades to smaller scales through eddy interactions <a href="#ref4">[4]</a>. When applied to magnetized plasmas, this yields a turbulent magnetic-field power spectrum W(k) &prop; k<sup>&minus;5/3</sup> <a href="#ref1">[1]</a>. The resulting spatial diffusion coefficient for particles with Larmor radius r<sub>L</sub> much smaller than the turbulence coherence length l<sub>c</sub> scales as &kappa; &prop; p<sup>1/3</sup> <a href="#ref1">[1]</a><a href="#ref2">[2]</a>. This is the slowest momentum scaling among the standard regimes, meaning high-energy particles diffuse relatively slowly and DSA is least efficient <a href="#ref3">[3]</a>.
</p>
<h3>Kraichnan Turbulence</h3>
<p>
  Kraichnan (1965) proposed an alternative cascade for magnetohydrodynamic turbulence based on Alfvén wave interactions, yielding a steeper spectrum E(k) &prop; k<sup>&minus;3/2</sup> <a href="#ref5">[5]</a>. This gives a diffusion coefficient &kappa; &prop; p<sup>1/2</sup>, intermediate between Kolmogorov and Bohm scalings <a href="#ref1">[1]</a><a href="#ref2">[2]</a>. Peretti et al. (2026) adopted Kraichnan diffusion as their benchmark regime for modeling particle acceleration at <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a>, as it represents a physically motivated middle ground <a href="#ref3">[3]</a>.
</p>
<h3>Goldreich-Sridhar Turbulence</h3>
<p>
  Goldreich &amp; Sridhar (1995) showed that MHD turbulence is fundamentally anisotropic, with eddies elongated along the local <a href="/pages/magnetic-field" class="wikilink">magnetic field</a> direction <a href="#ref6">[6]</a>. The perpendicular cascade follows a Kolmogorov-like k<sub>&perp;</sub><sup>&minus;5/3</sup> spectrum, while the parallel correlation scale varies as l<sub>&parallel;</sub> &prop; l<sub>&perp;</sub><sup>2/3</sup> <a href="#ref6">[6]</a>. This anisotropy complicates quasi-linear predictions for particle scattering rates, as resonant interactions depend on the parallel wavenumber spectrum <a href="#ref1">[1]</a>.
</p>
<h2 id="bohm-diffusion">Bohm Diffusion</h2>
<p>
  Bohm diffusion represents the theoretical minimum diffusion coefficient: &kappa;<sub>B</sub> = r<sub>L</sub>c/3, corresponding to scattering at every Larmor orbit <a href="#ref1">[1]</a><a href="#ref3">[3]</a>. This limit is approached when the turbulent magnetic field amplitude &delta;B is comparable to the mean field B<sub>0</sub> at the particle's resonant scale <a href="#ref1">[1]</a>. In the Bohm regime, &kappa; &prop; p (i.e., &delta; = 1), and <a href="/pages/diffusive-shock-acceleration" class="wikilink">DSA</a> achieves its highest efficiency and maximum energy <a href="#ref3">[3]</a>.
</p>
<p>
  Bohm diffusion is often assumed as an optimistic upper limit in acceleration models. Peretti et al. (2026) showed that for Seyfert-galaxy jets, the Bohm limit allows proton acceleration to EeV energies at <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a>, while Kolmogorov diffusion reduces this by up to three orders of magnitude <a href="#ref3">[3]</a>.
</p>
<h2 id="diffusion-scalings">Diffusion Coefficient Scalings</h2>
<p>
  The spatial diffusion coefficient is commonly parameterized as <a href="#ref1">[1]</a><a href="#ref2">[2]</a><a href="#ref3">[3]</a>:
</p>
<p style="text-align:center;">
  &kappa;(p) = &kappa;<sub>0</sub> (p / p<sub>0</sub>)<sup>&delta;</sup>
</p>
<p>
  where &delta; is set by the turbulence spectrum:
</p>
<ul>
  <li><strong>&delta; = 1 (Bohm):</strong> Maximum scattering rate; &kappa; = r<sub>L</sub>c/3 <a href="#ref3">[3]</a></li>
  <li><strong>&delta; = 1/2 (Kraichnan):</strong> &kappa; &prop; p<sup>1/2</sup>; intermediate regime <a href="#ref1">[1]</a></li>
  <li><strong>&delta; = 1/3 (Kolmogorov):</strong> &kappa; &prop; p<sup>1/3</sup>; weakest momentum dependence <a href="#ref1">[1]</a></li>
</ul>
<p>
  The normalization &kappa;<sub>0</sub> depends on the turbulence amplitude &epsilon;<sub>B</sub> = &delta;B<sup>2</sup>/B<sup>2</sup> and the coherence length l<sub>c</sub> of the turbulence <a href="#ref3">[3]</a>. In the quasi-linear regime (r<sub>L</sub> &lt;&lt; l<sub>c</sub>), resonant pitch-angle scattering on waves with wavelength ~ r<sub>L</sub> dominates the diffusion <a href="#ref1">[1]</a>. At high energies (r<sub>L</sub> &gt; l<sub>c</sub>), particles enter the small-angle scattering regime where &kappa; &prop; p<sup>2</sup> regardless of the turbulence spectrum <a href="#ref2">[2]</a>.
</p>
<h2 id="maximum-energy">Effect on Maximum Particle Energy</h2>
<p>
  The maximum energy E<sub>max</sub> achievable by DSA is set by the competition between acceleration time t<sub>acc</sub> &prop; &kappa;/u<sub>s</sub><sup>2</sup> and loss or escape timescales <a href="#ref3">[3]</a><a href="#ref7">[7]</a>. Since &kappa; increases with &delta;, steeper momentum scalings (larger &delta;) produce faster acceleration and higher E<sub>max</sub> for a given source <a href="#ref3">[3]</a>.
</p>
<p>
  For <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a>, the confinement limit typically determines E<sub>max</sub>: the upstream diffusion length &kappa;/u<sub>1</sub> must not exceed the shock height z<sub>sh</sub> <a href="#ref3">[3]</a>. Peretti et al. (2026) demonstrated the sensitivity quantitatively: for their Seyfert prototype, E<sub>max</sub> varies from ~10<sup>18</sup> eV (Bohm) to ~10<sup>17</sup> eV (Kraichnan) to ~10<sup>15</sup> eV (Kolmogorov) <a href="#ref3">[3]</a>. For microquasars, the spread is similarly dramatic <a href="#ref3">[3]</a>.
</p>
<h2 id="downstream-decay">Downstream Turbulence Decay</h2>
<p>
  Turbulence injected or amplified at the shock can decay downstream as energy cascades to dissipation scales <a href="#ref3">[3]</a>. Peretti et al. (2026) parameterized this as a power-law decay of the turbulent energy density with distance from the shock <a href="#ref3">[3]</a>. When the downstream diffusion coefficient grows rapidly with distance, particles can escape the acceleration region before achieving the confinement-limited E<sub>max</sub>, making downstream decay the dominant limitation on maximum energy <a href="#ref3">[3]</a>. This effect is particularly important for protostellar jets, where the downstream region is compact <a href="#ref3">[3]</a>.
</p>
<h2 id="modern-developments">Modern Developments</h2>
<p>
  Lazarian &amp; Yan (2021) explored mirror diffusion regimes relevant when turbulence levels are low and magnetic mirroring dominates over pitch-angle scattering <a href="#ref8">[8]</a>. Barreto-Mota et al. (2025) investigated diffusion in turbulence generated by streaming instabilities, finding that self-generated turbulence can maintain near-Bohm diffusion close to shocks even if the ambient turbulence supports a Kolmogorov or Kraichnan spectrum <a href="#ref9">[9]</a>. These developments suggest that the effective diffusion regime may vary spatially around astrophysical shocks <a href="#ref8">[8]</a><a href="#ref9">[9]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/diffusive-shock-acceleration" class="wikilink">Diffusive Shock Acceleration</a> — How diffusion regime sets the acceleration rate and E<sub>max</sub></li>
  <li><a href="/pages/recollimation-shocks" class="wikilink">Recollimation Shocks</a> — Application showing orders-of-magnitude sensitivity to turbulence model</li>
  <li><a href="/pages/shock-waves" class="wikilink">Shock Waves</a> — The discontinuities where turbulence is amplified</li>
  <li><a href="/pages/jet-cocoon-dynamics" class="wikilink">Jet-Cocoon Dynamics</a> — Environments hosting turbulence-mediated acceleration</li>
  <li><a href="/pages/2603-16647" class="wikilink">Peretti et al. (2026)</a> — Systematic comparison of Bohm/Kraichnan/Kolmogorov at recollimation shocks</li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">
      Subedi, P. et al. (2017). "Charged particle diffusion in isotropic random magnetic fields."
      <em>ApJ</em>, 837, 140.
      <a href="https://doi.org/10.3847/1538-4357/aa603a">DOI</a>
    </li>
    <li id="ref2">
      Dundovic, A. et al. (2020). "Novel aspects of cosmic ray diffusion in synthetic magnetic turbulence."
      <em>Phys. Rev. D</em>, 102, 103016.
      <a href="https://doi.org/10.1103/PhysRevD.102.103016">DOI</a>
    </li>
    <li id="ref3">
      Peretti, E., Amato, E., Cerri, S. S., Morlino, G., Pullano, L. P., &amp; Recchia, S. (2026). "Particle acceleration at recollimation shocks in sub-relativistic jets."
      <a href="https://arxiv.org/abs/2603.16647">arXiv:2603.16647</a>
    </li>
    <li id="ref4">
      Kolmogorov, A. N. (1941). "The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers."
      <em>Doklady Akademii Nauk SSSR</em>, 30, 301.
    </li>
    <li id="ref5">
      Kraichnan, R. H. (1965). "Inertial-range spectrum of hydromagnetic turbulence."
      <em>Physics of Fluids</em>, 8, 1385.
      <a href="https://doi.org/10.1063/1.1761412">DOI</a>
    </li>
    <li id="ref6">
      Goldreich, P. &amp; Sridhar, S. (1995). "Toward a theory of interstellar turbulence. II. Strong Alfvénic turbulence."
      <em>ApJ</em>, 438, 763.
      <a href="https://doi.org/10.1086/175121">DOI</a>
    </li>
    <li id="ref7">
      Hillas, A. M. (1984). "The origin of ultra-high-energy cosmic rays."
      <em>ARA&amp;A</em>, 22, 425.
      <a href="https://doi.org/10.1146/annurev.aa.22.090184.002233">DOI</a>
    </li>
    <li id="ref8">
      Lazarian, A. &amp; Yan, H. (2021). "Mirror diffusion of cosmic rays in turbulent magnetic fields."
    </li>
    <li id="ref9">
      Barreto-Mota, L. et al. (2025). "Particle diffusion in self-generated turbulence near shocks."
    </li>
  </ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  Turbulence · Diffusion · Bohm · Kraichnan · Kolmogorov · Particle Transport · MHD · Cosmic Rays
</div>
