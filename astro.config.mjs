import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";

export default defineConfig({
  site: "http://localhost:8080",
  outDir: "./dist",
  integrations: [mdx()],
});
