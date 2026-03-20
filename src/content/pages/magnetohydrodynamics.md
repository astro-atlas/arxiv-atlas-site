---
title: "Magnetohydrodynamics (MHD)"
pageType: concept
status: done
---

<h1 class="page-title">Magnetohydrodynamics (MHD)</h1>
<div class="infobox">
  <h3 class="infobox-title">Magnetohydrodynamics</h3>
  <table>
    <tr><th>Type:</th><td>Foundational concept</td></tr>
    <tr><th>Field:</th><td>Theoretical astrophysics, computational astrophysics</td></tr>
    <tr><th>Related:</th>
      <td>
        <a href="/pages/magnetic-field" class="wikilink">Magnetic field</a><br />
        <a href="/pages/magnetic-fields-in-star-formation" class="wikilink">Magnetic fields in star formation</a><br />
        <a href="/pages/turbulence" class="wikilink">Turbulence</a><br />
        <a href="/pages/star-formation" class="wikilink">Star formation</a><br />
        <a href="/pages/molecular-cloud" class="wikilink">Molecular cloud</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Magnetohydrodynamics (MHD)</strong> is the study of the dynamics of electrically conducting fluids in the presence of magnetic fields. In astrophysics, MHD governs the behavior of ionized and partially ionized gas in environments ranging from stellar interiors to the <a href="/pages/interstellar-medium" class="wikilink">interstellar medium</a>, molecular clouds, and accretion disks. The coupling between the gas and the magnetic field creates a rich variety of wave modes, instabilities, and force-balance regimes that profoundly influence <a href="/pages/star-formation" class="wikilink">star formation</a> and stellar cluster assembly.
</p>
<h2 id="equations">MHD Equations</h2>
<p>
  Ideal MHD combines the Euler equations of fluid dynamics with Maxwell's equations under the assumption of infinite conductivity (frozen-in field):
</p>
<ul>
  <li><strong>Mass continuity:</strong> ∂ρ/∂t + ∇·(ρ<strong>v</strong>) = 0</li>
  <li><strong>Momentum:</strong> ρ D<strong>v</strong>/Dt = −∇P + (1/4π)(∇×<strong>B</strong>)×<strong>B</strong> + ρ<strong>g</strong></li>
  <li><strong>Induction:</strong> ∂<strong>B</strong>/∂t = ∇×(<strong>v</strong>×<strong>B</strong>)</li>
  <li><strong>∇·B = 0</strong> (no magnetic monopoles)</li>
</ul>
<h2 id="astrophysical-applications">Astrophysical Applications</h2>
<p>
  MHD is central to understanding:
</p>
<ul>
  <li><strong>Molecular cloud support:</strong> Magnetic pressure and tension resist gravitational collapse; the <a href="/pages/mass-to-flux-ratio" class="wikilink">mass-to-flux ratio</a> determines whether a cloud is magnetically sub- or supercritical.</li>
  <li><strong>Star formation regulation:</strong> Magnetic fields slow collapse, shape filamentary structure, and support turbulent energy transfer.<sup><a href="#ref1">1</a></sup><sup><a href="#ref2">2</a></sup></li>
  <li><strong>Jet and outflow launching:</strong> MHD processes drive collimated outflows and jets from protostars and AGN (see <a href="/pages/agn-feedback" class="wikilink">AGN feedback</a>).</li>
  <li><strong>Cluster formation simulations:</strong> MHD simulation codes such as FLASH<sup><a href="#ref3">3</a></sup> are used in the Torch framework to model star cluster formation from first principles.<sup><a href="#ref4">4</a></sup></li>
</ul>
<h2 id="numerical-mhd">Numerical MHD</h2>
<p>
  Solving the MHD equations numerically requires careful treatment of discontinuities (shocks) and the ∇·B = 0 constraint. Key approaches include:
</p>
<ul>
  <li><strong>FLASH code:</strong> Adaptive mesh refinement (AMR) Eulerian MHD, used in the Torch framework for star cluster formation simulations.<sup><a href="#ref3">3</a></sup><sup><a href="#ref5">5</a></sup></li>
  <li><strong>Constrained transport (CT):</strong> Exactly preserves ∇·B = 0 on the grid.</li>
  <li><strong>SPH:</strong> Lagrangian approach used in earlier cluster formation work (Bonnell et al. 2003<sup><a href="#ref6">6</a></sup>).</li>
</ul>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/magnetic-field" class="wikilink">Magnetic field</a></li>
  <li><a href="/pages/magnetic-fields-in-star-formation" class="wikilink">Magnetic fields in star formation</a></li>
  <li><a href="/pages/mass-to-flux-ratio" class="wikilink">Mass-to-flux ratio</a></li>
  <li><a href="/pages/turbulence" class="wikilink">Turbulence</a></li>
  <li><a href="/pages/star-formation" class="wikilink">Star formation</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Mac Low, M.-M. &amp; Klessen, R. S. (2004). "Control of star formation by supersonic turbulence." <em>Rev. Mod. Phys.</em>, 76, 125.</li>
    <li id="ref2">McKee, C. F. &amp; Ostriker, E. C. (2007). "Theory of star formation." <em>ARA&amp;A</em>, 45, 565–687.</li>
    <li id="ref3">Fryxell, B. et al. (2000). "FLASH: An Adaptive Mesh Hydrodynamics Code." <em>ApJS</em>, 131, 273.</li>
    <li id="ref4">Wall, J. E. et al. (2019). "Collisional N-body dynamics coupled to self-gravitating MHD." <em>ApJ</em>, 887, 62.</li>
    <li id="ref5">Dubey, A. et al. (2014). "Evolution of FLASH, a multi-physics scientific simulation code." <em>Int. J. High Perf. Comput. Appl.</em>, 28, 225–237.</li>
    <li id="ref6">Bonnell, I. A. et al. (2003). "The hierarchical formation of a stellar cluster." <em>MNRAS</em>, 343, 413–418.</li>
    <li id="ref7">Akhmetali, A. et al. (2026). "Evolution of fractality in centrally concentrated young clusters." <em>A&amp;A</em> (submitted). <a href="https://arxiv.org/abs/2603.16183">arXiv:2603.16183</a></li>
  </ol>
</details>
