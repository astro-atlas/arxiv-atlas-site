---
title: "Spatially Resolved Stellar Populations"
pageType: concept
status: done
level: specialist
---

<h1 class="page-title">Spatially Resolved Stellar Populations</h1>
<div class="infobox">
  <h3 class="infobox-title">Spatially Resolved Stellar Populations</h3>
  <table>
    <tr><th>Type:</th><td>Methodology / Analysis technique</td></tr>
    <tr><th>Level:</th><td>Specialist</td></tr>
    <tr><th>Key instruments:</th><td>IFU surveys (CALIFA, MaNGA, SAMI), multi-band photometry (J-PLUS)</td></tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/star-formation" class="wikilink">Star formation</a><br />
        <a href="/pages/metallicity-gradients" class="wikilink">Metallicity gradients</a><br />
        <a href="/pages/emission-line-diagnostics" class="wikilink">Emission-line diagnostics</a><br />
        <a href="/pages/dust" class="wikilink">Dust</a><br />
        <a href="/pages/quenching-star-formation" class="wikilink">Quenching</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Spatially resolved stellar population analysis</strong> refers to the determination of stellar population properties &mdash; age, metallicity, <a href="/pages/dust" class="wikilink">dust</a> attenuation, star formation rate &mdash; as a function of position within a galaxy, rather than from integrated (galaxy-wide) measurements. This approach reveals internal gradients, asymmetries, and substructure that integrated spectra average out, providing critical constraints on galaxy formation and evolution mechanisms<sup><a href="#ref1">[1]</a><a href="#ref2">[2]</a><a href="#ref3">[3]</a></sup>.
</p>
<h2 id="techniques">Techniques</h2>
<p>
  Two main approaches enable spatially resolved analysis:
</p>
<ul>
  <li><strong>Integral field spectroscopy (IFS):</strong> Surveys like CALIFA<sup><a href="#ref1">[1]</a><a href="#ref4">[4]</a></sup>, MaNGA, and SAMI<sup><a href="#ref5">[5]</a></sup> obtain spectra at every spatial element (spaxel), providing full spectral information for stellar population fitting. This yields the highest fidelity results but is limited in sample size and spatial coverage.</li>
  <li><strong>Multi-band photometric fitting:</strong> Surveys like J-PLUS use multiple narrow- and broad-band filters to construct low-resolution SEDs at each spatial pixel. Codes like AlStar fit stellar population models to these multi-band datacubes, producing IFS-like resolved maps<sup><a href="#ref6">[6]</a><a href="#ref7">[7]</a></sup>. This trades spectral resolution for much wider spatial coverage.</li>
</ul>
<h2 id="scaling-relations">Resolved Scaling Relations</h2>
<p>
  Spatially resolved analysis has revealed fundamental local scaling relations within galaxies<sup><a href="#ref1">[1]</a><a href="#ref2">[2]</a><a href="#ref3">[3]</a></sup>:
</p>
<ul>
  <li><strong>Age&ndash;&Sigma;<sub>&#9733;</sub> relation:</strong> Stellar age correlates with local <a href="/pages/stellar-mass-surface-density" class="wikilink">stellar mass surface density</a>, with denser regions being older. In undisturbed galaxies this reflects inside-out formation; in interaction-processed groups the relation can be flattened<sup><a href="#ref6">[6]</a></sup>.</li>
  <li><strong>Metallicity&ndash;&Sigma;<sub>&#9733;</sub> relation:</strong> <a href="/pages/metallicity-gradients" class="wikilink">Nebular metallicity</a> correlates with local stellar mass surface density. Again, interaction history modulates the slope<sup><a href="#ref6">[6]</a><a href="#ref8">[8]</a></sup>.</li>
  <li><strong>Resolved star-forming main sequence (RSFMS):</strong> Local SFR surface density correlates with local stellar mass surface density, extending the global SFMS to sub-galactic scales<sup><a href="#ref9">[9]</a><a href="#ref6">[6]</a></sup>.</li>
</ul>
<h2 id="applications">Applications to Galaxy Evolution</h2>
<p>
  Comparing resolved properties between the M51 and M101 <a href="/pages/galaxy-groups" class="wikilink">galaxy groups</a> demonstrates how interaction history reshapes internal galaxy properties: M51 group members show flattened gradients and <a href="/pages/quenching-star-formation" class="wikilink">quenching</a> signatures, while M101 members preserve steep inside-out gradients<sup><a href="#ref6">[6]</a></sup>. This approach has also revealed outside-in quenching patterns in M63 and identified M51b as a fully retired galaxy embedded in an interacting pair<sup><a href="#ref6">[6]</a></sup>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/metallicity-gradients" class="wikilink">Metallicity gradients</a></li>
  <li><a href="/pages/emission-line-diagnostics" class="wikilink">Emission-line diagnostics</a></li>
  <li><a href="/pages/quenching-star-formation" class="wikilink">Star formation quenching</a></li>
  <li><a href="/pages/2603-15869" class="wikilink">Thainá-Batista et al. (2026) &mdash; Resolved populations in M51 group</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
<ol>
  <li id="ref1">González Delgado, R. M. et al. (2014a). "Spatially resolved stellar populations from CALIFA. I." <em>A&amp;A</em>.</li>
  <li id="ref2">González Delgado, R. M. et al. (2015). "Spatially resolved stellar populations from CALIFA. II." <em>A&amp;A</em>.</li>
  <li id="ref3">González Delgado, R. M. et al. (2016). "Spatially resolved stellar populations from CALIFA. III." <em>A&amp;A</em>.</li>
  <li id="ref4">García-Benito, R. et al. (2017). "CALIFA data release 3." <em>A&amp;A</em>.</li>
  <li id="ref5">Croom, S. M. et al. (2024). "SAMI Galaxy Survey." <em>MNRAS</em>. DOI:10.1093/mnras/stae458</li>
  <li id="ref6">Thainá-Batista, J. et al. (2026). "Spatially resolved stellar populations in the M51 group with J-PLUS. II." <em>A&amp;A</em> (accepted). <a href="https://arxiv.org/abs/2603.15869">arXiv:2603.15869</a></li>
  <li id="ref7">Rodríguez-Martín, J. E. et al. (2025). "J-PLUS extragalactic science methodology."</li>
  <li id="ref8">Barrera-Ballesteros, J. K. et al. (2016). "Resolved metallicity relations." <em>MNRAS</em>. DOI:10.1093/mnras/stw1984</li>
  <li id="ref9">Sánchez, S. F. et al. (2020). "The resolved star-forming main sequence." <em>ARA&amp;A</em>.</li>
</ol>
</details>
