# CLAUDE.md

## Project
Skyhawk Atlas is an educational, browser-based 3D explorer for Cessna aircraft systems. The current prototype is a self-contained Spanish HTML application using Three.js.

## Working rules
- Preserve the existing working prototype and inspect the current implementation before changing it.
- Keep the app usable offline; Three.js, GLTFLoader, OrbitControls, and the current aircraft reference are bundled locally.
- Prefer small, focused changes. Do not replace the single-file prototype with a new framework or build system unless requested.
- Keep the interface and instructional content in Spanish unless the user asks otherwise.
- Do not invent aircraft configurations, part numbers, locations, or procedures. Mark uncertainty explicitly and cite the source and applicability.
- Treat the included C172P geometry as a visual teaching reference only. It is not a verified C172S or FAC aircraft model. Distinguish geometry, functional teaching traces, and installation verified for a specific aircraft.
- Do not imply certification, flight credit, maintenance approval, or operational suitability. This is ground familiarization material and does not replace the applicable POH/AFM, supplements, checklists, or instructor.
- Retain and review third-party license notices before modifying or redistributing assets. The GLB is GPL-2.0; bundled Three.js code is MIT. Do not remove attribution or license files.
- Verify rights for any manufacturer images or other external content before commercial distribution.

## Architecture
- `index.html` is the current application entry point and contains the UI, styling, data, and application logic.
- `three.min.js`, `GLTFLoader.js`, and `OrbitControls.js` are bundled runtime dependencies.
- `c172-reference.glb` is the C172P-derived FlightGear reference model.
- `c172-reference-manifest.json` records inspected model structure; `c172-model-data.js` contains model mapping data.
- `README.md` documents user workflows, evidence limits, and sources.
- Keep the app dependency-light and avoid adding a package manager unless a concrete need justifies it.

## Before editing
1. Read the relevant sections of README.md and inspect the target code paths in index.html.
2. Identify whether a feature relies on the reference model, an added didactic trace, or aircraft-specific evidence.
3. Preserve existing controls, lessons, accessibility, and offline loading behavior.

## After editing
- Check the changed files for syntax or obvious runtime issues.
- Summarize what changed and any assumptions or unverified aviation details.
- Do not describe the prototype as a validated digital twin of a specific C172S unless aircraft-specific evidence supports that claim.
