# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the documentation site for Stenox, a macOS voice dictation app with AI enhancement. The docs are built with Mintlify.

## Development Commands

```bash
# Install Mintlify CLI globally
npm i -g mint

# Run local development server (from repo root where docs.json is located)
mint dev

# Preview at http://localhost:3000

# Update CLI if dev environment issues occur
mint update
```

## Architecture

- **docs.json**: Main configuration file - defines navigation structure, theme colors, logos, SEO metadata, and site settings
- **/*.mdx**: Documentation pages using MDX format (Markdown with JSX components)
- **snippets/*.mdx**: Reusable MDX components that can be imported into pages

## Key Mintlify Components Used

The docs use these Mintlify components extensively:
- `<Card>`, `<CardGroup>`: Feature cards with icons and links
- `<Tip>`, `<Note>`, `<Warning>`: Callout boxes
- `<Accordion>`, `<AccordionGroup>`: Collapsible sections
- `<Steps>`, `<Step>`: Sequential instructions

## Page Structure

Each MDX page uses frontmatter:
```yaml
---
title: "Page Title"
sidebarTitle: "Sidebar Name"  # Optional, shorter name for nav
description: "SEO description"
"og:title": "Custom OG Title"  # Optional, for custom social sharing
---
```

## Navigation Structure

Navigation is defined in `docs.json` under `navigation.tabs[0].groups`. Supports:
- Simple pages: `"page-name"` (maps to `page-name.mdx`)
- Nested groups: `{ "group": "Group Name", "pages": [...] }` for sub-sections

## Snippets

Reusable components live in `snippets/`. Import them in MDX files with `<Snippet file="filename.mdx" />`.
