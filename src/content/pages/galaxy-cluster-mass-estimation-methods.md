---
title: "Galaxy Cluster Mass Estimation Methods"
pageType: concept
status: done
---

<h1 class="page-title">Galaxy Cluster Mass Estimation Methods</h1>
<div class="infobox">
  <h3 class="infobox-title">Mass Estimation Methods</h3>
  <table>
    <tr><th>Type:</th><td>Methodology overview</td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/nfw-profile" class="wikilink">NFW Profile</a><br />
        <a href="/pages/jeans-equation" class="wikilink">Jeans Equation</a><br />
        <a href="/pages/sunyaev-zeldovich-effect" class="wikilink">Sunyaev-Zeldovich Effect</a><br />
        <a href="/pages/coma-cluster" class="wikilink">Coma Cluster</a>
      </td>
    </tr>
  </table>
</div>
<p>
  Galaxy cluster masses are measured through multiple independent techniques, each with distinct systematics. The <a href="/pages/coma-cluster" class="wikilink">Coma Cluster</a> serves as a benchmark for comparing these methods <a href="#ref1">[1]</a>.
</p>
<h2 id="kinematic">Kinematic Methods</h2>
<p>
  Galaxy velocities constrain the gravitational potential via the <a href="/pages/jeans-equation" class="wikilink">Jeans equation</a> <a href="#ref2">[2]</a><a href="#ref3">[3]</a>. Codes like <a href="/pages/mamposst" class="wikilink">MAMPOSSt</a> jointly fit mass and <a href="/pages/orbital-anisotropy-in-galaxy-clusters" class="wikilink">anisotropy</a> profiles <a href="#ref2">[2]</a>. Caustic methods and virial theorem estimates provide complementary constraints <a href="#ref4">[4]</a>. Systematics include interloper contamination and the mass-anisotropy degeneracy <a href="#ref2">[2]</a><a href="#ref3">[3]</a>.
</p>
<h2 id="lensing">Gravitational Lensing</h2>
<p>
  Weak lensing measures the projected mass distribution without assuming dynamical equilibrium <a href="#ref5">[5]</a><a href="#ref6">[6]</a>. Deep-learning CNN approaches mitigate noise amplification and mass-sheet degeneracy <a href="#ref6">[6]</a>. Weak lensing masses of Coma tend to be lower than kinematic estimates <a href="#ref5">[5]</a><a href="#ref6">[6]</a><a href="#ref1">[1]</a>.
</p>
<h2 id="xray-sz">X-ray and Sunyaev-Zeldovich</h2>
<p>
  X-ray observations of the ICM constrain the mass under hydrostatic equilibrium <a href="#ref7">[7]</a>. Combined with <a href="/pages/sunyaev-zeldovich-effect" class="wikilink">Sunyaev-Zeldovich</a> measurements, these provide temperature-independent mass estimates <a href="#ref7">[7]</a><a href="#ref8">[8]</a>.
</p>
<h2 id="ml">Machine Learning</h2>
<p>
  Bayesian deep learning methods use galaxy and ICM observables to predict cluster masses, yielding M<sub>200</sub> = 1.8 × 10<sup>15</sup> M<sub>☉</sub> for Coma <a href="#ref9">[9]</a>. These approaches are calibrated on simulations and may carry simulation-dependent biases <a href="#ref9">[9]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/coma-cluster" class="wikilink">Coma Cluster</a> — Multi-method mass comparison</li>
  <li><a href="/pages/nfw-profile" class="wikilink">NFW Profile</a></li>
  <li><a href="/pages/baryon-fraction-in-galaxy-clusters" class="wikilink">Baryon Fraction</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
<ol>
  <li id="ref1">Pedratti, S., et al. (2026). "Coma Cluster kinematics with DESI. I." <a href="https://arxiv.org/abs/2603.16706">arXiv:2603.16706</a></li>
  <li id="ref2">Mamon, G. A., Biviano, A., Boué, G. (2013). "MAMPOSSt." <em>MNRAS</em>, 429, 3079.</li>
  <li id="ref3">Łokas, E. L., Mamon, G. A. (2003). "Dark matter in Coma." <em>MNRAS</em>, 343, 401.</li>
  <li id="ref4">Benisty, D., et al. (2025). "Caustics and virial mass." <a href="https://arxiv.org/abs/2504.04135">arXiv:2504.04135</a></li>
  <li id="ref5">Gavazzi, R., et al. (2009). "Weak lensing mass of Coma." <em>A&amp;A</em>.</li>
  <li id="ref6">Cha, S., et al. (2025). "Deep-learning weak lensing." <em>ApJ</em>. DOI: 10.3847/1538-4357/adb1b7</li>
  <li id="ref7">Mirakhor, M. S., Walker, S. A. (2020). "XMM + Planck SZ mass." <em>MNRAS</em>. DOI: 10.1093/mnras/staa2203</li>
  <li id="ref8">Sunyaev, R. A., Zeldovich, Ya. B. (1972). "The Sunyaev-Zeldovich effect." <em>Comments Astrophys.</em>, 4, 173.</li>
  <li id="ref9">Ho, M., et al. (2022). "Bayesian deep learning cluster mass." <em>Nat. Astron.</em></li>
</ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  <a href="/pages/Tag_Methods" class="wikilink">Methods</a>
  <a href="/pages/Tag_Galaxy_Clusters" class="wikilink">Galaxy Clusters</a>
</div>
