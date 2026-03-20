---
title: "Faraday Rotation"
pageType: concept
status: done
---

<h1 class="page-title">Faraday Rotation</h1>
<div class="infobox">
  <h3 class="infobox-title">Faraday Rotation</h3>
  <table>
    <tr>
      <th>Type:</th>
      <td>Physical mechanism</td>
    </tr>
    <tr>
      <th>Level:</th>
      <td>Undergraduate / Intermediate</td>
    </tr>
    <tr>
      <th>First described:</th>
      <td>1845 (Michael Faraday)</td>
    </tr>
    <tr>
      <th>Key formalism:</th>
      <td>Burn (1966)</td>
    </tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/bondi-accretion" class="wikilink">Bondi accretion</a><br />
        <a href="/pages/parsec-scale-agn-jets" class="wikilink">Parsec-scale AGN jets</a><br />
        <a href="/pages/riaf-adaf-models" class="wikilink">RIAF/ADAF models</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>Faraday rotation</strong> is the rotation of the plane of <a href="/pages/polarimetry" class="wikilink">polarization</a> of linearly polarized electromagnetic radiation as it passes through a magnetized plasma. The amount of rotation depends on the line-of-sight component of the <a href="/pages/magnetic-field" class="wikilink">magnetic field</a>, the electron density, and the wavelength squared. In astrophysics, Faraday rotation is a primary diagnostic for magnetic fields in ionized gas — from the <a href="/pages/interstellar-medium" class="wikilink">interstellar medium</a> to AGN environments <a href="#ref1">[1]</a><a href="#ref2">[2]</a>.
</p>
<h2 id="physics">The &lambda;<sup>2</sup> Law</h2>
<p>
  The electric vector position angle (EVPA, &chi;) of linearly polarized radiation rotates as:
</p>
<p>
  &chi;(&lambda;) = &chi;<sub>0</sub> + RM &middot; &lambda;<sup>2</sup>
</p>
<p>
  where &chi;<sub>0</sub> is the intrinsic EVPA at the source, &lambda; is the observing wavelength, and <strong>RM</strong> (rotation measure) is defined as <a href="#ref1">[1]</a>:
</p>
<p>
  RM = 0.812 &int; n<sub>e</sub> <strong>B</strong>&middot;d<strong>l</strong> &nbsp; [rad m<sup>&minus;2</sup>]
</p>
<p>
  where n<sub>e</sub> is the electron density (cm<sup>&minus;3</sup>), <strong>B</strong> is the magnetic field (&mu;G), and the integral runs along the line of sight (pc). RM is thus a direct probe of the magnetized plasma column between source and observer <a href="#ref1">[1]</a><a href="#ref2">[2]</a>.
</p>
<h2 id="external-vs-internal">External vs. Internal Faraday Rotation</h2>
<p>
  A crucial distinction exists between <strong>external</strong> and <strong>internal</strong> Faraday rotation <a href="#ref1">[1]</a><a href="#ref3">[3]</a>:
</p>
<ul>
  <li><strong>External (foreground screen):</strong> The Faraday-rotating medium is separate from the emitting source. The EVPA follows a pure &lambda;<sup>2</sup> law with no depolarization from rotation alone. Large EVPA rotations (&gt;45°) with good &lambda;<sup>2</sup> fit are diagnostic of external rotation <a href="#ref1">[1]</a><a href="#ref4">[4]</a>.</li>
  <li><strong>Internal (co-spatial with emission):</strong> Emission and rotation occur in the same volume. Different depths contribute different rotations, causing depolarization and deviation from the &lambda;<sup>2</sup> law for rotations &gt;~45° <a href="#ref3">[3]</a><a href="#ref5">[5]</a>. This has been observed in Sgr A* <a href="#ref6">[6]</a> and M87 <a href="#ref7">[7]</a>.</li>
</ul>
<p>
  Park et al. (2026) confirmed external Faraday rotation in <a href="/pages/3c84-ngc1275-jet" class="wikilink">3C 84</a> by detecting EVPA rotations &gt;150° between 86 and 141 GHz with excellent &lambda;<sup>2</sup> fit <a href="#ref4">[4]</a>.
</p>
<h2 id="depolarization">Faraday Depolarization</h2>
<p>
  Even with an external Faraday screen, polarized emission can be suppressed through several mechanisms <a href="#ref1">[1]</a>:
</p>
<ul>
  <li><strong>Bandwidth depolarization:</strong> If RM is large enough that &chi; rotates significantly across the observing bandwidth, the averaged polarization is reduced <a href="#ref1">[1]</a>.</li>
  <li><strong>Beam depolarization:</strong> If RM varies across the telescope beam, different regions rotate by different amounts, reducing the net polarization <a href="#ref1">[1]</a><a href="#ref8">[8]</a>.</li>
  <li><strong>Differential Faraday rotation:</strong> In internal screens, emission from different depths rotates by different amounts, canceling out at long wavelengths <a href="#ref1">[1]</a><a href="#ref3">[3]</a>.</li>
</ul>
<h2 id="agn">RM as a Probe of AGN Environments</h2>
<p>
  In AGN, RM measurements at different distances from the central engine probe different layers of the circumnuclear environment <a href="#ref4">[4]</a><a href="#ref9">[9]</a>:
</p>
<ul>
  <li><strong>M87:</strong> RM &prop; r<sup>&minus;1</sup>, interpreted as a <a href="/pages/riaf-adaf-models" class="wikilink">RIAF</a> Faraday screen <a href="#ref9">[9]</a><a href="#ref10">[10]</a></li>
  <li><strong>Sgr A*:</strong> RM ~ &minus;5&times;10<sup>5</sup> rad/m<sup>2</sup>, consistent with hot accretion flow <a href="#ref11">[11]</a><a href="#ref12">[12]</a></li>
  <li><strong>3C 84:</strong> RM &prop; r<sup>&minus;2.7</sup>, explained by the circumnuclear ambient medium within the <a href="/pages/bondi-accretion" class="wikilink">Bondi radius</a> <a href="#ref4">[4]</a></li>
</ul>
<p>
  Transverse RM gradients across jets have been interpreted as evidence for helical magnetic fields <a href="#ref13">[13]</a><a href="#ref14">[14]</a>, though the jet boundary layer origin is debated <a href="#ref15">[15]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/2603-16796" class="wikilink">Park et al. (2026)</a> — First spatially resolved RM profile in 3C 84</li>
  <li><a href="/pages/bondi-accretion" class="wikilink">Bondi Accretion</a> — Accretion model constraining circumnuclear density</li>
  <li><a href="/pages/riaf-adaf-models" class="wikilink">RIAF/ADAF Models</a> — Hot accretion flow as alternative Faraday screen</li>
  <li><a href="/pages/3c84-ngc1275-jet" class="wikilink">3C 84 / NGC 1275</a> — Source overview</li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Burn, B. J. (1966). "On the depolarization of discrete radio sources by Faraday dispersion." <em>MNRAS</em>, 133, 67. <a href="https://doi.org/10.1093/mnras/133.1.67">DOI</a></li>
    <li id="ref2">Rybicki, G. B. &amp; Lightman, A. P. (1979). <em>Radiative Processes in Astrophysics.</em> Wiley.</li>
    <li id="ref3">Cioffi, D. F. &amp; Jones, T. W. (1980). "Internal Faraday rotation effects." <em>AJ</em>, 85, 368. <a href="https://doi.org/10.1086/112685">DOI</a></li>
    <li id="ref4">Park, J. et al. (2026). "Faraday Rotation Measure of 3C 84." <a href="https://arxiv.org/abs/2603.16796">arXiv:2603.16796</a></li>
    <li id="ref5">Sokoloff, D. D. et al. (1998). "Depolarization and RM dispersion formalism."</li>
    <li id="ref6">Wielgus, M. et al. (2024). "Internal Faraday screen of Sgr A*." <em>A&amp;A</em>, 682, A97. <a href="https://doi.org/10.1051/0004-6361/202347772">DOI</a></li>
    <li id="ref7">Pasetto, A. et al. (2021). "EVPA deviation from &lambda;<sup>2</sup> in M87."</li>
    <li id="ref8">Sokoloff, D. D. et al. (1998). "RM dispersion and beam depolarization."</li>
    <li id="ref9">Park, J. et al. (2019). "Faraday rotation in M87 jet." <em>ApJ</em>, 871, 257. <a href="https://doi.org/10.3847/1538-4357/aaf9a9">DOI</a></li>
    <li id="ref10">Yuan, F. et al. (2022). "M87 RM modeled with RIAF."</li>
    <li id="ref11">Bower, G. C. et al. (2003). "Sgr A* RM detection."</li>
    <li id="ref12">Marrone, D. P. et al. (2006). "Sgr A* RM from SMA."</li>
    <li id="ref13">Asada, K. et al. (2002). "Transverse RM gradient in 3C 273."</li>
    <li id="ref14">Gabuzda, D. C. et al. (2004). "Transverse RM gradients in blazar jets."</li>
    <li id="ref15">Kim, J.-Y. et al. (2019). "Jet boundary layer model for 3C 84." <em>A&amp;A</em>, 622, A196. <a href="https://doi.org/10.1051/0004-6361/201832920">DOI</a></li>
  </ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  Polarization &middot; Magnetic Fields &middot; Radio Astronomy &middot; VLBI &middot; AGN &middot; Plasma Physics
</div>
