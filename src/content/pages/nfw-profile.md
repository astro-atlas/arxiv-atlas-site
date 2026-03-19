---
title: "NFW Profile"
pageType: concept
status: done
---

<h1 class="page-title">NFW Profile</h1>
<div class="infobox">
  <h3 class="infobox-title">Navarro-Frenk-White Profile</h3>
  <table>
    <tr><th>Type:</th><td>Dark matter density profile</td></tr>
    <tr><th>First described:</th><td>Navarro, Frenk &amp; White (1996, 1997) <a href="#ref1">[1]</a></td></tr>
    <tr><th>Key parameter:</th><td>Concentration c = r<sub>200</sub>/r<sub>s</sub></td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/galaxy-cluster-mass-estimation-methods" class="wikilink">Cluster Mass Estimation</a><br />
        <a href="/pages/jeans-equation" class="wikilink">Jeans Equation</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>NFW profile</strong> describes the radial density distribution of dark matter halos as ρ(r) ∝ r<sup>−1</sup>(1 + r/r<sub>s</sub>)<sup>−2</sup>, where r<sub>s</sub> is the scale radius <a href="#ref1">[1]</a>. Originally derived from N-body cosmological simulations, it has become the standard reference model for dark matter halos from galaxy to cluster scales <a href="#ref1">[1]</a>.
</p>
<h2 id="functional-form">Functional Form</h2>
<p>
  The profile has a central cusp (ρ ∝ r<sup>−1</sup>) transitioning to a steeper outer slope (ρ ∝ r<sup>−3</sup>) at r ≫ r<sub>s</sub> <a href="#ref1">[1]</a>. The single shape parameter is the concentration c = r<sub>200</sub>/r<sub>s</sub>. The projected (2D) NFW profile is analytically tractable <a href="#ref2">[2]</a>, making it suitable for fitting galaxy spatial distributions in clusters <a href="#ref3">[3]</a><a href="#ref4">[4]</a><a href="#ref5">[5]</a>.
</p>
<h2 id="extensions">Extensions and Alternatives</h2>
<ul>
  <li><strong>Generalised NFW (gNFW):</strong> Adds a free inner slope parameter γ, allowing departures from the canonical r<sup>−1</sup> cusp <a href="#ref6">[6]</a></li>
  <li><strong>Burkert profile:</strong> Features a flat core (ρ ∝ const at small r) rather than a cusp, with sharper slope transition <a href="#ref7">[7]</a></li>
  <li><strong>Hernquist profile:</strong> Steeper decline at large radii (ρ ∝ r<sup>−4</sup>); sometimes preferred for galaxy number density fits by BIC/AIC <a href="#ref8">[8]</a></li>
</ul>
<p>
  In the <a href="/pages/coma-cluster" class="wikilink">Coma Cluster</a>, Pedratti et al. (2026) find the NFW model (with gOM anisotropy) is preferred for the total mass profile, yielding r<sub>s</sub> = 0.48<sup>+0.27</sup><sub>−0.13</sub> Mpc, consistent with weak lensing concentration estimates <a href="#ref9">[9]</a><a href="#ref10">[10]</a>.
</p>
<h2 id="applications">Applications in Cluster Studies</h2>
<p>
  The NFW profile provides adequate descriptions of cluster total mass from lensing <a href="#ref11">[11]</a> and is the default mass model in kinematic codes like <a href="/pages/mamposst" class="wikilink">MAMPOSSt</a> <a href="#ref12">[12]</a>. Importantly, the galaxy number density profile scale radius is generally not the same as the mass profile scale radius <a href="#ref13">[13]</a><a href="#ref14">[14]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/galaxy-cluster-mass-estimation-methods" class="wikilink">Galaxy Cluster Mass Estimation Methods</a></li>
  <li><a href="/pages/jeans-equation" class="wikilink">Jeans Equation</a></li>
  <li><a href="/pages/coma-cluster" class="wikilink">Coma Cluster</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
<ol>
  <li id="ref1">Navarro, J. F., Frenk, C. S., White, S. D. M. (1997). "A Universal Density Profile from Hierarchical Clustering." <em>ApJ</em>, 490, 493.</li>
  <li id="ref2">Bartelmann, M. (1996). "Arcs from a universal dark-matter halo profile." <em>A&amp;A</em>. DOI: 10.48550/arXiv.astro-ph/9602053</li>
  <li id="ref3">Lin, Y.-T., Mohr, J. J., Stanford, S. A. (2004). "Near-infrared properties of galaxy clusters." <em>ApJ</em>. DOI: 10.1086/421714</li>
  <li id="ref4">Annunziatella, M., et al. (2014). "Galaxy density profiles in clusters." <em>A&amp;A</em>.</li>
  <li id="ref5">Sartoris, B., et al. (2020). "Cluster member spatial distributions." <em>A&amp;A</em>. DOI: 10.1051/0004-6361/202037521</li>
  <li id="ref6">Nagai, D., Kravtsov, A. V., Vikhlinin, A. (2007). "gNFW profile." <em>ApJ</em>. DOI: 10.1086/521328</li>
  <li id="ref7">Burkert, A. (1995). "Structure of Dark Matter Halos in Dwarf Galaxies." <em>ApJ</em>, 447, L25.</li>
  <li id="ref8">Hernquist, L. (1990). "An analytical model for spherical galaxies and bulges." <em>ApJ</em>, 356, 359.</li>
  <li id="ref9">Pedratti, S., et al. (2026). "Coma Cluster kinematics with DESI. I." <a href="https://arxiv.org/abs/2603.16706">arXiv:2603.16706</a></li>
  <li id="ref10">Gavazzi, R., et al. (2009). "Weak lensing mass of Coma." <em>A&amp;A</em>.</li>
  <li id="ref11">Umetsu, K., et al. (2016). "Cluster mass distributions from lensing." <em>ApJ</em>.</li>
  <li id="ref12">Mamon, G. A., Biviano, A., Boué, G. (2013). "MAMPOSSt." <em>MNRAS</em>, 429, 3079.</li>
  <li id="ref13">Biviano, A., et al. (2006). "Galaxy vs mass profile scale radii." <em>A&amp;A</em>.</li>
  <li id="ref14">Budzynski, J. M., et al. (2012). "Galaxy number density vs mass profile." <em>MNRAS</em>.</li>
</ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  <a href="/pages/Tag_Dark_Matter" class="wikilink">Dark Matter</a>
  <a href="/pages/Tag_Galaxy_Clusters" class="wikilink">Galaxy Clusters</a>
</div>
