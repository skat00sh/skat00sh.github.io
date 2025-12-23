# Devendra Vyas - Personal Website

A Hugo-based personal website and blog using the PaperMod theme.

## Prerequisites

- **Hugo Extended** (version 0.92.2 or later recommended)
  - Check if installed: `hugo version`
  - Install from: https://gohugo.io/installation/

## Local Development

### Quick Start

1. **Start the development server:**
   ```bash
   hugo server
   ```

2. **View your site:**
   - Open your browser to: `http://localhost:1313`
   - The site will auto-reload when you make changes

### Development Server Options

**Basic server:**
```bash
hugo server
```

**With draft posts visible:**
```bash
hugo server -D
```

**With future-dated posts visible:**
```bash
hugo server -F
```

**Custom port:**
```bash
hugo server -p 8080
```

**Bind to all network interfaces (accessible from other devices):**
```bash
hugo server --bind 0.0.0.0
```

### Build for Production

To build the static site:

```bash
hugo --minify
```

The output will be in the `public/` directory.

### Update Hugo Theme

If you need to update the PaperMod theme:

```bash
git submodule update --remote --merge
```

## Project Structure

- `content/` - Your content (posts, pages)
- `config.yaml` - Site configuration
- `themes/PaperMod/` - PaperMod theme (git submodule)
- `static/` - Static files (images, etc.)
- `public/` - Generated site (created when you build)

## Notes

- The site uses Hugo Extended for SCSS processing
- GitHub Actions automatically builds and deploys on push to `master` branch
- Local development uses `http://localhost:1313` (baseURL is automatically adjusted)

