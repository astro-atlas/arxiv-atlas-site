import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z.object({
    title: z.string(),
    pageType: z.enum(['concept', 'paper', 'portal', 'daily_summary']).default('concept'),
    status: z.enum(['done', 'stub']).default('done'),
  }),
});

export const collections = { pages };
