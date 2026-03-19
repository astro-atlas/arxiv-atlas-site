---
title: "Minimum Spanning Tree"
pageType: concept
status: done
---

<h1 class="page-title">Minimum Spanning Tree</h1>
<div class="infobox">
  <h3 class="infobox-title">Minimum Spanning Tree (MST)</h3>
  <table>
    <tr><th>Type:</th><td>Intermediate concept / statistical technique</td></tr>
    <tr><th>Used in:</th><td>Cluster fractality diagnostics, graph theory</td></tr>
    <tr><th>Related:</th>
      <td>
        <a href="/pages/q-parameter-fractality" class="wikilink">Q parameter (fractality)</a><br />
        <a href="/pages/fractal-structure-star-clusters" class="wikilink">Fractal structure of star clusters</a>
      </td>
    </tr>
  </table>
</div>
<p>
  A <strong>minimum spanning tree (MST)</strong> is a graph-theoretic construct: given a set of points (e.g., stellar positions), it is the tree (acyclic connected graph) that connects all points with the minimum total edge length. In astrophysics, the MST is widely used to characterize the spatial distribution of stars in clusters and to compute the <a href="/pages/q-parameter-fractality" class="wikilink">Q parameter</a> as a measure of cluster fractality.<sup><a href="#ref1">1</a></sup>
</p>
<h2 id="construction">Construction and Normalization</h2>
<p>
  The MST is constructed from the Euclidean distances between all pairs of stars. For cluster analysis, the mean edge length m is normalized by the cluster size r<sub>cl</sub>:
</p>
<ul>
  <li><strong>2D normalization:</strong> m̄ = m / (r<sub>cl</sub><sup>2</sup> N<sub>s</sub>)<sup>1/2</sup></li>
  <li><strong>3D normalization:</strong> m̄ = m / (4/3 π r<sub>cl</sub><sup>3</sup> N<sub>s</sub>)<sup>1/3</sup></li>
</ul>
<p>
  The normalized mean interparticle separation s̄ is analogously defined. The ratio m̄/s̄ gives the Q parameter.<sup><a href="#ref2">2</a></sup>
</p>
<h2 id="physical-intuition">Physical Intuition</h2>
<p>
  In a fractal, substructured distribution, stars form tight local groups — MST edges within groups are short, but gaps between groups are large, making m̄ ≪ s̄ and Q ≪ 1. In a smooth, centrally concentrated distribution, stars are more uniformly spaced — m̄ and s̄ are comparable and Q is larger. The MST is therefore a compact proxy for the degree of substructure in the system.
</p>
<h2 id="applications">Applications in Star Cluster Studies</h2>
<p>
  The MST-based Q parameter has been applied to:
</p>
<ul>
  <li>Observations of young stellar clusters in the Milky Way and LMC<sup><a href="#ref3">3</a></sup><sup><a href="#ref4">4</a></sup></li>
  <li>Simulations of star cluster formation (SPH, AMR, MHD+N-body)<sup><a href="#ref5">5</a></sup><sup><a href="#ref6">6</a></sup><sup><a href="#ref7">7</a></sup></li>
  <li>Tracking structural evolution during cluster assembly and gas expulsion</li>
</ul>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/q-parameter-fractality" class="wikilink">Q parameter (fractality)</a></li>
  <li><a href="/pages/fractal-structure-star-clusters" class="wikilink">Fractal structure of star clusters</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Cartwright, A. &amp; Whitworth, A. P. (2004). "The statistical analysis of star clusters." <em>MNRAS</em>, 348, 589–598.</li>
    <li id="ref2">Cartwright, A. (2009). "Measuring clustering in 2dv space." <em>MNRAS</em>, 400, 1427–1430.</li>
    <li id="ref3">Bastian, N. et al. (2009). "The spatial evolution of stellar structures in the LMC." <em>MNRAS</em>, 392, 868–878.</li>
    <li id="ref4">Kuhn, M. A. et al. (2014). "The spatial structure of young stellar clusters. I. Subclusters." <em>ApJ</em>, 787, 107.</li>
    <li id="ref5">Schmeja, S. &amp; Klessen, R. S. (2006). "Evolving structures of star-forming clusters." <em>A&amp;A</em>, 449, 151–159.</li>
    <li id="ref6">Maschberger, Th. et al. (2010). "Properties of hierarchically forming star clusters." <em>MNRAS</em>, 404, 1061–1080.</li>
    <li id="ref7">Akhmetali, A. et al. (2026). "Evolution of fractality in centrally concentrated young clusters." <em>A&amp;A</em> (submitted). <a href="https://arxiv.org/abs/2603.16183">arXiv:2603.16183</a></li>
  </ol>
</details>
