---
title: "Q Parameter (Fractality)"
pageType: concept
status: done
---

<h1 class="page-title">Q Parameter (Fractality)</h1>
<div class="infobox">
  <h3 class="infobox-title">Q Parameter</h3>
  <table>
    <tr><th>Type:</th><td>Intermediate concept / statistical diagnostic</td></tr>
    <tr><th>Introduced by:</th><td>Cartwright &amp; Whitworth (2004)<sup><a href="#ref1">1</a></sup></td></tr>
    <tr><th>Threshold:</th><td>Q &lt; 0.8 (2D) or &lt; 0.7 (3D) → fractal; Q &gt; threshold → centrally concentrated</td></tr>
    <tr><th>Related:</th>
      <td>
        <a href="/pages/fractal-structure-star-clusters" class="wikilink">Fractal structure of star clusters</a><br />
        <a href="/pages/star-cluster-formation" class="wikilink">Star cluster formation</a><br />
        <a href="/pages/dynamical-relaxation-clusters" class="wikilink">Dynamical relaxation</a><br />
        <a href="/pages/minimum-spanning-tree" class="wikilink">Minimum spanning tree</a>
      </td>
    </tr>
  </table>
</div>
<p>
  The <strong>Q parameter</strong> is a dimensionless statistic that quantifies whether a stellar cluster has a hierarchically substructured (fractal) or centrally concentrated, smooth spatial distribution. It is the most widely used diagnostic for <a href="/pages/fractal-structure-star-clusters" class="wikilink">fractal structure in star clusters</a> in both observations and simulations.<sup><a href="#ref1">1</a></sup>
</p>
<h2 id="definition">Definition</h2>
<p>
  Q is defined as:
</p>
<blockquote>
  Q = m̄ / s̄
</blockquote>
<p>
  where m̄ is the normalized mean edge length of the <a href="/pages/minimum-spanning-tree" class="wikilink">minimum spanning tree</a> (MST) connecting all stars, and s̄ is the normalized mean interparticle separation.<sup><a href="#ref1">1</a></sup> Both quantities are normalized by the cluster size r<sub>cl</sub> (radius enclosing 95% of the cluster mass). The normalization for m̄ in 2D is (r<sub>cl</sub><sup>2</sup> N<sub>s</sub>)<sup>1/2</sup>; in 3D it is (4/3 π r<sub>cl</sub><sup>3</sup> N<sub>s</sub>)<sup>1/3</sup>.<sup><a href="#ref2">2</a></sup>
</p>
<h2 id="interpretation">Interpretation</h2>
<ul>
  <li><strong>Q ≪ 1</strong>: Highly substructured (fractal) distribution — points form tight isolated groups with small m̄ separated by large s̄.</li>
  <li><strong>Q &lt; 0.8 (2D) / Q &lt; 0.7 (3D)</strong>: Fractal substructure present.</li>
  <li><strong>Q ≈ threshold</strong>: Approximately uniform density profile.</li>
  <li><strong>Q &gt; threshold</strong>: Centrally concentrated, radially smooth cluster.</li>
  <li><strong>Q ~ 1.2</strong>: Strongly centrally concentrated cluster (seen in high-resolution simulations at late times<sup><a href="#ref3">3</a></sup>).</li>
</ul>
<h2 id="s-m-plots">s̄–m̄ Diagnostic Plots</h2>
<p>
  Plotting s̄ vs. m̄ provides an even more sensitive diagnostic than Q alone: the location in s̄–m̄ space distinguishes fractal distributions (with different fractal dimensions f<sub>dim</sub> ~ 1.6, 2.0) from radial density profiles (with different power-law slopes α).<sup><a href="#ref2">2</a></sup>
</p>
<h2 id="evolution">Temporal Evolution</h2>
<p>
  Young clusters typically start with Q below the fractal threshold, reflecting inherited structure from the parent <a href="/pages/molecular-cloud" class="wikilink">molecular cloud</a><sup><a href="#ref4">4</a></sup>. As dynamical relaxation proceeds, Q rises. Key empirical findings:
</p>
<ul>
  <li>Q exceeds the fractal threshold at ~2.5 t<sub>ff</sub> in most simulations of centrally concentrated clouds<sup><a href="#ref3">3</a></sup><sup><a href="#ref5">5</a></sup>.</li>
  <li>Q fluctuates when subclusters merge and re-fragment — sensitive to dynamical subcluster interactions<sup><a href="#ref3">3</a></sup>.</li>
  <li>Some young observed clusters (e.g., ρ Ophiuchus) show centrally concentrated Q at ~1 Myr; others (NGC 1513, NGC 1641) retain substructure beyond 100 Myr<sup><a href="#ref6">6</a></sup>.</li>
</ul>
<h2 id="correlation-with-fdim">Correlation with Fractal Dimension</h2>
<p>
  Q is a binary fractal indicator (fractal vs. not), while the <a href="/pages/fractal-structure-star-clusters" class="wikilink">fractal dimension</a> quantifies the degree of fractality. The correlation between Q and fractal dimension in physical simulations is weak-to-moderate (Spearman ρ): Q correlates more strongly with the correlation dimension (sensitive to local clustering) than with the box-counting dimension (global measure).<sup><a href="#ref3">3</a></sup> This contrasts with stronger correlations found in artificially constructed fractal clusters.<sup><a href="#ref6">6</a></sup>
</p>
<h2 id="see-also">See Also</h2>
<ul>
  <li><a href="/pages/fractal-structure-star-clusters" class="wikilink">Fractal structure of star clusters</a></li>
  <li><a href="/pages/minimum-spanning-tree" class="wikilink">Minimum spanning tree</a></li>
  <li><a href="/pages/star-cluster-formation" class="wikilink">Star cluster formation</a></li>
  <li><a href="/pages/dynamical-relaxation-clusters" class="wikilink">Dynamical relaxation in clusters</a></li>
</ul>
<details class="references"><summary><h2>References</h2></summary>
  <ol>
    <li id="ref1">Cartwright, A. &amp; Whitworth, A. P. (2004). "The statistical analysis of star clusters." <em>MNRAS</em>, 348, 589–598.</li>
    <li id="ref2">Cartwright, A. (2009). "Measuring clustering in 2dv space." <em>MNRAS</em>, 400, 1427–1430.</li>
    <li id="ref3">Akhmetali, A. et al. (2026). "Evolution of fractality in centrally concentrated young clusters." <em>A&amp;A</em> (submitted). <a href="https://arxiv.org/abs/2603.16183">arXiv:2603.16183</a></li>
    <li id="ref4">Schmeja, S. &amp; Klessen, R. S. (2006). "Evolving structures of star-forming clusters." <em>A&amp;A</em>, 449, 151–159.</li>
    <li id="ref5">Laverde-Villarreal, E. et al. (2025). "The Evolution of Substructure during Star Cluster Assembly." <em>ApJ</em>, 989, 22.</li>
    <li id="ref6">Sánchez, N. &amp; Alfaro, E. J. (2009). "The spatial distribution of stars in open clusters." <em>ApJ</em>, 696, 2086.</li>
    <li id="ref7">Bastian, N. et al. (2009). "The spatial evolution of stellar structures in the LMC." <em>MNRAS</em>, 392, 868–878.</li>
    <li id="ref8">Parker, R. J. &amp; Meyer, M. R. (2012). "Characterizing the dynamical state of star clusters from snapshots." <em>MNRAS</em>, 427, 637–650.</li>
  </ol>
</details>
