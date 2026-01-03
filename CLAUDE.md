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

- **docs.json**: Main configuration file - defines navigation structure, theme colors, logos, and site settings
- **/*.mdx**: Documentation pages using MDX format (Markdown with JSX components)
- Content organized into groups: Getting Started, Core Features, Profiles, Transcription Providers, AI Enhancement Providers, Guides

## Key Mintlify Components Used

The docs use these Mintlify components extensively:
- `<Card>`, `<CardGroup>`: Feature cards with icons and links
- `<Tip>`, `<Note>`, `<Warning>`: Callout boxes
- `<Accordion>`, `<AccordionGroup>`: Collapsible sections
- `<Steps>`, `<Step>`: Sequential instructions
- Frontmatter with `title` and `description` fields

## Navigation Structure

Navigation is defined in `docs.json` under `navigation.tabs[0].groups`. Each group has a `group` name and `pages` array. Page references are paths without the `.mdx` extension.
