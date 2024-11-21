import { defineConfig } from "@voxel51/fiftyone-js-plugin-build";
import { dirname } from "path";
import { fileURLToPath } from "url";

const thirdPartyDependencies = [/^@mui.*/]
// const thirdPartyDependencies = [
//   "@mui/x-tree-view/SimpleTreeView", 
//   "@mui/x-tree-view/TreeItem",
//   "@mui/material/styles",
//   "@mui/material/Collapse",
//   "@mui/material/Checkbox",
//   "@mui/material/utils",
// ]
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const dir = __dirname;

/**
 * List any third-party dependencies that should be bundled into the plugin.
 * You can either use regex or package names.
 */
const myThirdPartyDependencies = ["lodash"];

export default defineConfig(dir, {
  buildConfigOverride: { sourcemap: true },
  forceBundleDependencies: thirdPartyDependencies,
});