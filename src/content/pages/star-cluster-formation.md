---
title: "Star Cluster Formation"
pageType: concept
status: done
---

<h1 class="page-title">Star Cluster Formation</h1>
<div class="infobox">
  <h3 class="infobox-title">Star Cluster Formation</h3>
  <table>
    <tr><th>Type:</th><td>Intermediate concept</td></tr>
    <tr><th>Setting:</th><td><a href="/pages/molecular-cloud" class="wikilink">Giant molecular clouds</a></td></tr>
    <tr><th>Timescale:</th><td>~1–10 Myr (embedded phase)</td></tr>
    <tr><th>Key process:</th><td>Gravoturbulent fragmentation → subcluster merging</td></tr>
    <tr><th>Related:</th>
      <td>
        <a href="/pages/star-formation" class="wikilink">Star formation</a><br />
        <a href="/pages/fractal-structure-star-clusters" class="wikilink">Fractal structure of star clusters</a><br />
        <a href="/pages/stellar-feedback" class="wikilink">Stellar feedback</a><br />
        <a href="/pages/dynamical-relaxation-clusters" class="wikilink">Dynamical relaxation</a><br />
        <a href="/pages/subcluster-formation" class="wikilink">Subcluster formation</a><br />
        <a href="/pages/magnetohydrodynamics" class="wikilink">Magnetohydrodynamics</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Star cluster formation</strong> is the process by which a population of gravitationally interacting stars assembles from a collapsing <a href="/pages/molecular-cloud" class="wikilink">molecular cloud</a>. Most stars in the Milky Way are thought to have formed in clustered environments<sup><a href="#ref1">1</a></sup>, and the dynamical and structural properties of clusters at birth set the stage for their long-term evolution and dissolution.
</p>
<h2 id="global-collapse">Global Hierarchical Collapse</h2>
<p>
  Current models invoke the global hierarchical collapse of giant molecular clouds (GMCs)<sup><a href="#ref2">2</a></sup><sup><a href="#ref3">3</a></sup>. As a cloud undergoes gravoturbulent collapse<sup><a href="#ref4">4</a></sup><sup><a href="#ref5">5</a></sup>, it fragments into dense, star-forming clumps — subclusters — that can merge over time into a single, larger cluster. The initial stellar distribution is therefore hierarchical and <a href="/pages/fractal-structure-star-clusters" class="wikilink">fractal</a>, inheriting the spatial structure of the natal cloud.
</p>
<h2 id="centrally-concentrated">Centrally Concentrated Formation</h2>
<p>
  A class of models considers star formation within centrally concentrated molecular cloud structures, where the gas density profile is roughly uniform in the center and declines steeply at large radii<sup><a href="#ref6">6</a></sup><sup><a href="#ref7">7</a></sup>. In this scenario, as modeled by the Torch simulation framework<sup><a href="#ref8">8</a></sup><sup><a href="#ref9">9</a></sup>, clusters form with fractal substructure that is gradually erased by dynamical relaxation at approximately 2.5 free-fall times.<sup><a href="#ref10">10</a></sup>
</p>
<h2 id="gas-expulsion">Gas Expulsion and Cluster Survival</h2>
<p>
  After the embedded phase, <a href="/pages/stellar-feedback" class="wikilink">stellar feedback</a> — particularly photoionization and stellar winds — drives gas expulsion. Clusters that retain a sufficient fraction of their stars survive as bound systems; others dissolve into the field.<sup><a href="#ref1">1</a></sup><sup><a href="#ref11">11</a></sup> The star formation efficiency (SFE) profile within the cloud plays a critical role: centrally peaked SFE profiles lead to more resilient clusters.<sup><a href="#ref6">6</a></sup><sup><a href="#ref12">12</a></sup>
</p>
<h2 id="simulations">Key Simulation Frameworks</h2>
<ul>
  <li><strong>Torch</strong>: Couples FLASH MHD<sup><a href="#ref13">13</a></sup> with AMUSE N-body<sup><a href="#ref14">14</a></sup>; includes self-consistent gas dynamics, star formation via sink particles, stellar evolution (SeBa), radiative transfer, and gravitational N-body (ph4 integrator).<sup><a href="#ref8">8</a></sup><sup><a href="#ref9">9</a></sup></li>
  <li><strong>SPH codes</strong>: Early simulations by Bonnell et al. (2003<sup><a href="#ref15">15</a></sup>, 2008<sup><a href="#ref16">16</a></sup>) established the hierarchical assembly picture.</li>
</ul>
<h2 id="open-questions">Open Questions</h2>
<ul>
  <li>What initial conditions (density profile, magnetic field, turbulence) determine whether a forming cluster survives gas expulsion?</li>
  <li>How universal is the ~2.5 t<sub>ff</sub> fractal erasure timescale across different cloud environments?</li>
  <li>What role does the initial mass function (IMF) stochasticity play in cluster structural evolution?</li>
</ul>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/star-formation" class="wikilink">Star formation</a></li>
  <li><a href="/pages/fractal-structure-star-clusters" class="wikilink">Fractal structure of star clusters</a></li>
  <li><a href="/pages/q-parameter-fractality" class="wikilink">Q parameter (fractality)</a></li>
  <li><a href="/pages/subcluster-formation" class="wikilink">Subcluster formation</a></li>
  <li><a href="/pages/stellar-feedback" class="wikilink">Stellar feedback</a></li>
  <li><a href="/pages/dynamical-relaxation-clusters" class="wikilink">Dynamical relaxation in clusters</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Lada, C. J. &amp; Lada, E. A. (2003). "Embedded clusters in molecular clouds." <em>ARA&amp;A</em>, 41, 57–115.</li>
    <li id="ref2">Vázquez-Semadeni, E. et al. (2017). "Hierarchical star cluster assembly in globally collapsing molecular clouds." <em>MNRAS</em>, 467, 1313–1328.</li>
    <li id="ref3">Grudić, M. Y. et al. (2018). "From the top down and back up again." <em>MNRAS</em>, 481, 688–702.</li>
    <li id="ref4">Larson, R. B. (1981). "Turbulence and star formation in molecular clouds." <em>MNRAS</em>, 194, 809–826.</li>
    <li id="ref5">Mac Low, M.-M. &amp; Klessen, R. S. (2004). "Control of star formation by supersonic turbulence." <em>Rev. Mod. Phys.</em>, 76, 125.</li>
    <li id="ref6">Shukirgaliyev, B. et al. (2017). "Impact of a star formation efficiency profile on the evolution of open clusters." <em>A&amp;A</em>, 605, A119.</li>
    <li id="ref7">Parmentier, G. &amp; Pfalzner, S. (2013). "Local-density-driven clustered star formation." <em>A&amp;A</em>, 549, A132.</li>
    <li id="ref8">Wall, J. E. et al. (2019). "Collisional N-body dynamics coupled to self-gravitating MHD." <em>ApJ</em>, 887, 62.</li>
    <li id="ref9">Wall, J. E. et al. (2020). "Modeling of the effects of stellar feedback during star cluster formation." <em>ApJ</em>, 904, 192.</li>
    <li id="ref10">Akhmetali, A. et al. (2026). "Evolution of fractality in centrally concentrated young clusters." <em>A&amp;A</em> (submitted). <a href="https://arxiv.org/abs/2603.16183">arXiv:2603.16183</a></li>
    <li id="ref11">Portegies Zwart, S. F. et al. (2010). "Young massive star clusters." <em>ARA&amp;A</em>, 48, 431–493.</li>
    <li id="ref12">Shukirgaliyev, B. et al. (2018). "The Long-term Evolution of Star Clusters Formed with a Centrally Peaked SFE Profile." <em>ApJ</em>, 863, 171.</li>
    <li id="ref13">Fryxell, B. et al. (2000). "FLASH: An Adaptive Mesh Hydrodynamics Code." <em>ApJS</em>, 131, 273.</li>
    <li id="ref14">Pelupessy, F. I. et al. (2013). "The astrophysical multipurpose software environment." <em>A&amp;A</em>, 557, A84.</li>
    <li id="ref15">Bonnell, I. A. et al. (2003). "The hierarchical formation of a stellar cluster." <em>MNRAS</em>, 343, 413–418.</li>
    <li id="ref16">Bonnell, I. A. et al. (2008). "Gravitational fragmentation and the formation of brown dwarfs." <em>MNRAS</em>, 389, 1556–1562.</li>
  </ol>
</details>
