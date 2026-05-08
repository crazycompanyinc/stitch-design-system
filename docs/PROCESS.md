# 🎬 PROCESO DE DISEÑO CINEMÁTICO — Stitch + NanoBanana

> Proceso claro y efectivo para crear webs cinematográficas con IA

## Visión General

```
┌─────────────────────────────────────────────────────────────────┐
│                    CINEMATIC WEB DESIGN                          │
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ STITCH   │───▶│NANOBANANA│───▶│  GEMINI  │───▶│  DEPLOY  │  │
│  │ Layout   │    │  Assets  │    │   Code   │    │  Live    │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│       │               │               │               │        │
│       ▼               ▼               ▼               ▼        │
│   3 variaciones   Hero bg        HTML/CSS/JS     Vercel/GH     │
│   por acento      Icons          Refinamiento     Pages/CF      │
│                   Mockups        Integration                   │
│                   Animations     Optimization                  │
└─────────────────────────────────────────────────────────────────┘
```

## FASE 1: PREPARACIÓN (5 minutos)

### 1.1 — Definir el Producto

Responder estas preguntas:
- ¿Qué producto/servicio? (1 frase)
- ¿Quién es el target? (edad, perfil)
- ¿Qué acción debe hacer el usuario? (CTA principal)
- ¿Qué tono visual? (premium, playful, corporate, artistic)
- ¿Colores de marca? (si no hay, elegir de la paleta cinematográfica)

### 1.2 — Elegir Paleta de Colores

**Siempre dark mode como base:**

| Elemento | Color |
|---|---|
| Background primary | `#0a0a0b` |
| Background secondary | `#111113` |
| Text primary | `#ffffff` |
| Text secondary | `rgba(255,255,255,0.65)` |
| Text muted | `rgba(255,255,255,0.40)` |
| Surface/cards | `rgba(255,255,255,0.03-0.08)` |
| Border | `rgba(255,255,255,0.08-0.12)` |

**Elegir UN acento:**

| Industria | Acento | Hex |
|---|---|---|
| AI/Tech/SaaS | Electric Cyan | `#00d4ff` |
| Fintech/Crypto | Emerald | `#10b981` |
| Health/Wellness | Emerald Green | `#10b981` |
| Creative/Agency | Neon Purple | `#a855f7` |
| Luxury/Premium | Gold | `#ffd700` |
| Fitness/Food | Coral Orange | `#ff6b35` |
| Fashion/Beauty | Pink | `#f472b6` |
| Enterprise/B2B | BMW Blue | `#1c69d4` |

### 1.3 — Definir Estructura de Secciones

Mínimo 8 secciones:
```
1. Navigation (fixed, glassmorphism)
2. Hero (100vh, fullscreen, impacto máximo)
3. Trust/Social Proof (logos, métricas)
4. Features (bento grid, 4-6 features)
5. How It Works / Process (3-4 pasos)
6. Showcase / Product (imágenes, demos)
7. Testimonials + Pricing
8. CTA Final + Footer
```

---

## FASE 2: STITCH — Generar Layout Base (15 minutos)

### 2.1 — Construir Prompt para Stitch

Usar este template:

```bash
python scripts/stitch_generate.py "Create a complete cinematic landing page for [PRODUCT], a [DESCRIPTION].

STYLE: Dark mode (#0a0a0b), [premium/cinematic/modern] aesthetic.
TYPOGRAPHY: Space Grotesk for headings, Inter for body.
COLORS: Background #0a0a0b, Accent #[ACCENT_COLOR] with glow effect.

SECTIONS:
1. Navigation (fixed, glassmorphism pill)
2. Hero (100vh, gradient overlay, large title, CTA)
3. Trust Bar (logos + metrics)
4. Features (bento grid, 6 cards, glassmorphism)
5. How It Works (3 steps, connected timeline)
6. Product Showcase (image + text split layout)
7. Testimonials (horizontal carousel, 5 cards)
8. Pricing (3 tiers, middle highlighted)
9. CTA Final (gradient background, large CTA)
10. Footer (4-column links)

INTERACTIONS:
- Scroll-driven reveal animations
- Hover effects: translateY(-4px) + glow
- Smooth scroll, custom scrollbar
- Nav background darkens on scroll

TECHNICAL:
- Single HTML file (all CSS in <style>, JS in <script>)
- NO Bootstrap, NO Tailwind CDN
- CSS custom properties for all tokens
- Responsive: mobile-first

Generate the complete HTML now." -o output/design.html
```

### 2.2 — Generar 3 Variaciones

```bash
python scripts/stitch_generate.py "[PROMPT]" --variations 3 -o output/design.html
```

Esto genera `design_v1.html`, `design_v2.html`, `design_v3.html` con diferentes acentos.

### 2.3 — Evaluar y Seleccionar

Abrir cada variación en browser y evaluar:

```
CHECKLIST DE EVALUACIÓN:
☐ Background oscuro (#0a0a0b)?                    [0-10]
☐ Hero 100vh con impacto visual?                  [0-10]
☐ Tipografía grande (hero ≥72px)?                 [0-10]
☐ Acento de color con glow?                       [0-10]
☐ Glassmorphism cards?                            [0-10]
☐ Bento grid layout?                              [0-10]
☐ Sin frameworks externos?                        [0-10]
☐ Responsive (mobile OK)?                         [0-10]
☐ Scroll animations implementadas?                [0-10]
☐ Se siente como una película?                    [0-10]
                                                   ---
TOTAL:                                             [/100]
```

**Seleccionar la variación con mayor score.**

---

## FASE 3: NANOBANANA — Crear Assets (20 minutos)

### 3.1 — Generar Hero Background

```bash
python scripts/nanobanana_generate.py \
  "Dark cinematic hero background for [INDUSTRY] website. 
   Deep black (#0a0a0b) base with subtle [ACCENT] gradient orbs.
   Abstract geometric shapes, dramatic lighting, premium feel.
   No text, no logos. 16:9 aspect ratio." \
  -o assets/hero-bg.png --aspect-ratio 16:9
```

### 3.2 — Generar Feature Icons

```bash
python scripts/nanobanana_generate.py \
  "Set of 6 minimal line icons on transparent background:
   [ICON_1], [ICON_2], [ICON_3], [ICON_4], [ICON_5], [ICON_6].
   Style: thin 1.5px stroke, rounded caps, 48x48px each.
   White (#ffffff) color. Clean, modern, consistent style." \
  -o assets/icons/features.png --aspect-ratio 1:1
```

### 3.3 — Generar Product Mockup Frame

```bash
python scripts/nanobanana_generate.py \
  "Browser mockup frame for website showcase.
   Dark theme (#1a1a1a), minimal window chrome.
   Rounded corners (8px), subtle drop shadow.
   Screen area should be empty/dark for compositing.
   Slight 3D perspective angle. Professional." \
  -o assets/mockups/browser.png --aspect-ratio 16:9
```

### 3.4 — Generar Animación Interactiva (para secciones)

```bash
# Frame 1: Estado inicial
python scripts/nanobanana_generate.py \
  "Abstract particle field on black background, particles scattered randomly.
   Subtle [ACCENT] glow. Cinematic, tech-forward. No text." \
  -o assets/animations/hero_01.png --aspect-ratio 16:9

# Frame 2: Partículas convergiendo
python scripts/nanobanana_generate.py \
  "Abstract particles converging into flowing lines on black background.
   [ACCENT] colored particle trails, smooth motion blur effect.
   Cinematic, dynamic. No text." \
  -o assets/animations/hero_02.png --aspect-ratio 16:9

# Frame 3: Forma revelándose
python scripts/nanobanana_generate.py \
  "Flowing light lines forming an abstract geometric shape on black.
   Dramatic [ACCENT] glow, cinematic reveal moment.
   Premium, high-end feel. No text." \
  -o assets/animations/hero_03.png --aspect-ratio 16:9
```

### 3.5 — Batch Generation (Alternativa)

Crear archivo `assets/batch.json`:

```json
[
  {
    "prompt": "Dark cinematic hero background with cyan glow orbs",
    "output": "hero-bg.png",
    "aspect_ratio": "16:9"
  },
  {
    "prompt": "Set of 6 minimal line icons: rocket, shield, chart, users, settings, zap",
    "output": "icons/features.png",
    "aspect_ratio": "1:1"
  },
  {
    "prompt": "Dark noise texture, 100x100 tileable",
    "output": "textures/noise.png",
    "aspect_ratio": "1:1"
  }
]
```

```bash
python scripts/nanobanana_generate.py --batch assets/batch.json
```

---

## FASE 4: INTEGRACIÓN — Componer Diseño Final (30 minutos)

### 4.1 — Integrar Hero Background

En el HTML de Stitch, reemplazar el gradiente del hero:

```css
.hero-bg {
  position: absolute;
  inset: 0;
  background: url('assets/hero-bg.png') center/cover no-repeat;
}
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(10,10,11,0.3) 0%, rgba(10,10,11,0.95) 100%);
}
```

### 4.2 — Integrar Iconos

Reemplazar iconos placeholder con los generados:

```html
<img src="assets/icons/rocket.svg" alt="Fast" loading="lazy">
```

### 4.3 — Integrar Mockups

Compositar screenshots dentro de mockups:

```css
.product-showcase {
  position: relative;
}
.product-showcase .frame {
  background: url('assets/mockups/browser.png') center/contain no-repeat;
}
.product-showcase .screenshot {
  position: absolute;
  /* ajustar posición para que encaje en el mockup */
  top: 8%; left: 12%; width: 76%; height: 72%;
  object-fit: cover;
}
```

### 4.4 — Integrar Animaciones

Para la animación interactiva del hero (frames de NanoBanana):

```html
<div class="hero-animation">
  <img src="assets/animations/hero_01.png" class="frame active" alt="">
  <img src="assets/animations/hero_02.png" class="frame" alt="">
  <img src="assets/animations/hero_03.png" class="frame" alt="">
</div>
```

```javascript
// Ciclar frames de animación
const frames = document.querySelectorAll('.hero-animation .frame');
let current = 0;
setInterval(() => {
  frames[current].classList.remove('active');
  current = (current + 1) % frames.length;
  frames[current].classList.add('active');
}, 2000);
```

O mejor: usar las frames como spritesheet para animación de scroll-driven.

---

## FASE 5: REFINAMIENTO (20 minutos)

### 5.1 — Iterar con Stitch

Para secciones específicas que necesitan mejora:

```bash
python scripts/stitch_generate.py \
  "Refine the pricing section of this design. Make cards more prominent, 
   add glow effect to the recommended plan, improve mobile layout. 
   Keep dark mode (#0a0a0b), accent #[COLOR]." \
  -o output/pricing_refined.html
```

### 5.2 — Refinar Manualmente

Cambios que Stitch no hace bien:
- Ajustar valores CSS específicos (1-2px)
- Custom scrollbar
- Complex hover states
- CSS containment y will-change para performance
- Lazy loading de imágenes
- Form validation

### 5.3 — QA Final

```
QA CHECKLIST:
☐ Desktop 1440px — diseño intacto
☐ Tablet 768px — layout correcto
☐ Mobile 375px — todo legible y funcional
☐ Mobile 320px — no overflow horizontal
☐ Colores consistentes
☐ Tipografía legible (mín 16px body)
☐ Imágenes nítidas
☐ Animaciones fluidas
☐ Links y CTAs funcionales
☐ Lighthouse Performance ≥ 80
☐ Contraste WCAG AA (4.5:1)
```

---

## FASE 6: DEPLOY (5 minutos)

### Vercel (recomendado)

```bash
cd /root/my-project
vercel --prod
```

### GitHub Pages

```bash
git init && git add -A
git commit -m "Initial deploy"
git remote add origin https://github.com/USER/REPO.git
git push -u origin main
# Settings → Pages → Source: main branch
```

### Cloudflare Pages

```bash
# Conectar repo en dash.cloudflare.com/pages
# Build settings: No build command, output: /
```

---

## RESUMEN DEL PROCESO

| Fase | Tiempo | Herramienta | Output |
|---|---|---|---|
| 1. Preparación | 5 min | Manual | Paleta, estructura, brief |
| 2. Stitch Layout | 15 min | stitch_generate.py | 3 variaciones HTML |
| 3. NanoBanana Assets | 20 min | nanobanana_generate.py | Hero bg, icons, mockups |
| 4. Integración | 30 min | Manual + scripts | HTML final con assets |
| 5. Refinamiento | 20 min | Stitch iterate + manual | HTML refinado |
| 6. Deploy | 5 min | vercel/gh pages | URL en producción |
| **TOTAL** | **~95 min** | | |

---

## NOTAS IMPORTANTES

### Sobre Stitch (Google)
- Stitch es una herramienta de diseño de Google Labs que usa Gemini
- Genera UIs desde texto, wireframes o screenshots
- Exporta a código HTML/CSS
- Template: stitch.withgoogle.com
- API: Gemini 2.0 Flash via generativelanguage.googleapis.com

### Sobre Nano Banana
- Modelo de generación de imágenes de Gemini API
- Endpoint: gemini-2.0-flash-exp-image-generation
- Soporta: text-to-image, image editing, variations
- Ideal para: hero backgrounds, icons, mockups, textures
- No genera video directamente (usar Veo para video)

### Sobre "Cinemático"
- No es solo "bonito" — es una EXPERIENCIA
- Cada sección = una escena de película
- Scroll = línea temporal
- Imágenes/video = contenido principal
- Tipografía = diálogos
- Espacios vacíos = pausas dramáticas
- Animaciones = transiciones de cámara
- NanoBanana crea los "efectos visuales" (hero backgrounds, animaciones)
- Stitch crea la "estructura narrativa" (layout, flujo)
