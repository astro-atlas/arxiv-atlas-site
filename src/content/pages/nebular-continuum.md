---
title: "Nebular Continuum"
pageType: concept
status: done
level: intermediate
---

<h1 class="page-title">Nebular Continuum</h1>
<div class="infobox">
  <h3 class="infobox-title">Nebular Continuum</h3>
  <table>
    <tr><th>Type:</th><td>Emission mechanism</td></tr>
    <tr><th>Level:</th><td>Intermediate</td></tr>
    <tr><th>Origin:</th><td>Ionized gas (H II regions, diffuse ISM)</td></tr>
    <tr><th>Components:</th><td>Free-free (bremsstrahlung), free-bound (recombination), two-photon</td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/uv-slope" class="wikilink">UV slope</a><br />
        <a href="/pages/interstellar-medium" class="wikilink">ISM</a><br />
        <a href="/pages/star-formation" class="wikilink">Star formation</a><br />
        <a href="/pages/emission-line-diagnostics" class="wikilink">Emission-line diagnostics</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>nebular continuum</strong> is continuous electromagnetic radiation emitted by ionized gas, as distinct from the discrete emission lines produced by bound-bound transitions. It arises from three physical processes in ionized hydrogen (and helium) gas: free-free emission (bremsstrahlung), free-bound emission (recombination continuum), and two-photon emission from metastable states. In galaxies with intense <a href="/pages/star-formation" class="wikilink">star formation</a> and high ionization parameters, nebular continuum emission can contribute significantly to the observed broadband flux, particularly in the rest-frame UV and optical<a href="#ref1">[1]</a>.
</p>
<h2 id="components">Emission Components</h2>
<ul>
  <li><strong>Free-free (bremsstrahlung):</strong> Radiation emitted by electrons decelerated in the Coulomb field of ions. Produces a relatively flat spectrum that can extend from radio to X-ray wavelengths. Dominates at longer wavelengths.</li>
  <li><strong>Free-bound (recombination):</strong> Radiation emitted when a free electron is captured by an ion. Produces continuum edges at the ionization thresholds of hydrogen (Lyman, Balmer, Paschen continua) and helium. Particularly important in the UV.</li>
  <li><strong>Two-photon:</strong> Emission from the metastable 2s state of hydrogen, which decays by emitting two photons whose energies sum to Ly&alpha; (10.2 eV). Produces a broad continuum peaking at ~1400 &Aring;. Important in the UV for high-ionization nebulae<a href="#ref1">[1]</a>.</li>
</ul>
<h2 id="uv-reddening">Effect on UV Slopes</h2>
<p>
  Strong nebular continuum emission can redden the observed <a href="/pages/uv-slope" class="wikilink">UV slope</a> of a galaxy even in the absence of <a href="/pages/dust" class="wikilink">dust</a>, because the nebular continuum has a shallower spectral slope than the intrinsic stellar UV continuum<a href="#ref1">[1]</a>. This effect is proposed as an alternative explanation for the red UV slopes observed in some <a href="/pages/high-redshift-galaxies" class="wikilink">z &gt; 10 galaxies</a>, alongside dust attenuation<a href="#ref2">[2]</a>.
</p>
<p>
  However, producing a significant UV reddening (&Delta;&beta;<sub>UV</sub> ~ +1 to +2) through nebular continuum alone requires extreme conditions: gas densities n<sub>H</sub> &gt; 10<sup>4</sup> cm<sup>&minus;3</sup>, stellar effective temperatures T<sub>eff</sub> &gt; 5 &times; 10<sup>4</sup> K, and ionizing photon production efficiencies well above standard stellar population models<a href="#ref2">[2]</a><a href="#ref1">[1]</a>. For EGS-z11-R0 at z = 11.45, SED modeling shows that dust attenuation is the primary driver of the red UV slope (&beta;<sub>UV</sub> &asymp; &minus;1.0), with nebular continuum playing a secondary role<a href="#ref3">[3]</a>.
</p>
<h2 id="diagnostics">Diagnostic Value</h2>
<p>
  The strength of the nebular continuum relative to the stellar continuum provides diagnostic information about:
</p>
<ul>
  <li><strong>Ionization parameter (log U):</strong> Higher ionization parameters produce stronger nebular continuum relative to stellar emission.</li>
  <li><strong>Electron density:</strong> Denser gas produces stronger free-free and recombination emission per unit volume.</li>
  <li><strong>Escape fraction of ionizing photons:</strong> If most ionizing photons are absorbed by gas (low escape fraction), nebular continuum is maximized.</li>
</ul>
<p>
  Separating nebular continuum from stellar and <a href="/pages/dust" class="wikilink">dust</a> contributions requires multi-component SED modeling with photoionization codes such as Cloudy<a href="#ref4">[4]</a><a href="#ref5">[5]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/uv-slope" class="wikilink">UV slope</a> &mdash; observable affected by nebular continuum</li>
  <li><a href="/pages/dust" class="wikilink">Interstellar dust</a> &mdash; competing reddening mechanism</li>
  <li><a href="/pages/emission-line-diagnostics" class="wikilink">Emission-line diagnostics</a> &mdash; companion line emission</li>
  <li><a href="/pages/red-monsters" class="wikilink">Red monsters</a> &mdash; population where nebular vs. dust reddening is debated</li>
  <li><a href="/pages/2603-15841" class="wikilink">Rodighiero et al. (2026)</a> &mdash; EGS-z11-R0 UV slope analysis</li>
</ul>
<div class="references">
<h2>References</h2>
<ol>
  <li id="ref1">Katz, H. et al. (2025). "Nebular continuum emission effects on UV slopes at high redshift."</li>
  <li id="ref2">Mitsuhashi, I. et al. (2025). "Red candidates at z ~ 12 deviating from the M<sub>UV</sub>&ndash;&beta;<sub>UV</sub> relation."</li>
  <li id="ref3">Rodighiero, G. et al. (2026). "EGS-z11-R0: a red, dust-rich galaxy at Cosmic Dawn." <a href="https://arxiv.org/abs/2603.15841">arXiv:2603.15841</a></li>
  <li id="ref4">Ferland, G. J. et al. (1998). "CLOUDY 90: Numerical Simulation of Plasmas and their Spectra." <em>PASP</em>, 110, 761.</li>
  <li id="ref5">Ferland, G. J. et al. (2013). "The 2013 Release of Cloudy." <em>RMxAA</em>, 49, 137.</li>
</ol>
</div>
