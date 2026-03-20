---
title: "Mass-to-Flux Ratio"
pageType: concept
status: done
---

<h1 class="page-title">Mass-to-Flux Ratio</h1>
<div class="infobox">
  <h3 class="infobox-title">Mass-to-Flux Ratio (λ)</h3>
  <table>
    <tr><th>Type:</th><td>Diagnostic parameter</td></tr>
    <tr><th>Symbol:</th><td>λ (dimensionless, normalized)</td></tr>
    <tr><th>Critical value:</th><td>λ = 1</td></tr>
    <tr><th>Formula:</th><td>λ = 7.6 × 10⁻²¹ N(H₂)/B_tot</td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/magnetic-fields-in-star-formation" class="wikilink">B-fields in star formation</a><br />
        <a href="/pages/davis-chandrasekhar-fermi-method" class="wikilink">DCF method</a><br />
        <a href="/pages/gravity" class="wikilink">Gravitational collapse</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>mass-to-flux ratio</strong> (λ) is the fundamental diagnostic parameter for assessing whether <a href="/pages/magnetic-field" class="wikilink">magnetic fields</a> can prevent <a href="/pages/gravity" class="wikilink">gravitational collapse</a> in a <a href="/pages/molecular-cloud" class="wikilink">molecular cloud</a>. It compares the gravitational mass of a cloud to its magnetic flux, normalized to the critical value at which they are in balance<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup>.
</p>
<h2 id="section-0">Definition</h2>
<p>The observed mass-to-flux ratio is<sup><a href="#ref1">[1]</a></sup>:</p>
<p style="text-align:center; font-size:1.1em;">
  <strong>λ<sub>obs</sub> = 7.6 × 10⁻²¹ × N(H₂) / B<sub>tot</sub></strong>
</p>
<p>where N(H₂) is the <a href="/pages/column-density" class="wikilink">column density</a> (cm⁻²) and B_tot is the total magnetic field strength (μG). Since <a href="/pages/dust-polarimetry" class="wikilink">dust polarimetry</a> only measures the plane-of-sky component B_POS, a statistical correction B_tot = 1.3 × B_POS is applied<sup><a href="#ref1">[1]</a></sup>.</p>
<h2 id="section-1">Magnetic Criticality Regimes</h2>
<ul>
  <li><strong>Subcritical (λ &lt; 1)</strong> — magnetic pressure exceeds gravity; the cloud cannot collapse unless flux is lost (e.g., via ambipolar diffusion)<sup><a href="#ref3">[3]</a></sup></li>
  <li><strong>Transcritical (λ ~ 1)</strong> — magnetic and gravitational forces are comparable; the cloud is on the edge of stability. G351.77-0.53 shows λ ~ 0.9 ± 0.6<sup><a href="#ref4">[4]</a></sup></li>
  <li><strong>Supercritical (λ &gt; 1)</strong> — gravity overwhelms magnetic support; collapse proceeds dynamically. Near clump c1 in G351, λ > 1<sup><a href="#ref4">[4]</a></sup></li>
</ul>
<h2 id="section-2">Spatial Variations</h2>
<p>
  The mass-to-flux ratio is not uniform across a cloud. In magnetically regulated collapse models, λ increases from the cloud envelope (subcritical/transcritical) to the dense core (supercritical) as mass accumulates faster than magnetic flux<sup><a href="#ref3">[3]</a></sup>. This gradient is observed in G351.77-0.53 and is consistent with the <a href="/pages/hourglass-magnetic-field-morphology" class="wikilink">hourglass B-field morphology</a><sup><a href="#ref4">[4]</a></sup>.
</p>
<h2 id="section-3">Uncertainties</h2>
<p>
  Mass-to-flux ratio estimates carry substantial uncertainties from: (1) B_POS from the <a href="/pages/davis-chandrasekhar-fermi-method" class="wikilink">DCF method</a> (factor ~2), (2) <a href="/pages/column-density" class="wikilink">column density</a> measurements (factor ~1.5 from temperature and abundance assumptions), and (3) the B_tot = 1.3 × B_POS statistical correction, which assumes random field inclinations.
</p>
<h2 id="section-4">See Also</h2>
<ul>
  <li><a href="/pages/2603-16425" class="wikilink">Jadhav et al. (2025)</a></li>
  <li><a href="/pages/magnetic-fields-in-star-formation" class="wikilink">Magnetic fields in star formation</a></li>
  <li><a href="/pages/davis-chandrasekhar-fermi-method" class="wikilink">DCF method</a></li>
  <li><a href="/pages/gravity" class="wikilink">Gravitational collapse</a></li>
  <li><a href="/pages/column-density" class="wikilink">Column density</a></li>
  <li><a href="/pages/hourglass-magnetic-field-morphology" class="wikilink">Hourglass B-field morphology</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Crutcher, R. M. (2004). "Mass-to-flux ratio." <em>Ap&SS</em>, 292, 225. DOI:10.1023/B:ASTR.0000045021.42255.95</li>
    <li id="ref2">Crutcher, R. M. (2012). "Magnetic Fields in Molecular Clouds." <em>ARA&A</em>, 50, 29. DOI:10.1146/annurev-astro-081811-125514</li>
    <li id="ref3">Nakamura, F. & Li, Z.-Y. (2008). "Magnetically Regulated Star Formation." <em>ApJ</em>, 687, 354. DOI:10.1086/591641</li>
    <li id="ref4">Jadhav, O. R., et al. (2025). "Hourglass B-field toward IRDC G351.77-0.53." arXiv:2603.16425</li>
  </ol>
</details>
