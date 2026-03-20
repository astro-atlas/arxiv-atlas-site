---
title: "MAMPOSSt / MG-MAMPOSSt"
pageType: concept
status: done
---

<h1 class="page-title">MAMPOSSt / MG-MAMPOSSt</h1>
<div class="infobox">
  <h3 class="infobox-title">MAMPOSSt</h3>
  <table>
    <tr><th>Type:</th><td>Kinematic analysis code</td></tr>
    <tr><th>Full name:</th><td>Modelling Anisotropy and Mass Profiles of Observed Spherical Systems</td></tr>
    <tr><th>MAMPOSSt:</th><td>Mamon, Biviano &amp; Boué (2013) <a href="#ref1">[1]</a></td></tr>
    <tr><th>MG-MAMPOSSt:</th><td>Pizzuti, Saltas &amp; Amendola (2021) <a href="#ref2">[2]</a></td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/jeans-equation" class="wikilink">Jeans Equation</a><br />
        <a href="/pages/projected-phase-space" class="wikilink">Projected Phase Space</a><br />
        <a href="/pages/nfw-profile" class="wikilink">NFW Profile</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>MAMPOSSt</strong> is a maximum-likelihood code that jointly reconstructs the mass and <a href="/pages/orbital-anisotropy-in-galaxy-clusters" class="wikilink">anisotropy</a> profiles of spherical systems from <a href="/pages/projected-phase-space" class="wikilink">projected phase-space</a> data (projected radii and line-of-sight velocities) <a href="#ref1">[1]</a>. It solves the spherical <a href="/pages/jeans-equation" class="wikilink">Jeans equation</a> assuming parametric forms for both the mass density profile and anisotropy profile <a href="#ref1">[1]</a>.
</p>
<h2 id="mg-mamposst">MG-MAMPOSSt Extension</h2>
<p>
  <strong>MG-MAMPOSSt</strong> extends the original code to work in modified gravity frameworks (e.g. f(R), Vainshtein screening), allowing cluster kinematics to test the nature of gravity <a href="#ref2">[2]</a><a href="#ref3">[3]</a><a href="#ref4">[4]</a>.
</p>
<h2 id="methodology">Key Features</h2>
<ul>
  <li>Assumes 3D Gaussian velocity distribution (valid even when LoS distribution is non-Gaussian) <a href="#ref1">[1]</a></li>
  <li>Supports multiple mass models: <a href="/pages/nfw-profile" class="wikilink">NFW</a>, gNFW, Burkert, Hernquist <a href="#ref1">[1]</a></li>
  <li>Supports multiple anisotropy models: Osipkov-Merritt, Tiret, constant-β <a href="#ref1">[1]</a></li>
  <li>MCMC sampling with Gelman-Rubin convergence diagnostic <a href="#ref5">[5]</a></li>
  <li>Interloper removal via Clean algorithm <a href="#ref1">[1]</a></li>
</ul>
<h2 id="applications">Applications</h2>
<p>
  Applied to the <a href="/pages/coma-cluster" class="wikilink">Coma Cluster</a> using DESI DR1 data <a href="#ref6">[6]</a>, CLASH-VLT clusters <a href="#ref7">[7]</a>, and PSZ2 G067.17+67.46 <a href="#ref8">[8]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/jeans-equation" class="wikilink">Jeans Equation</a></li>
  <li><a href="/pages/projected-phase-space" class="wikilink">Projected Phase Space</a></li>
  <li><a href="/pages/galaxy-cluster-mass-estimation-methods" class="wikilink">Mass Estimation Methods</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
<ol>
  <li id="ref1">Mamon, G. A., Biviano, A., Boué, G. (2013). "MAMPOSSt." <em>MNRAS</em>, 429, 3079. DOI: 10.1093/mnras/sts565</li>
  <li id="ref2">Pizzuti, L., Saltas, I. D., Amendola, L. (2021). "MG-MAMPOSSt." <em>MNRAS</em>.</li>
  <li id="ref3">Pizzuti, L., et al. (2022). "Testing gravity with cluster kinematics." <em>MNRAS</em>.</li>
  <li id="ref4">Zamani, F., et al. (2024). "Modified gravity tests with clusters." <em>MNRAS</em>.</li>
  <li id="ref5">Gelman, A., Rubin, D. B. (1992). "Inference from iterative simulation." <em>Statistical Science</em>, 7, 457.</li>
  <li id="ref6">Pedratti, S., et al. (2026). "Coma Cluster kinematics with DESI. I." <a href="https://arxiv.org/abs/2603.16706">arXiv:2603.16706</a></li>
  <li id="ref7">Biviano, A., et al. (2025). "CLASH-VLT cluster anisotropy." <a href="https://arxiv.org/abs/2508.05195">arXiv:2508.05195</a></li>
  <li id="ref8">Pizzuti, L., et al. (2025). "Cluster orbital anisotropy." <em>A&amp;A</em>. DOI: 10.1051/0004-6361/202555417</li>
</ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  <a href="/pages/Tag_Methods" class="wikilink">Methods</a>
  <a href="/pages/Tag_Galaxy_Clusters" class="wikilink">Galaxy Clusters</a>
</div>
