# 🍌 NANOBANANA PROMPTS — Imágenes y Animaciones Interactivas

> Prompts optimizados para Nano Banana (Gemini Image Generation)

## ¿Qué es Nano Banana?

Nano Banana es el modelo de generación de imágenes de Google Gemini API. Permite:
- Generar imágenes fotorrealistas desde texto
- Editar imágenes existentes
- Generar variaciones de estilo
- Crear assets para web design

## API Endpoint

```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp-image-generation:generateContent
```

## Prompts para Diseño Web

### Hero Backgrounds

```prompt
Generate a premium dark cinematic hero background for a [INDUSTRY] website.
Deep black (#0a0a0b) base with subtle mesh gradient in [COLORS].
Abstract geometric shapes, subtle particle effects, dramatic lighting.
No text, no logos, no people. Pure abstract/geometric.
Style: minimal, premium, tech-forward. 16:9 aspect ratio, 1920x1080px.
```

```prompt
Create a luxurious dark background for a premium [PRODUCT] landing page.
Deep blacks with subtle [ACCENT COLOR] gradient orbs (400px blur).
Subtle noise texture overlay (2% opacity). Abstract flowing shapes.
No text, no UI elements. Pure atmospheric background.
Mood: sophisticated, exclusive, premium. 16:9 aspect ratio.
```

### Product Mockups

```prompt
Create a sleek product mockup frame for a [DEVICE/TYPE] on transparent background.
Minimalist design, subtle shadow, premium feel.
The device screen should be empty (solid dark #1a1a1a) for easy content overlay.
Style: Apple-like product photography. Clean, professional.
```

```prompt
Generate a browser mockup frame for showcasing a website.
Dark theme (#1a1a1a), minimal window chrome (no tabs bar).
Rounded corners (8px), subtle drop shadow.
The browser content area should be empty/dark for easy compositing.
Perspective: slight 3D angle (15° rotation).
```

### Icons & Illustrations

```prompt
Create a set of 6 minimal line icons for a [INDUSTRY] website.
Style: thin 1.5px stroke, rounded caps, consistent 48x48px grid.
Theme: [DESCRIBE THEMES]. Monochromatic white (#ffffff).
Clean, modern, professional. SVG-style appearance.
```

```prompt
Generate an abstract illustration for a [CONCEPT] feature section.
Style: flat design with subtle gradients, geometric shapes.
Colors: [BRAND COLORS] on transparent background.
Modern, tech-forward, minimal. No text.
```

### Textures & Patterns

```prompt
Create a subtle noise/grain texture for dark web backgrounds.
100x100px tileable pattern, 2-3% opacity when overlaid.
Pure black base with subtle monochromatic noise.
Seamless, tileable, minimal.
```

```prompt
Generate a subtle grid pattern for dark backgrounds.
Thin lines (0.5px), rgba(255,255,255,0.03) color.
Grid size: 40px x 40px. Seamless, tileable.
Perfect for adding depth to dark sections.
```

---

## Prompts para Animaciones Interactivas (Cinemático)

### Hero Animation Concepts

```prompt
Create a 5-frame animation storyboard for a cinematic website hero.
Frame 1: Black screen with subtle particle emergence
Frame 2: Particles form glowing lines that converge
Frame 3: Lines resolve into product/brand silhouette
Frame 4: Silhouette reveals with dramatic light sweep
Frame 5: Final composition with subtle ambient motion

Style: Dark premium, cinematic, smooth transitions.
Each frame: 1920x1080px, 16:9 ratio.
```

### Interactive Element Concepts

```prompt
Generate visual concepts for interactive hover states on a dark premium website:
1. Button hover: subtle glow expansion (3 states: normal, hover, active)
2. Card hover: glassmorphism + lift + border glow (3 states)
3. Image hover: subtle zoom + overlay reveal (3 states)
4. Link hover: underline animation from center (3 states)

Style: smooth, refined, premium. All on dark (#0a0a0b) background.
Show each state separately with transition arrows.
```

---

## Integración NanoBanana + Stitch

### Workflow: Hero Section

```bash
# Paso 1: Generar hero background con NanoBanana
python scripts/nanobanana_generate.py \
  "Dark cinematic hero background, black base with cyan glow orbs, 
   abstract geometric shapes, 1920x1080, premium tech aesthetic" \
  -o assets/hero-bg.png

# Paso 2: Usar la imagen como referencia en Stitch
# (Generar HTML con Stitch, insertar la imagen como background)
```

### Workflow: Feature Icons

```bash
# Paso 1: Generar set de iconos
python scripts/nanobanana_generate.py \
  "Set of 6 minimal line icons: rocket, shield, chart, users, 
   settings, zap. White on transparent, 48x48, thin stroke" \
  -o assets/icons/feature-set.png

# Paso 2: Extraer iconos individuales con processing
python scripts/extract_icons.py assets/icons/feature-set.png -o assets/icons/
```

### Workflow: Product Mockups

```bash
# Paso 1: Generar mockup frame
python scripts/nanobanana_generate.py \
  "Browser mockup frame, dark theme, empty screen area, 
   slight 3D angle, professional product photography style" \
  -o assets/mockups/browser.png

# Paso 2: Compositar screenshot dentro del mockup
python scripts/composite_mockup.py \
  --frame assets/mockups/browser.png \
  --content screenshots/app.png \
  -o assets/mockups/final.png
```

---

## Parámetros Óptimos

### Para Backgrounds Web

```json
{
  "temperature": 0.9,
  "topP": 0.95,
  "topK": 40,
  "candidateCount": 1,
  "responseModalities": ["TEXT", "IMAGE"],
  "imageConfig": {
    "aspectRatio": "16:9",
    "imageSize": "1K"
  }
}
```

### Para Assets/UI Elements

```json
{
  "temperature": 0.7,
  "topP": 0.9,
  "candidateCount": 3,
  "responseModalities": ["TEXT", "IMAGE"],
  "imageConfig": {
    "aspectRatio": "1:1",
    "imageSize": "1K"
  }
}
```

---

## Prompt Templates por Industria

### AI/Tech Company

```
Generate a premium hero image for an AI company website.
Visual concepts: neural networks, data flows, abstract AI representations.
Colors: Black base (#000000) with electric blue (#00d4ff) and purple (#7c3aed) accents.
Style: Futuristic, clean, sophisticated. No text, no logos.
Mood: Intelligence, innovation, trust. 16:9 aspect ratio.
```

### Fintech

```
Generate a premium hero image for a fintech platform website.
Visual concepts: abstract data visualization, growth charts, secure vault imagery.
Colors: Black base (#000000) with emerald (#10b981) and gold (#ffd700) accents.
Style: Professional, trustworthy, modern. No text, no logos.
Mood: Security, growth, prosperity. 16:9 aspect ratio.
```

### Health/Wellness

```
Generate a premium hero image for a health/wellness app website.
Visual concepts: organic shapes, flowing lines, natural gradients.
Colors: Dark base (#0a0a0b) with emerald (#10b981) and soft white accents.
Style: Clean, calming, modern. No text, no logos.
Mood: Wellness, balance, vitality. 16:9 aspect ratio.
```

### Creative Agency

```
Generate a premium hero image for a creative agency website.
Visual concepts: abstract art, bold shapes, creative chaos organized.
Colors: Black base (#000000) with vibrant accent (#ff6b35 or #a855f7).
Style: Bold, artistic, unexpected. No text, no logos.
Mood: Creativity, energy, originality. 16:9 aspect ratio.
```
