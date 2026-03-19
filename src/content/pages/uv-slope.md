---
title: "UV Slope"
pageType: concept
status: done
level: intermediate
---

<h1 class="page-title">UV Slope (&beta;<sub>UV</sub>)</h1>
<div class="infobox">
  <h3 class="infobox-title">UV Slope</h3>
  <table>
    <tr><th>Type:</th><td>Observational diagnostic</td></tr>
    <tr><th>Level:</th><td>Intermediate</td></tr>
    <tr><th>Definition:</th><td>Power-law index of rest-frame UV continuum (f<sub>&lambda;</sub> &prop; &lambda;<sup>&beta;</sup>)</td></tr>
    <tr><th>Wavelength range:</th><td>~1200&ndash;3000 &Aring; (rest-frame)</td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/mv-betauv-relation" class="wikilink">M<sub>UV</sub>&ndash;&beta;<sub>UV</sub> relation</a><br />
        <a href="/pages/dust" class="wikilink">Interstellar dust</a><br />
        <a href="/pages/high-redshift-galaxies" class="wikilink">High-redshift galaxies</a><br />
        <a href="/pages/red-monsters" class="wikilink">Red monsters</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>UV slope</strong> (&beta;<sub>UV</sub>) parameterizes the shape of a galaxy&rsquo;s rest-frame ultraviolet continuum as a power law f<sub>&lambda;</sub> &prop; &lambda;<sup>&beta;</sup>, typically measured over the range ~1200&ndash;3000 &Aring;. It is one of the most accessible observables for characterizing stellar populations, <a href="/pages/dust" class="wikilink">dust</a> content, and ionizing conditions in galaxies, particularly at high redshift where the UV rest-frame is redshifted into the near-infrared and observable with JWST.
</p>
<h2 id="physical-drivers">Physical Drivers</h2>
<p>
  The UV slope is shaped by the interplay of several physical processes:
</p>
<ul>
  <li><strong>Stellar population age and metallicity:</strong> Young, metal-poor populations produce intrinsically blue slopes (&beta;<sub>UV</sub> &asymp; &minus;2.5 to &minus;3), while older or more metal-rich populations are somewhat redder<a href="#ref1">[1]</a>.</li>
  <li><strong><a href="/pages/dust" class="wikilink">Dust</a> attenuation:</strong> Even modest amounts of dust can significantly redden the UV slope. Applying the Calzetti dust law<a href="#ref2">[2]</a>, A<sub>V</sub> ~ 1 mag shifts &beta;<sub>UV</sub> by &Delta;&beta; ~ +1.5&ndash;2<a href="#ref3">[3]</a>.</li>
  <li><strong><a href="/pages/nebular-continuum" class="wikilink">Nebular continuum</a> emission:</strong> Strong free-bound and two-photon emission from ionized gas can redden the UV slope under extreme conditions (high gas density, high ionization parameter), even without dust<a href="#ref4">[4]</a>.</li>
  <li><strong>AGN contribution:</strong> An active galactic nucleus can modify the UV continuum shape through power-law emission<a href="#ref5">[5]</a>.</li>
</ul>
<h2 id="measurement">Measurement Methods</h2>
<p>
  The UV slope is measured either from spectroscopy (fitting a power law to the rest-frame 1350&ndash;2600 &Aring; continuum) or from broadband photometry (fitting photometric points sampling the UV rest-frame). At z &gt; 10, these rest-frame wavelengths are redshifted to &lambda;<sub>obs</sub> ~ 1.5&ndash;3 &mu;m, well within JWST/NIRCam coverage. Spectroscopic measurements are preferred but require sufficient S/N; photometric measurements are more common but susceptible to systematic effects from photometric scatter and emission-line contamination<a href="#ref5">[5]</a>.
</p>
<h2 id="high-z-galaxies">UV Slopes at z &gt; 10</h2>
<p>
  JWST has enabled systematic UV slope measurements at z &gt; 10, revealing that the majority of galaxies at these epochs have extremely blue slopes (&beta;<sub>UV</sub> &lt; &minus;2.5), consistent with young, metal-poor, dust-poor stellar populations<a href="#ref1">[1]</a><a href="#ref6">[6]</a>. These blue slopes follow the canonical <a href="/pages/mv-betauv-relation" class="wikilink">M<sub>UV</sub>&ndash;&beta;<sub>UV</sub> relation</a> at z ~ 10&ndash;12<a href="#ref1">[1]</a>.
</p>
<p>
  However, a minority population of red UV continuum sources (&beta;<sub>UV</sub> &gt; &minus;1.5) deviates significantly from this relation<a href="#ref3">[3]</a><a href="#ref7">[7]</a>. The spectroscopic confirmation of EGS-z11-R0 at z = 11.45 with &beta;<sub>UV</sub> &asymp; &minus;1.0 demonstrated that such red slopes result primarily from <a href="/pages/dust" class="wikilink">dust</a> attenuation (A<sub>V</sub> ~ 1 mag), identifying the source as a &ldquo;<a href="/pages/red-monsters" class="wikilink">red monster</a>&rdquo;<a href="#ref5">[5]</a>. The existence of both blue and red populations supports an evolutionary picture in which galaxies alternate between dust-obscured and dust-free phases at <a href="/pages/cosmic-dawn" class="wikilink">cosmic dawn</a><a href="#ref8">[8]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/mv-betauv-relation" class="wikilink">M<sub>UV</sub>&ndash;&beta;<sub>UV</sub> relation</a> &mdash; canonical UV colour-magnitude relation</li>
  <li><a href="/pages/dust" class="wikilink">Interstellar dust</a> &mdash; primary reddening agent</li>
  <li><a href="/pages/nebular-continuum" class="wikilink">Nebular continuum</a> &mdash; alternative reddening mechanism</li>
  <li><a href="/pages/red-monsters" class="wikilink">Red monsters</a> &mdash; dust-reddened galaxies at cosmic dawn</li>
  <li><a href="/pages/high-redshift-galaxies" class="wikilink">High-redshift galaxies</a> &mdash; the population where UV slopes are most diagnostic</li>
  <li><a href="/pages/2603-15841" class="wikilink">Rodighiero et al. (2026)</a> &mdash; UV slope measurement of EGS-z11-R0</li>
</ul>
<div class="references">
<h2>References</h2>
<ol>
  <li id="ref1">Cullen, F. et al. (2024). "UV slope-magnitude relation at z ~ 10&ndash;12."</li>
  <li id="ref2">Calzetti, D. et al. (2000). "The dust content of star-forming galaxies." <em>ApJ</em>, 533, 682. DOI:10.1086/308692</li>
  <li id="ref3">Mitsuhashi, I. et al. (2025). "Red candidates at z ~ 12 deviating from the M<sub>UV</sub>&ndash;&beta;<sub>UV</sub> relation."</li>
  <li id="ref4">Katz, H. et al. (2025). "Nebular continuum emission effects on UV slopes at high redshift."</li>
  <li id="ref5">Rodighiero, G. et al. (2026). "EGS-z11-R0: a red, dust-rich galaxy at Cosmic Dawn." <a href="https://arxiv.org/abs/2603.15841">arXiv:2603.15841</a></li>
  <li id="ref6">Morales, A. M. et al. (2024). "UV slope measurements at z &gt; 10."</li>
  <li id="ref7">Rodighiero, G. et al. (2023). "Discovery of red UV continuum candidates at high redshift."</li>
  <li id="ref8">Ferrara, A. (2024). "Red Monsters and Blue Monsters: radiative feedback and the early growth of galaxies."</li>
</ol>
</div>
