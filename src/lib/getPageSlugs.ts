// Workaround: move glob reading out of Base.astro to avoid Astro compiler bug
export function getExistingSlugs(): string[] {
  const pageFiles = import.meta.glob('../pages/pages/*.astro');
  return Object.keys(pageFiles)
    .map(p => p.split('/').pop()!.replace('.astro', ''))
    .filter(s => !s.startsWith('_'));
}
