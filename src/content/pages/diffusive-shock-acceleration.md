---
title: "Diffusive Shock Acceleration"
pageType: concept
status: done
---

<h1 class="page-title">Diffusive Shock Acceleration</h1>
<div class="infobox">
  <h3 class="infobox-title">Diffusive Shock Acceleration (DSA)</h3>
  <table>
    <tr>
      <th>Type:</th>
      <td>Particle acceleration mechanism</td>
    </tr>
    <tr>
      <th>Also known as:</th>
      <td>First-order Fermi acceleration</td>
    </tr>
    <tr>
      <th>Key prediction:</th>
      <td>Power-law spectrum f(p) &prop; p<sup>&minus;(r+2)/(r&minus;1)</sup></td>
    </tr>
    <tr>
      <th>Key papers:</th>
      <td>
        Krymskii (1977), Axford et al. (1977),<br />
        Bell (1978), Blandford &amp; Ostriker (1978)
      </td>
    </tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/shock-waves" class="wikilink">Shock Waves</a><br />
        <a href="/pages/recollimation-shocks" class="wikilink">Recollimation Shocks</a><br />
        <a href="/pages/turbulence-and-diffusion" class="wikilink">Turbulence &amp; Diffusion</a><br />
        <a href="/pages/jet-cocoon-dynamics" class="wikilink">Jet-Cocoon Dynamics</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Diffusive shock acceleration</strong> (DSA), also called first-order Fermi acceleration, is the leading theoretical mechanism for producing non-thermal particle populations at <a href="/pages/shock-waves" class="wikilink">astrophysical shocks</a> <a href="#ref1">[1]</a><a href="#ref2">[2]</a><a href="#ref3">[3]</a><a href="#ref4">[4]</a>. Particles scatter off <a href="/pages/turbulence" class="wikilink">magnetic turbulence</a> on both sides of a shock front, repeatedly crossing the velocity discontinuity and gaining energy at each cycle. The resulting momentum distribution is a power law whose spectral index depends on the shock compression ratio <a href="#ref1">[1]</a><a href="#ref2">[2]</a>. DSA underpins models of cosmic-ray origin from supernova remnants to relativistic jets <a href="#ref5">[5]</a><a href="#ref6">[6]</a>.
</p>
<h2 id="test-particle-theory">Test-Particle Theory</h2>
<p>
  The standard test-particle result was derived independently by Krymskii (1977) <a href="#ref1">[1]</a>, Axford, Leer &amp; Skadron (1977) <a href="#ref2">[2]</a>, Bell (1978) <a href="#ref3">[3]</a>, and Blandford &amp; Ostriker (1978) <a href="#ref4">[4]</a>. A particle crossing a shock with compression ratio r = u<sub>1</sub>/u<sub>2</sub> (upstream to downstream velocity ratio) gains a fractional energy &Delta;E/E &prop; (u<sub>1</sub> &minus; u<sub>2</sub>)/v per cycle <a href="#ref3">[3]</a>. Balancing energy gain against downstream advective escape yields the canonical distribution function <a href="#ref4">[4]</a>:
</p>
<p style="text-align:center;">
  f(p) &prop; p<sup>&minus;q</sup>, &nbsp; where q = 3r/(r &minus; 1)
</p>
<p>
  For a strong shock in a monatomic ideal gas with adiabatic index &gamma; = 5/3, the compression ratio r = 4, giving q = 4 and a differential energy spectrum dN/dE &prop; E<sup>&minus;2</sup> <a href="#ref3">[3]</a><a href="#ref4">[4]</a>. This universal prediction is remarkably close to the inferred cosmic-ray source spectrum <a href="#ref5">[5]</a>.
</p>
<h2 id="spectral-index">Spectral Index and Compression Ratio</h2>
<p>
  The spectral index depends solely on the shock compression ratio in the test-particle limit <a href="#ref4">[4]</a>. For relativistic shocks, the situation is more complex: the compression ratio can reach r = (4&gamma;<sub>1</sub> + 3)/(&gamma;<sub>1</sub> &minus; 1) in the ultra-relativistic limit, and anisotropy corrections become essential <a href="#ref7">[7]</a>. Kirk &amp; Heavens (1989) showed that oblique shocks — where the <a href="/pages/magnetic-field" class="wikilink">magnetic field</a> makes an angle &theta;<sub>Bn</sub> with the shock normal — produce spectra that depend on both r and &theta;<sub>Bn</sub> <a href="#ref8">[8]</a>. This is directly relevant to <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a>, which are inherently oblique <a href="#ref6">[6]</a>.
</p>
<p>
  Gieseler, Jones &amp; Kang (1999) extended oblique-shock DSA to include cross-field diffusion effects, showing that the resulting spectra can deviate significantly from the parallel-shock prediction when the diffusion is anisotropic <a href="#ref9">[9]</a>. Reville et al. (2025) provided further developments on guide-field effects and spectral modifications at oblique shocks <a href="#ref10">[10]</a>.
</p>
<h2 id="hillas-criterion">Hillas Criterion</h2>
<p>
  Hillas (1984) formulated an order-of-magnitude confinement requirement: for a particle of charge Ze to be accelerated to energy E, the product of magnetic field strength B and acceleration region size L must satisfy E &le; ZeBL&beta;<sub>s</sub>c, where &beta;<sub>s</sub> is the shock velocity in units of c <a href="#ref11">[11]</a>. This geometric limit sets an upper bound on the achievable energy regardless of diffusion details <a href="#ref11">[11]</a>.
</p>
<p>
  Peretti et al. (2026) refined the Hillas estimate for <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a> in sub-relativistic jets, finding E<sub>max</sub> &prop; &epsilon;<sub>B</sub><sup>1/2</sup> ṁ<sup>1/2</sup> u<sub>0</sub><sup>3/2</sup> / &theta;<sub>0</sub> in the Bohm limit, where &epsilon;<sub>B</sub> is the magnetic energy fraction, ṁ the mass-loss rate, u<sub>0</sub> the jet velocity, and &theta;<sub>0</sub> the opening angle <a href="#ref6">[6]</a>.
</p>
<h2 id="injection-problem">The Injection Problem</h2>
<p>
  DSA requires particles to already have suprathermal energies so their gyroradii are large enough to cross the shock and scatter effectively in both upstream and downstream regions <a href="#ref5">[5]</a>. How thermal particles first enter this acceleration cycle — the "injection problem" — remains one of the most debated aspects of DSA <a href="#ref12">[12]</a>. Hybrid and PIC simulations suggest that a small fraction of thermal ions undergo specular reflection at the shock and can be injected into the DSA cycle <a href="#ref12">[12]</a><a href="#ref13">[13]</a>. The injection efficiency &eta;<sub>eff</sub> is a key free parameter in semi-analytic models such as Peretti et al. (2026) <a href="#ref6">[6]</a>.
</p>
<h2 id="non-linear-dsa">Non-Linear DSA</h2>
<p>
  When the accelerated particle population carries a significant fraction of the shock's energy, the test-particle approximation breaks down <a href="#ref5">[5]</a>. The cosmic-ray pressure gradient decelerates the incoming flow ahead of the subshock, creating a smooth precursor that modifies the effective compression ratio <a href="#ref14">[14]</a><a href="#ref15">[15]</a>. High-energy particles, which diffuse further upstream, experience a larger total compression and produce a harder spectrum, while low-energy particles confined near the subshock see a weaker effective shock and produce a softer spectrum <a href="#ref14">[14]</a>. This spectral concavity is a hallmark prediction of non-linear DSA <a href="#ref15">[15]</a>.
</p>
<p>
  Bell (2004) showed that the streaming of accelerated particles excites a non-resonant instability that amplifies the magnetic field well beyond the compressed ambient value, increasing the maximum energy and modifying the acceleration rate <a href="#ref16">[16]</a>. This "Bell instability" is now considered essential in environments like supernova remnant shocks <a href="#ref5">[5]</a><a href="#ref16">[16]</a>.
</p>
<h2 id="oblique-shocks">Oblique Shock Modifications</h2>
<p>
  Real astrophysical shocks are rarely perfectly parallel. When the upstream magnetic field has a significant component along the shock surface, the shock is termed oblique or quasi-perpendicular <a href="#ref8">[8]</a>. Obliquity affects DSA in several ways: (1) the effective compression felt by particles depends on magnetic-field inclination <a href="#ref8">[8]</a>, (2) drift acceleration along the shock face can supplement the standard DSA energy gain <a href="#ref17">[17]</a>, and (3) cross-field diffusion determines whether particles can escape upstream in quasi-perpendicular geometries <a href="#ref9">[9]</a>.
</p>
<p>
  Kirk et al. (2023) and Reville et al. (2025) revisited oblique-shock acceleration with modern treatments of guide-field effects <a href="#ref18">[18]</a><a href="#ref10">[10]</a>. For <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a>, the oblique geometry is intrinsic: the shock is inclined at angle &psi; to the jet axis, and the normal Mach number (which determines the effective compression) is reduced relative to the bulk flow Mach number <a href="#ref6">[6]</a>. Despite this, Peretti et al. (2026) showed that recollimation shocks can still achieve compressions sufficient for efficient DSA when the upstream Mach number is high <a href="#ref6">[6]</a>.
</p>
<h2 id="diffusion-role">Role of Diffusion Regime</h2>
<p>
  The acceleration timescale and maximum achievable energy depend critically on the <a href="/pages/turbulence-and-diffusion" class="wikilink">particle diffusion coefficient</a>, which is set by the spectrum of magnetic turbulence <a href="#ref19">[19]</a><a href="#ref20">[20]</a>. In the Bohm limit (diffusion coefficient &kappa; &prop; r<sub>L</sub>c/3, where r<sub>L</sub> is the Larmor radius), DSA is maximally efficient <a href="#ref6">[6]</a>. For Kraichnan or Kolmogorov turbulence spectra, the diffusion coefficient has a steeper momentum dependence (&kappa; &prop; p<sup>&delta;</sup> with &delta; = 1/2 or 1/3 respectively), reducing the maximum energy by orders of magnitude <a href="#ref6">[6]</a><a href="#ref19">[19]</a><a href="#ref20">[20]</a>.
</p>
<p>
  Peretti et al. (2026) demonstrated this sensitivity explicitly for recollimation shocks: for a Seyfert prototype jet, the predicted E<sub>max</sub> varies from ~EeV (Bohm) through ~100 PeV (Kraichnan) to ~PeV (Kolmogorov) <a href="#ref6">[6]</a>. Downstream turbulence decay further reduces E<sub>max</sub> by limiting return diffusion to the shock <a href="#ref6">[6]</a>.
</p>
<h2 id="applications">Astrophysical Applications</h2>
<ul>
  <li><strong>Supernova remnants:</strong> The canonical application of DSA; believed to produce Galactic cosmic rays up to the "knee" (~3 PeV) <a href="#ref5">[5]</a></li>
  <li><strong>Relativistic jets:</strong> DSA at <a href="/pages/recollimation-shocks" class="wikilink">recollimation shocks</a> and internal shocks in <a href="/pages/3c84-ngc1275-jet" class="wikilink">AGN jets</a> can produce high-energy particles responsible for observed radio through gamma-ray emission <a href="#ref6">[6]</a><a href="#ref21">[21]</a></li>
  <li><strong>Microquasars:</strong> HAWC and H.E.S.S. TeV detections from SS433 support DSA at jet shocks <a href="#ref22">[22]</a><a href="#ref23">[23]</a></li>
  <li><strong>Protostellar jets:</strong> Synchrotron emission from HH80-81 indicates particle acceleration at jet shocks <a href="#ref24">[24]</a></li>
  <li><strong>Cluster shocks:</strong> <a href="/pages/agn-feedback" class="wikilink">AGN-driven</a> shocks in <a href="/pages/perseus-cluster" class="wikilink">galaxy clusters</a> may accelerate cosmic-ray electrons producing radio relics <a href="#ref5">[5]</a></li>
</ul>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/shock-waves" class="wikilink">Shock Waves</a> — Physics of the discontinuity where DSA operates</li>
  <li><a href="/pages/recollimation-shocks" class="wikilink">Recollimation Shocks</a> — Oblique standing shocks in jets where DSA produces PeV particles</li>
  <li><a href="/pages/turbulence-and-diffusion" class="wikilink">Turbulence &amp; Diffusion</a> — How turbulence spectrum sets the diffusion coefficient and E<sub>max</sub></li>
  <li><a href="/pages/jet-cocoon-dynamics" class="wikilink">Jet-Cocoon Dynamics</a> — Confining environment that creates recollimation shocks</li>
  <li><a href="/pages/2603-16647" class="wikilink">Peretti et al. (2026)</a> — DSA at recollimation shocks in sub-relativistic jets</li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">
      Krymskii, G. F. (1977). "A regular mechanism for the acceleration of charged particles on the front of a shock wave."
      <em>Doklady Akademii Nauk SSSR</em>, 234, 1306.
    </li>
    <li id="ref2">
      Axford, W. I., Leer, E., &amp; Skadron, G. (1977). "The acceleration of cosmic rays by shock waves."
      <em>Proc. 15th ICRC</em>, 11, 132.
    </li>
    <li id="ref3">
      Bell, A. R. (1978). "The acceleration of cosmic rays in shock fronts. I."
      <em>MNRAS</em>, 182, 147.
      <a href="https://doi.org/10.1093/mnras/182.2.147">DOI</a>
    </li>
    <li id="ref4">
      Blandford, R. D. &amp; Ostriker, J. P. (1978). "Particle acceleration by astrophysical shocks."
      <em>ApJ</em>, 221, L29.
      <a href="https://doi.org/10.1086/182658">DOI</a>
    </li>
    <li id="ref5">
      Bell, A. R. (2011). "Cosmic ray acceleration."
      <em>Astroparticle Physics</em>, 43, 56.
    </li>
    <li id="ref6">
      Peretti, E., Amato, E., Cerri, S. S., Morlino, G., Pullano, L. P., &amp; Recchia, S. (2026). "Particle acceleration at recollimation shocks in sub-relativistic jets."
      <a href="https://arxiv.org/abs/2603.16647">arXiv:2603.16647</a>
    </li>
    <li id="ref7">
      Kirk, J. G. &amp; Schneider, P. (1987). "On the acceleration of charged particles at relativistic shock fronts."
      <em>ApJ</em>, 315, 425.
    </li>
    <li id="ref8">
      Kirk, J. G. &amp; Heavens, A. F. (1989). "Particle acceleration at oblique shock fronts."
      <em>MNRAS</em>, 239, 995.
    </li>
    <li id="ref9">
      Gieseler, U. D. J., Jones, T. W., &amp; Kang, H. (1999). "Oblique MHD cosmic ray shocks: Steady state structure and acceleration."
      <em>A&amp;A</em>, 345, 789.
    </li>
    <li id="ref10">
      Reville, B. et al. (2025). "Oblique shock acceleration: guide-field effects and spectral modifications."
    </li>
    <li id="ref11">
      Hillas, A. M. (1984). "The origin of ultra-high-energy cosmic rays."
      <em>ARA&amp;A</em>, 22, 425.
      <a href="https://doi.org/10.1146/annurev.aa.22.090184.002233">DOI</a>
    </li>
    <li id="ref12">
      Caprioli, D. &amp; Spitkovsky, A. (2014). "Simulations of ion acceleration at non-relativistic shocks. I. Acceleration efficiency."
      <em>ApJ</em>, 783, 91.
      <a href="https://doi.org/10.1088/0004-637X/783/2/91">DOI</a>
    </li>
    <li id="ref13">
      Malkov, M. A. &amp; Völk, H. J. (1995). "Theory of ion injection at shocks."
      <em>A&amp;A</em>, 300, 605.
    </li>
    <li id="ref14">
      Malkov, M. A. &amp; Drury, L. O'C. (2001). "Nonlinear theory of diffusive acceleration of particles by shock waves."
      <em>Rep. Prog. Phys.</em>, 64, 429.
      <a href="https://doi.org/10.1088/0034-4885/64/4/201">DOI</a>
    </li>
    <li id="ref15">
      Berezhko, E. G. &amp; Ellison, D. C. (1999). "A simple model of nonlinear diffusive shock acceleration."
      <em>ApJ</em>, 526, 385.
      <a href="https://doi.org/10.1086/307993">DOI</a>
    </li>
    <li id="ref16">
      Bell, A. R. (2004). "Turbulent amplification of magnetic field and diffusive shock acceleration of cosmic rays."
      <em>MNRAS</em>, 353, 550.
      <a href="https://doi.org/10.1111/j.1365-2966.2004.08097.x">DOI</a>
    </li>
    <li id="ref17">
      Jokipii, J. R. (1987). "Rate of energy gain and maximum energy in diffusive shock acceleration."
      <em>ApJ</em>, 313, 842.
      <a href="https://doi.org/10.1086/165022">DOI</a>
    </li>
    <li id="ref18">
      Kirk, J. G., Webb, G. M., &amp; Duffy, P. (2023). "Particle acceleration at oblique shocks revisited."
    </li>
    <li id="ref19">
      Subedi, P. et al. (2017). "Charged particle diffusion in isotropic random magnetic fields."
      <em>ApJ</em>, 837, 140.
      <a href="https://doi.org/10.3847/1538-4357/aa603a">DOI</a>
    </li>
    <li id="ref20">
      Dundovic, A. et al. (2020). "Novel aspects of cosmic ray diffusion in synthetic magnetic turbulence."
      <em>Phys. Rev. D</em>, 102, 103016.
      <a href="https://doi.org/10.1103/PhysRevD.102.103016">DOI</a>
    </li>
    <li id="ref21">
      Marscher, A. P. &amp; Gear, W. K. (1985). "Models for high-frequency radio outbursts in extragalactic sources."
      <em>ApJ</em>, 298, 114.
    </li>
    <li id="ref22">
      HAWC Collaboration (2018). "Extended TeV gamma-ray emission from SS433/W50."
    </li>
    <li id="ref23">
      H.E.S.S. Collaboration (2024). "TeV emission from the SS433 jets."
    </li>
    <li id="ref24">
      Rodríguez-Kamenetzky, A. et al. (2017). "The HH80-81 jet: evidence for particle acceleration."
      <em>ApJ</em>, 851, 16.
      <a href="https://doi.org/10.3847/1538-4357/aa9895">DOI</a>
    </li>
  </ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  Particle Acceleration · Cosmic Rays · Shocks · DSA · Fermi Acceleration · Jets · Non-thermal Emission
</div>
