---
title: "Davis-Chandrasekhar-Fermi Method"
pageType: concept
status: done
---

<h1 class="page-title">Davis-Chandrasekhar-Fermi (DCF) Method</h1>
<div class="infobox">
  <h3 class="infobox-title">DCF Method</h3>
  <table>
    <tr><th>Type:</th><td>Analysis technique</td></tr>
    <tr><th>First described:</th><td>1951 (Davis), 1953 (Chandrasekhar & Fermi)</td></tr>
    <tr><th>Measures:</th><td>Plane-of-sky B-field strength (B_POS)</td></tr>
    <tr>
      <th>Inputs:</th>
      <td>
        Gas density, velocity dispersion, polarization angle dispersion
      </td>
    </tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/dust-polarimetry" class="wikilink">Dust polarimetry</a><br />
        <a href="/pages/magnetic-field" class="wikilink">Magnetic fields</a><br />
        <a href="/pages/mass-to-flux-ratio" class="wikilink">Mass-to-flux ratio</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>Davis-Chandrasekhar-Fermi (DCF) method</strong> is the most widely used technique for estimating the plane-of-sky magnetic field strength in <a href="/pages/molecular-cloud" class="wikilink">molecular clouds</a> from <a href="/pages/dust-polarimetry" class="wikilink">dust polarimetry</a> data. The core idea is that <a href="/pages/turbulence" class="wikilink">turbulent</a> gas motions perturb the <a href="/pages/magnetic-field" class="wikilink">magnetic field</a> lines, and the degree of perturbation (measured as polarization angle dispersion) is inversely related to the field strength<sup><a href="#ref1">[1]</a></sup>.
</p>
<h2 id="section-0">The DCF Equation</h2>
<p>The classical DCF formula is:</p>
<p style="text-align:center; font-size:1.1em;">
  <strong>B<sub>POS</sub> = Q × √(4πρ) × σ<sub>V,nt</sub> / δθ</strong>
</p>
<p>or equivalently in convenient units<sup><a href="#ref2">[2]</a></sup>:</p>
<p style="text-align:center;">
  B<sub>POS</sub> ≈ 9.3 × √n(H₂) × ΔV<sub>nt</sub> / δθ &nbsp; [μG]
</p>
<p>where:</p>
<ul>
  <li><strong>Q</strong> — correction factor (typically 0.5) accounting for non-ideal conditions<sup><a href="#ref2">[2]</a></sup></li>
  <li><strong>ρ, n(H₂)</strong> — gas mass density / number density</li>
  <li><strong>σ<sub>V,nt</sub>, ΔV<sub>nt</sub></strong> — non-thermal (turbulent) velocity dispersion from molecular line observations</li>
  <li><strong>δθ</strong> — dispersion of polarization position angles (radians)</li>
</ul>
<h2 id="section-1">Measuring Angle Dispersion</h2>
<h3>Structure Function Method</h3>
<p>
  The angular structure function D(ℓ) = ⟨[θ(x) − θ(x+ℓ)]²⟩^(1/2) separates turbulent (b²), large-scale (m²ℓ²), and noise (σ_M²) contributions to angle dispersion<sup><a href="#ref3">[3]</a></sup><sup><a href="#ref4">[4]</a></sup>. The turbulent component b gives δθ. In G351.77-0.53, this yields δθ = 8.3° ± 1.5°<sup><a href="#ref5">[5]</a></sup>.
</p>
<h3>Sliding Box Method</h3>
<p>
  A complementary approach computes δθ locally within sliding boxes of ~5× beam size, producing pixel-by-pixel B-field strength maps<sup><a href="#ref6">[6]</a></sup>. This reveals spatial variations — in G351, B_POS reaches ~0.8 mG near the densest clump c1<sup><a href="#ref5">[5]</a></sup>.
</p>
<h2 id="section-2">Limitations and the Q Factor</h2>
<p>The DCF method carries significant systematic uncertainties:</p>
<ul>
  <li><strong>Q factor</strong> — ranges from 0.2 to 1 depending on turbulence regime, cloud geometry, and magnetization level. In strongly magnetized systems Q → 1; in weakly magnetized/self-gravitating systems Q ~ 0.3–0.4<sup><a href="#ref7">[7]</a></sup></li>
  <li><strong>Beam/LOS integration</strong> — finite beam size and line-of-sight averaging reduce the observed δθ, causing B_POS to be overestimated<sup><a href="#ref8">[8]</a></sup></li>
  <li><strong>Velocity-field coupling</strong> — the assumption that turbulent velocities and B-field perturbations are correlated breaks down in complex environments</li>
  <li><strong>Non-turbulent motions</strong> — stellar feedback, outflows, and systematic flows contaminate σ<sub>V,nt</sub></li>
</ul>
<h2 id="section-3">Application: G351.77-0.53</h2>
<p>
  In the <a href="/pages/infrared-dark-clouds" class="wikilink">IRDC</a> G351.77-0.53, the DCF method with Q = 0.5 yields a mean B_POS ~ 147 ± 60 μG (structure function) or ~170 ± 127 μG (sliding box). Combined with <a href="/pages/column-density" class="wikilink">column density</a> to compute the <a href="/pages/mass-to-flux-ratio" class="wikilink">mass-to-flux ratio</a> λ ~ 0.9 ± 0.6, this indicates a magnetically transcritical cloud with B-fields dynamically important in regulating collapse<sup><a href="#ref5">[5]</a></sup>.
</p>
<h2 id="section-4">See Also</h2>
<ul>
  <li><a href="/pages/2603-16425" class="wikilink">Jadhav et al. (2025)</a></li>
  <li><a href="/pages/dust-polarimetry" class="wikilink">Dust polarimetry</a> — provides the input data</li>
  <li><a href="/pages/mass-to-flux-ratio" class="wikilink">Mass-to-flux ratio</a> — derived from DCF results</li>
  <li><a href="/pages/magnetic-fields-in-star-formation" class="wikilink">Magnetic fields in star formation</a></li>
  <li><a href="/pages/turbulence" class="wikilink">Turbulence</a> — provides velocity dispersion input</li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Chandrasekhar, S. & Fermi, E. (1953). "Magnetic Fields in Spiral Arms." <em>ApJ</em>, 118, 113. DOI:10.1086/145731</li>
    <li id="ref2">Crutcher, R. M. (2012). "Magnetic Fields in Molecular Clouds." <em>ARA&A</em>, 50, 29. DOI:10.1146/annurev-astro-081811-125514</li>
    <li id="ref3">Hildebrand, R. H., et al. (2009). "Dispersion of Magnetic Fields in Molecular Clouds. I." <em>ApJ</em>, 696, 567. DOI:10.1088/0004-637X/696/1/567</li>
    <li id="ref4">Houde, M., et al. (2004). "Polarimetry structure functions." <em>ApJ</em>, 616, 111. DOI:10.1086/382067</li>
    <li id="ref5">Jadhav, O. R., et al. (2025). "Hourglass B-field toward IRDC G351.77-0.53." arXiv:2603.16425</li>
    <li id="ref6">Hwang, J., et al. (2021). "Sliding box DCF in OMC-1." <em>ApJ</em>, 913, 85. DOI:10.3847/1538-4357/abf3c4</li>
    <li id="ref7">Liu, J., et al. (2021). "DCF correction factor in MHD simulations." <em>ApJ</em>, 919, 79. DOI:10.3847/1538-4357/ac0cec</li>
    <li id="ref8">Houde, M., et al. (2009). "Dispersion of Magnetic Fields. II." <em>ApJ</em>, 706, 1504. DOI:10.1088/0004-637X/706/2/1504</li>
  </ol>
</details>
