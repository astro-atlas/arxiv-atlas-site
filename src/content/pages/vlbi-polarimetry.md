---
title: "VLBI Polarimetry"
pageType: concept
status: done
---

<h1 class="page-title">VLBI Polarimetry</h1>
<div class="infobox">
  <h3 class="infobox-title">VLBI <a href="/pages/polarimetry" class="wikilink">polarimetry</a></h3>
  <table>
    <tr>
      <th>Type:</th>
      <td>Observational technique</td>
    </tr>
    <tr>
      <th>Level:</th>
      <td>Specialist</td>
    </tr>
    <tr>
      <th>Key instruments:</th>
      <td>VLBA, KVN, HSA, EHT, EVN</td>
    </tr>
    <tr>
      <th>Key software:</th>
      <td>GPCAL, PolConvert, AIPS, Difmap</td>
    </tr>
    <tr>
      <th>Related:</th>
      <td>
        <a href="/pages/faraday-rotation" class="wikilink">Faraday rotation</a><br />
        <a href="/pages/3c84-ngc1275-jet" class="wikilink">3C 84 / NGC 1275 jet</a><br />
        <a href="/pages/2603-16796" class="wikilink">Park et al. (2026)</a>
      </td>
    </tr>
  </table>
</div>
<p>
  <strong>VLBI polarimetry</strong> is the measurement of polarized radio emission at milliarcsecond resolution using very long baseline interferometry. It enables spatially resolved mapping of <a href="/pages/magnetic-field" class="wikilink">magnetic field</a> structures in AGN jets and their environments through Stokes I, Q, U (and sometimes V) imaging, yielding electric vector position angle (EVPA) and <a href="/pages/faraday-rotation" class="wikilink">rotation measure</a> (RM) maps <a href="#ref1">[1]</a><a href="#ref2">[2]</a>. The technique demands careful calibration of instrumental polarization (D-terms) and absolute EVPA, making it one of the most technically challenging areas of radio astronomy.
</p>
<h2 id="d-terms">D-Term Calibration</h2>
<p>
  Instrumental polarization leakage (D-terms) arises from imperfect isolation between orthogonal polarization feeds. If uncorrected, D-terms create spurious polarized signal — particularly dangerous for weakly polarized sources like <a href="/pages/3c84-ngc1275-jet" class="wikilink">3C 84</a>, where the core polarization is below 1% <a href="#ref3">[3]</a><a href="#ref4">[4]</a>.
</p>
<p>
  Traditional D-term calibration in AIPS (LPCAL) uses a single calibrator and assumes the source structure is similar between polarizations <a href="#ref5">[5]</a>. The <strong>GPCAL</strong> pipeline developed by Park et al. (2021) significantly improves accuracy by using multiple calibrators simultaneously and eliminating the "similarity approximation" <a href="#ref6">[6]</a>. GPCAL has been extended to handle frequency-dependent <a href="#ref7">[7]</a> and time-dependent <a href="#ref8">[8]</a> D-term variations, which is critical for wide-bandwidth and long-track observations.
</p>
<p>
  In the Park et al. (2026) study of 3C 84, GPCAL calibration was essential: because the core of 3C 84 is effectively unpolarized at KVN frequencies, any apparent core polarization is a direct indicator of residual D-term contamination <a href="#ref4">[4]</a><a href="#ref3">[3]</a>. The authors demonstrated that weak polarization features near bright unpolarized cores in VLBA images are instrumental artifacts, not real detections — a cautionary result for the field <a href="#ref4">[4]</a>.
</p>
<h2 id="evpa">EVPA Calibration</h2>
<p>
  The absolute EVPA orientation requires external calibration because VLBI arrays lack short baselines that would recover total-power polarization information. Standard practice uses comparison with quasi-simultaneous single-dish or connected-interferometer observations of calibrator sources <a href="#ref1">[1]</a>.
</p>
<p>
  For KVN data, single-dish EVPA calibration is performed using known calibrator EVPAs measured at the same frequencies <a href="#ref9">[9]</a><a href="#ref10">[10]</a>. For VLBA data, Park et al. (2026) cross-checked EVPA calibration by comparing multiple calibrator sources across epochs, identifying and correcting systematic offsets of up to 10&ndash;20&deg; in archival BU-BLAZAR data <a href="#ref4">[4]</a><a href="#ref11">[11]</a>. This correction was critical for obtaining accurate RM values.
</p>
<p>
  EVPA uncertainty is typically estimated as &sigma;<sub>EVPA</sub> = 0.5 &times; arctan(&sigma;<sub>D</sub> / m), where &sigma;<sub>D</sub> is the D-term uncertainty (~5% for VLBA) and m is the fractional polarization <a href="#ref12">[12]</a>.
</p>
<h2 id="fpt">Frequency Phase Transfer</h2>
<p>
  At high frequencies (&gt;43 GHz), atmospheric phase fluctuations degrade VLBI coherence. The <strong>frequency phase transfer</strong> (FPT) technique calibrates tropospheric phase at a low frequency and scales the solution to high frequencies, enabling coherent detection at 86&ndash;141 GHz <a href="#ref13">[13]</a><a href="#ref14">[14]</a>.
</p>
<p>
  The Korean VLBI Network (KVN) is uniquely suited for FPT because it observes at four frequencies simultaneously (22, 43, 86, 129 GHz) with a shared signal path <a href="#ref13">[13]</a>. This simultaneous multi-frequency capability is essential for measuring large RMs (|RM| &gt; 10<sup>5</sup> rad/m<sup>2</sup>) in sources like 3C 84, where the EVPA rotates by many radians between adjacent frequency bands <a href="#ref4">[4]</a>. The upgraded 16-Gbps OCTAD recording system (post-2022) enables simultaneous 4-band observations with finer frequency sampling, greatly improving RM measurement reliability and resolving n&pi; ambiguities <a href="#ref4">[4]</a>.
</p>
<h2 id="polconvert">PolConvert</h2>
<p>
  Heterogeneous VLBI arrays often mix antennas with circular feeds (e.g., VLBA) and linear feeds (e.g., Effelsberg, ALMA). <strong>PolConvert</strong> is a software tool that converts linear-feed visibilities to a circular basis, enabling joint calibration and imaging with circular-feed stations <a href="#ref15">[15]</a>.
</p>
<p>
  In the Park et al. (2026) HSA 8 GHz observations, PolConvert was used to incorporate Effelsberg (linear feeds) into the otherwise circular-feed VLBA+VLA array, providing critical additional sensitivity for detecting the weak polarization at the southern lobe of 3C 84 <a href="#ref4">[4]</a><a href="#ref15">[15]</a>.
</p>
<h2 id="rm-measurement">RM Measurement Strategies</h2>
<p>
  Accurate RM determination requires multi-frequency EVPA measurements and careful handling of the n&pi; ambiguity — the degeneracy arising because EVPA is defined modulo &pi; <a href="#ref4">[4]</a>. Strategies include:
</p>
<ul>
  <li><strong>Narrow frequency spacing:</strong> Using closely spaced sub-bands (e.g., KVN&rsquo;s 43.0, 44.0, 45.5, 46.5 GHz) constrains n&pi; wraps before extrapolating to wider frequency separations <a href="#ref4">[4]</a>.</li>
  <li><strong>In-band RM:</strong> For very large RM, even the 256 MHz VLBA bandwidth can yield measurable EVPA rotation within a single band <a href="#ref16">[16]</a>.</li>
  <li><strong>Weighted mean RM:</strong> Averaging RM over polarized regions reduces noise while accounting for spatial RM gradients <a href="#ref2">[2]</a>.</li>
</ul>
<p>
  The combination of VLBA (high resolution at 43 GHz), KVN (simultaneous multi-frequency at 43&ndash;141 GHz), and HSA (high sensitivity at 8 GHz) enabled Park et al. (2026) to trace the RM profile of 3C 84 from 1 to 15 pc — spanning over a decade in spatial scale with a single consistent framework <a href="#ref4">[4]</a>.
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/faraday-rotation" class="wikilink">Faraday Rotation</a> — The physics being measured</li>
  <li><a href="/pages/2603-16796" class="wikilink">Park et al. (2026)</a> — Showcase application of VLBI polarimetry to 3C 84</li>
  <li><a href="/pages/2603-16647" class="wikilink">Cho et al. (2026)</a> — Related VLBI polarimetric study</li>
  <li><a href="/pages/3c84-ngc1275-jet" class="wikilink">3C 84 / NGC 1275 Jet</a> — Target source</li>
  <li><a href="/pages/recollimation-shocks" class="wikilink">Recollimation Shocks</a> — Jet structures revealed by polarimetry</li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Hovatta, T. et al. (2012). "MOJAVE: VLBA polarimetry of AGN jets." <em>AJ</em>, 144, 105. <a href="https://doi.org/10.1088/0004-6256/144/4/105">DOI</a></li>
    <li id="ref2">Park, J. et al. (2019). "Faraday rotation in the M87 jet." <em>ApJ</em>, 871, 257. <a href="https://doi.org/10.3847/1538-4357/aaf9a9">DOI</a></li>
    <li id="ref3">Kim, J.-Y. et al. (2019). "VLBI imaging of 3C 84 at 86 GHz: jet boundary layer polarization." <em>A&amp;A</em>, 622, A196. <a href="https://doi.org/10.1051/0004-6361/201832920">DOI</a></li>
    <li id="ref4">Park, J. et al. (2026). "Faraday Rotation Measure of 3C 84 and the Circumnuclear Environment of NGC 1275." <a href="https://arxiv.org/abs/2603.16796">arXiv:2603.16796</a></li>
    <li id="ref5">Greisen, E. W. (2003). "AIPS, the VLA, and the VLBA." <em>Information Handling in Astronomy</em>.</li>
    <li id="ref6">Park, J. et al. (2021). "GPCAL: a generalized calibration pipeline for instrumental polarization in VLBI data." <em>ApJ</em>, 906, 85. <a href="https://doi.org/10.3847/1538-4357/abcc6e">DOI</a></li>
    <li id="ref7">Park, J. et al. (2023). "GPCAL: frequency-dependent D-term calibration."</li>
    <li id="ref8">Park, J. et al. (2023). "GPCAL: time-dependent D-term calibration."</li>
    <li id="ref9">Kang, S. et al. (2015). "KVN single-dish polarimetry."</li>
    <li id="ref10">Kam, M. et al. (2023). "KVN EVPA calibration procedure."</li>
    <li id="ref11">Jorstad, S. G. et al. (2017). "VLBA-BU-BLAZAR program." <em>ApJ</em>, 846, 98. <a href="https://doi.org/10.3847/0004-637X/846/2/98">DOI</a></li>
    <li id="ref12">Hovatta, T. et al. (2012). "EVPA uncertainty formalism." <em>AJ</em>, 144, 105. <a href="https://doi.org/10.1088/0004-6256/144/4/105">DOI</a></li>
    <li id="ref13">Rioja, M. J. &amp; Dodson, R. (2011). "Frequency phase transfer for high-frequency VLBI." <em>AJ</em>, 141, 114. <a href="https://doi.org/10.1088/0004-6256/141/4/114">DOI</a></li>
    <li id="ref14">Algaba, J. C. et al. (2015). "FPT technique applications."</li>
    <li id="ref15">Mart&iacute;-Vidal, I. et al. (2016). "PolConvert: converting mixed-feed VLBI data." <em>A&amp;A</em>, 587, A143. <a href="https://doi.org/10.1051/0004-6361/201526063">DOI</a></li>
    <li id="ref16">Nagai, H. et al. (2017). "In-band RM measurement of 3C 84 with VLBA." <em>ApJ</em>, 849, 52. <a href="https://doi.org/10.3847/1538-4357/aa8e43">DOI</a></li>
  </ol>
</div>
<div class="page-tags">
  <strong>Tags:</strong>
  VLBI &middot; Polarimetry &middot; Radio Astronomy &middot; Calibration &middot; D-terms &middot; EVPA &middot; Instrumentation
</div>
