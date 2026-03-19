---
title: "Jeans Equation"
pageType: concept
status: done
---

<h1 class="page-title">Jeans Equation</h1>
<div class="infobox">
  <h3 class="infobox-title">Jeans Equation (Cluster Dynamics)</h3>
  <table>
    <tr><th>Type:</th><td>Dynamical equation</td></tr>
    <tr><th>Domain:</th><td>Stellar dynamics, cluster kinematics</td></tr>
    <tr><th>Key codes:</th><td><a href="/pages/mamposst" class="wikilink">MAMPOSSt / MG-MAMPOSSt</a></td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/orbital-anisotropy-in-galaxy-clusters" class="wikilink">Orbital Anisotropy</a><br />
        <a href="/pages/projected-phase-space" class="wikilink">Projected Phase Space</a><br />
        <a href="/pages/nfw-profile" class="wikilink">NFW Profile</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>Jeans equation</strong> relates the mass profile of a gravitating system to the velocity dispersion and density distribution of its tracer population, assuming dynamical equilibrium <a href="#ref1">[1]</a>. In the context of galaxy clusters, it is the theoretical backbone of kinematic mass estimation: given observed galaxy positions and line-of-sight velocities, the Jeans equation constrains both the total gravitational potential and the <a href="/pages/orbital-anisotropy-in-galaxy-clusters" class="wikilink">orbital anisotropy</a> <a href="#ref1">[1]</a><a href="#ref2">[2]</a>.
</p>
<h2 id="formulation">Spherical Jeans Equation</h2>
<p>
  For a spherically symmetric system, the Jeans equation reads: d(ν σ<sub>r</sub>²)/dr + 2β(r) ν σ<sub>r</sub>²/r = −ν dΦ/dr, where ν is the tracer number density, σ<sub>r</sub> is the radial velocity dispersion, β(r) = 1 − σ<sub>θ</sub>²/σ<sub>r</sub>² is the anisotropy parameter, and Φ is the gravitational potential <a href="#ref1">[1]</a>. The mass-anisotropy degeneracy — the fact that β and M(r) enter together — is the fundamental challenge <a href="#ref1">[1]</a><a href="#ref3">[3]</a>.
</p>
<h2 id="mamposst">Application via MAMPOSSt</h2>
<p>
  <a href="/pages/mamposst" class="wikilink">MAMPOSSt</a> solves the Jeans equation using <a href="/pages/projected-phase-space" class="wikilink">projected phase-space</a> data (projected radii and line-of-sight velocities) via maximum likelihood, jointly constraining mass and anisotropy profiles <a href="#ref1">[1]</a>. The method assumes a 3D Gaussian velocity distribution, which remains valid even when the LoS velocity distribution significantly departs from Gaussianity <a href="#ref1">[1]</a>. Alternative approaches using the kurtosis profile provide additional constraints beyond the dispersion alone <a href="#ref4">[4]</a>.
</p>
<h2 id="assumptions">Key Assumptions and Limitations</h2>
<ul>
  <li><strong>Spherical symmetry:</strong> Most implementations assume spherical symmetry; cluster ellipticity introduces systematic biases <a href="#ref1">[1]</a></li>
  <li><strong>Dynamical equilibrium:</strong> Galaxies must be in equilibrium; interlopers and substructure violate this <a href="#ref1">[1]</a><a href="#ref5">[5]</a></li>
  <li><strong>Tracer population:</strong> Using a mixed population (all members) has been validated against independent mass estimates <a href="#ref6">[6]</a><a href="#ref7">[7]</a><a href="#ref2">[2]</a></li>
</ul>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/mamposst" class="wikilink">MAMPOSSt / MG-MAMPOSSt</a></li>
  <li><a href="/pages/orbital-anisotropy-in-galaxy-clusters" class="wikilink">Orbital Anisotropy in Galaxy Clusters</a></li>
  <li><a href="/pages/galaxy-cluster-mass-estimation-methods" class="wikilink">Galaxy Cluster Mass Estimation Methods</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
<ol>
  <li id="ref1">Mamon, G. A., Biviano, A., Boué, G. (2013). "MAMPOSSt." <em>MNRAS</em>, 429, 3079.</li>
  <li id="ref2">Biviano, A., et al. (2023). "Cluster kinematic mass estimates." <em>ApJ</em>. DOI: 10.3847/1538-4357/acf832</li>
  <li id="ref3">Łokas, E. L., Mamon, G. A. (2003). "Dark matter in the Coma cluster." <em>MNRAS</em>, 343, 401.</li>
  <li id="ref4">Łokas, E. L. (2002). "Velocity moments and the mass-anisotropy degeneracy." <em>MNRAS</em>.</li>
  <li id="ref5">Malavasi, N., et al. (2020). "Coma large-scale structure." <em>A&amp;A</em>. DOI: 10.1051/0004-6361/201936629</li>
  <li id="ref6">Sartoris, B., et al. (2020). "Cluster member spatial distributions." <em>A&amp;A</em>. DOI: 10.1051/0004-6361/202037521</li>
  <li id="ref7">Biviano, A., et al. (2013). "Cluster mass and anisotropy profiles." <em>A&amp;A</em>.</li>
</ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  <a href="/pages/Tag_Galaxy_Clusters" class="wikilink">Galaxy Clusters</a>
  <a href="/pages/Tag_Methods" class="wikilink">Methods</a>
</div>
