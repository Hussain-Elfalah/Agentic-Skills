#!/usr/bin/env node
/**
 * Epic-design HTML layer validator (depth attrs, aria-hidden, reduced-motion, limits).
 */
const fs = require("fs");
const path = require("path");

const file = process.argv[2];
if (!file) {
  console.error("Usage: node validate-layers.js <path/to/index.html>");
  process.exit(1);
}

const html = fs.readFileSync(path.resolve(file), "utf8");
const issues = [];
const warnings = [];

function has(pattern, label, severity = "error") {
  if (!pattern.test(html)) {
    (severity === "error" ? issues : warnings).push(label);
  }
}

has(/prefers-reduced-motion:\s*reduce/i, "Missing prefers-reduced-motion: reduce block");
has(/data-depth\s*=\s*["'][0-5]["']/i, "No data-depth attributes found (expected on layered scenes)", "warn");

const scenes = html.match(/<section[^>]*class="[^"]*scene[^"]*"/gi) || [];
if (scenes.length === 0) {
  warnings.push("No .scene sections found");
}

const depthEls = [...html.matchAll(/data-depth\s*=\s*["'](\d)["']/gi)];
const decorativeWithoutAria = html.match(
  /<div[^>]*data-depth[^>]*aria-hidden\s*=\s*["']true["'][^>]*>/gi
);
const depthDecorative = html.match(/<div[^>]*class="[^"]*layer[^"]*depth-[01][^"]*"[^>]*>/gi) || [];

if (depthEls.length > 0 && (!decorativeWithoutAria || decorativeWithoutAria.length < 1)) {
  warnings.push("Background/atmosphere layers should use aria-hidden=\"true\"");
}

const imgs = [...html.matchAll(/<img\b[^>]*>/gi)];
imgs.forEach((tag, i) => {
  if (!/alt\s*=\s*["'][^"']+["']/i.test(tag[0])) {
    issues.push(`img #${i + 1} missing non-empty alt`);
  }
});

const animated = (html.match(/@keyframes|animation:/gi) || []).length;
if (animated > 80) {
  warnings.push(`High animation count (${animated}); consider reducing for performance`);
}

const willChange = (html.match(/will-change\s*:/gi) || []).length;
if (willChange > 24) {
  warnings.push(`Many will-change declarations (${willChange}); remove after animation completes`);
}

console.log(`\nEpic-design validation: ${path.basename(file)}\n`);
if (issues.length === 0 && warnings.length === 0) {
  console.log("PASS — no issues found.");
  process.exit(0);
}
issues.forEach((m) => console.log("ERROR:", m));
warnings.forEach((m) => console.log("WARN:", m));
process.exit(issues.length > 0 ? 1 : 0);
