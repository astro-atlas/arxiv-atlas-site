---
title: "Dust Polarimetry"
pageType: concept
status: done
---

<h1 class="page-title">Dust Polarimetry</h1>
<div class="infobox">
  <h3 class="infobox-title"><a href="/pages/dust" class="wikilink">dust</a> Polarimetry</h3>
  <table>
    <tr><th>Type:</th><td>Observational technique</td></tr>
    <tr><th>Wavelengths:</th><td>Far-infrared to submillimeter (50–850 μm)</td></tr>
    <tr><th>Key instruments:</th><td><a href="/pages/sofia-hawc-plus" class="wikilink">SOFIA</a>/HAWC+, JCMT/POL-2, ALMA</td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/davis-chandrasekhar-fermi-method" class="wikilink">DCF method</a><br />
        <a href="/pages/hourglass-magnetic-field-morphology" class="wikilink">Hourglass B-field morphology</a><br />
        <a href="/pages/faraday-rotation" class="wikilink">Faraday rotation</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Dust <a href="/pages/polarimetry" class="wikilink">polarimetry</a></strong> is the primary observational technique for mapping the plane-of-sky <a href="/pages/magnetic-field" class="wikilink">magnetic field</a> morphology in molecular clouds and star-forming regions. Non-spherical dust grains align with their long axes perpendicular to the local magnetic field direction; their thermal emission is therefore partially polarized, with the polarization E-vector perpendicular to the field<sup><a href="#ref1">[1]</a></sup>. By rotating observed polarization angles by 90°, astronomers infer the projected B-field orientation on the sky.
</p>
<h2 id="section-0">Physical Basis</h2>
<p>
  Dust grain alignment is primarily driven by radiative alignment torques (RATs), where anisotropic radiation fields spin up non-spherical grains and align them with the magnetic field<sup><a href="#ref1">[1]</a></sup>. The resulting polarized thermal emission at far-infrared and submillimeter wavelengths traces the B-field orientation integrated along the line of sight, weighted by dust <a href="/pages/column-density" class="wikilink">column density</a> and temperature.
</p>
<p>Key observational parameters include:</p>
<ul>
  <li><strong>Polarization fraction (p)</strong> — typically 1–15% in <a href="/pages/molecular-cloud" class="wikilink">molecular cloud</a>s; decreases with increasing column density due to field tangling and beam averaging</li>
  <li><strong>Polarization angle (θ)</strong> — derived from Stokes Q and U: θ = ½ arctan2(U, Q); B-field = θ + 90°</li>
  <li><strong>Quality cuts</strong> — standard thresholds include p/σ_p > 3, I/σ_I > 100, and p &lt; 30% to exclude unreliable detections<sup><a href="#ref2">[2]</a></sup><sup><a href="#ref3">[3]</a></sup></li>
</ul>
<h2 id="section-1">Instruments and Facilities</h2>
<p>
  Far-infrared dust polarimetry from space or airborne platforms is essential because the atmosphere is opaque at these wavelengths. <strong>SOFIA/HAWC+</strong> operated at 53–214 μm and was the primary facility for cloud-scale B-field mapping until SOFIA's retirement in 2022<sup><a href="#ref4">[4]</a></sup>. Ground-based submillimeter polarimetry is possible at 450 and 850 μm using JCMT/POL-2 (BISTRO survey) and at millimeter wavelengths with ALMA, which provides interferometric polarimetry at sub-arcsecond resolution.
</p>
<p>
  Large-scale Galactic B-field structure is traced by <strong>Planck</strong> 353 GHz polarization at 5′ resolution<sup><a href="#ref5">[5]</a></sup>, providing the context within which higher-resolution studies are interpreted.
</p>
<h2 id="section-2">Applications in <a href="/pages/star-formation" class="wikilink">star formation</a></h2>
<p>
  Dust polarimetry has revealed that B-fields are generally perpendicular to high-column-density filaments (N(H₂) > 5×10²¹ cm⁻²) but parallel or random in lower-density environments<sup><a href="#ref6">[6]</a></sup><sup><a href="#ref7">[7]</a></sup>. This orientation transition is a key diagnostic of the dynamical importance of magnetic fields relative to gravity and <a href="/pages/turbulence" class="wikilink">turbulence</a>.
</p>
<p>
  Combined with the <a href="/pages/davis-chandrasekhar-fermi-method" class="wikilink">Davis-Chandrasekhar-Fermi (DCF) method</a>, polarization angle dispersions yield estimates of B-field strength. Studies of <a href="/pages/infrared-dark-clouds" class="wikilink">infrared dark clouds</a> such as G351.77-0.53 have used HAWC+ 214 μm polarimetry to detect <a href="/pages/hourglass-magnetic-field-morphology" class="wikilink">hourglass-shaped B-field morphologies</a> indicative of magnetically regulated gravitational collapse<sup><a href="#ref8">[8]</a></sup>.
</p>
<h2 id="section-3">Limitations</h2>
<ul>
  <li><strong>Line-of-sight averaging</strong> — polarization traces a column-density-weighted mean field, washing out small-scale structure<sup><a href="#ref9">[9]</a></sup></li>
  <li><strong>Beam dilution</strong> — finite beam size averages over turbulent field variations, reducing observed polarization angle dispersion</li>
  <li><strong>Grain alignment efficiency</strong> — varies with radiation field, density, and grain size; depolarization in dense cores may not imply field disorder<sup><a href="#ref10">[10]</a></sup></li>
  <li><strong>Projection effects</strong> — only the plane-of-sky field component is measured; 3D reconstruction requires complementary techniques (e.g., starlight polarization, Zeeman observations)</li>
</ul>
<h2 id="section-4">See Also</h2>
<ul>
  <li><a href="/pages/2603-16425" class="wikilink">Jadhav et al. (2025) — Hourglass B-field in IRDC G351.77-0.53</a></li>
  <li><a href="/pages/davis-chandrasekhar-fermi-method" class="wikilink">Davis-Chandrasekhar-Fermi method</a></li>
  <li><a href="/pages/infrared-dark-clouds" class="wikilink">Infrared dark clouds</a></li>
  <li><a href="/pages/hourglass-magnetic-field-morphology" class="wikilink">Hourglass magnetic field morphology</a></li>
  <li><a href="/pages/faraday-rotation" class="wikilink">Faraday rotation</a> — complementary B-field technique for ionized gas</li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Andersson, B.-G., Lazarian, A., & Vaillancourt, J. E. (2015). "Interstellar Dust Grain Alignment." <em>ARA&A</em>, 53, 501.</li>
    <li id="ref2">Zielinski, N., et al. (2022). "Polarization quality criteria for SOFIA/HAWC+." <em>A&A</em>, 659, A22. DOI:10.1051/0004-6361/202141537</li>
    <li id="ref3">Li, D., et al. (2022). "SOFIA/HAWC+ polarimetric data analysis." <em>MNRAS</em>, 514, 3024. DOI:10.1093/mnras/stac1527</li>
    <li id="ref4">Harper, D. A., et al. (2018). "HAWC+: a far-infrared camera and polarimeter for SOFIA." <em>JAI</em>, 7, 1840008. DOI:10.1142/S2251171718400081</li>
    <li id="ref5">Planck Collaboration (2015). "Planck 353 GHz all-sky polarization maps." <em>A&A</em>, 576, A104. DOI:10.1051/0004-6361/201424082</li>
    <li id="ref6">Planck Collaboration (2016). "Planck results: B-fields in filamentary structures." <em>A&A</em>, 586, A138. DOI:10.1051/0004-6361/201525896</li>
    <li id="ref7">Soler, J. D., et al. (2017). "Column density-dependent B-field orientation." <em>A&A</em>, 603, A64. DOI:10.1051/0004-6361/201731049</li>
    <li id="ref8">Jadhav, O. R., et al. (2025). "Hourglass-Shaped Magnetic Field toward IRDC G351.77-0.53." arXiv:2603.16425</li>
    <li id="ref9">Houde, M., et al. (2009). "Dispersion of Magnetic Fields in Molecular Clouds. II." <em>ApJ</em>, 706, 1504. DOI:10.1088/0004-637X/706/2/1504</li>
    <li id="ref10">Pravash, K., et al. (2025). "Grain alignment and disruption in G34.43+0.24." <em>ApJ</em>, 981, 30. DOI:10.3847/1538-4357/adae06</li>
  </ol>
</details>
