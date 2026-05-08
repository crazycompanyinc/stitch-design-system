# 🎨 STITCH PROMPTS — Guía Completa

> Prompts optimizados para Google Stitch vía Gemini API

## Índice

1. [Anatomía de un Prompt Perfecto](#anatomía)
2. [Prompts por Tipo de Página](#por-tipo)
3. [Prompts por Componente](#por-componente)
4. [Prompts de Estilo Cinematográfico](#cinematic)
5. [Prompts de Refinamiento](#refinamiento)
6. [Anti-Prompts (qué evitar)](#anti-prompts)

---

## Anatomía de un Prompt Perfecto <a name="anatomía"></a>

Todo prompt para Stitch debe seguir esta estructura:

```
[CONTEXTO] + [ESTILO] + [ESTRUCTURA] + [COMPONENTES] + [COLOR] + [RESTRICCIONES]
```

### Template Maestro

```
Create a complete, self-contained HTML/CSS/JS landing page for [PRODUCT/SERVICE].

STYLE: [Dark/Light] mode, [modern/cinematic/minimal/premium] aesthetic.
TYPOGRAPHY: [Font choices], bold headings, generous spacing.
COLORS: Background #[hex], Accent #[hex] with glow effect.
LAYOUT: [hero/features/grid/bento/asymmetric].

SECTIONS (in order):
1. Navigation (fixed, glassmorphism)
2. Hero (100vh, fullscreen background, CTA buttons)
3. [Section 2 - context-specific]
4. [Section 3 - context-specific]
5. Features/Services (bento grid or cards)
6. Social Proof (testimonials/logos)
7. CTA Final
8. Footer

INTERACTIONS:
- Scroll-driven reveal animations
- Hover effects (translate, glow, border)
- Smooth scroll
- Custom scrollbar

TECHNICAL:
- Single HTML file (all CSS in <style>, JS in <script>)
- NO external frameworks (no Bootstrap, no Tailwind CDN)
- CSS custom properties for all tokens
- Responsive (mobile-first)
- IntersectionObserver for scroll animations
```

---

## Prompts por Tipo de Página <a name="por-tipo"></a>

### 🚀 SaaS / Tech Startup

```
Create a complete premium dark landing page for [PRODUCT], a [DESCRIPTION].

Hero: Full-viewport with animated gradient mesh background (deep blues/purples 
on black), large bold title "Transform [BENEFIT] with [PRODUCT]", subtitle 
explaining the value prop, primary CTA "Start Free Trial" (glowing orange 
#ff6b35), secondary CTA "Watch Demo" (ghost button).

Sections:
- Trust Bar: "Trusted by 10,000+ companies" + logo placeholders
- Features: Bento grid with 6 cards (icon, title, description). Use glassmorphism 
  cards with subtle borders. Each card has hover glow effect.
- How It Works: 3-step horizontal process with connecting lines and numbered circles
- Pricing: 3-tier cards (Starter $29, Pro $79, Enterprise). Middle card highlighted 
  with glow border. Annual/monthly toggle.
- Testimonials: Horizontal scroll carousel with 5 testimonials
- FAQ: Accordion with 6 questions
- Final CTA: Dark section with gradient accent, "Ready to get started?" + CTA button
- Footer: 4-column layout with links

Style: Dark #0a0a0b, accent #ff6b35, fonts Space Grotesk + Inter, 
border-radius 8-16px, glassmorphism cards with backdrop-filter blur(20px).
All scroll-driven animations via IntersectionObserver.
Single self-contained HTML file.
```

### 💰 Fintech / Crypto

```
Create a complete premium landing page for [PRODUCT], a [DESCRIPTION].

Hero: Dark cinematic background (#000000), large typography "The Future of 
[BENEFIT] is Here", clean minimal design, subtle particle animation effect.
Primary CTA: "Get Started" (#00d4ff cyan glow). Secondary: "Learn More".

Sections:
- Stats Bar: "Total Volume $2.5B+", "Active Users 50K+", "Countries 120+" in 
  large monospace numbers
- Features: 4-column grid with icons, clean minimal cards with subtle borders
- Security: Large lock icon + "Bank-grade security" statement with animated 
  shield graphic
- App Screenshots: Mockup carousel showing mobile/web interface
- Compliance: SOC2, GDPR, PCI-DSS badges
- Pricing: Simple 2-tier (Free / Pro $19/mo) with clear feature comparison
- Testimonials: 3-column with star ratings and photos
- CTA Final: Gradient background, "Join 50,000+ users" + signup button

Style: Black #000000, accent #00d4ff cyan, fonts Inter + JetBrains Mono, 
sharp corners (4-8px radius), minimal glassmorphism.
Subtle cyan glow on all interactive elements.
Single HTML file.
```

### 🎨 Creative Agency / Portfolio

```
Create a complete premium dark portfolio website for [NAME/AGENCY].

Hero: Full-viewport with large animated typography "We Create Digital 
Experiences That Matter". Subtle mouse-follow gradient effect. CTA: "View Our 
Work" (pill button with hover scale animation).

Sections:
- Work Grid: Masonry layout with 6 projects (image, title, category). 
  Hover reveals project details with smooth overlay animation.
- Services: Horizontal scroll section with 4 services, each with icon and 
  description. Parallax scroll effect.
- About: Split layout (left: large portrait photo, right: bio text and stats 
  "100+ Projects", "15 Years", "30 Awards")
- Process: 4-step vertical timeline with icons and descriptions
- Clients: Infinite horizontal scroll logo bar
- Contact: Minimal form with 4 fields, social links, map placeholder

Style: Black #0a0a0b, accent #ffd700 gold or #ff6b35 coral, fonts Space Grotesk 
display + Inter body. Generous whitespace (120px between sections). 
Smooth scroll, parallax effects, cursor-follow glow.
Single HTML file.
```

### 🏋️ Fitness / Health App

```
Create a complete premium dark fitness app landing page for [PRODUCT].

Hero: Full-screen with dark muscular gradient background, bold typography 
"Transform Your Body", app mockup floating with subtle 3D animation effect.
CTA: "Start Free Trial" (strong orange #ff6b35), "Download App" (App Store badges).

Sections:
- Stats: "50M+ Workouts Completed", "4.9★ Rating", "10M+ Users" in large numbers
- Features: Bento grid with workout photos, progress tracking, nutrition, community
- Plans: Feature comparison table (Free, Premium $9.99, Pro $19.99)
- Testimonials: Before/after transformation photos with quotes
- App Preview: 3-phone mockup showing app screens
- CTA: "Download Now" + App Store/Google Play badges

Style: Dark #111111, accent #ff6b35 orange, energetic, bold typography, 
rounded corners (16px), vibrant gradient overlays.
Single HTML file.
```

### 🛒 E-commerce / DTC Brand

```
Create a complete premium e-commerce landing page for [PRODUCT/BRAND].

Hero: Full-bleed product photography with dramatic lighting, overlay gradient 
from black to transparent, product name in large bold typography, price and 
"Add to Cart" CTA with accent glow.

Sections:
- Product Gallery: Horizontal scroll with 6+ product images, magnifying glass hover
- Features: Icon grid (Free Shipping, 30-Day Returns, Secure Payment)
- How It Works: 3-step visual process
- Reviews: Star ratings + review cards with user photos
- Size Guide: Modal toggle with measurement chart
- Newsletter: Email capture with "Get 10% Off" incentive
- Instagram Feed: Grid of 9 lifestyle images

Style: Black or dark gray background, product-focused, clean minimal UI, 
elegant typography (serif headings + sans body), subtle hover animations.
Single HTML file.
```

---

## Prompts por Componente <a name="por-componente"></a>

### Navigation

```
Create a fixed navigation bar with glassmorphism (rgba(255,255,255,0.05) background, 
backdrop-filter blur(20px)), rounded pill shape (border-radius 9999px), horizontal 
layout. Left: logo text "BRAND". Center: 5 nav links (Services, Work, About, Blog, 
Contact) in 14px Inter font weight 500, white with 70% opacity. Right: CTA button 
"Contact" with accent color background and subtle glow. On scroll, add subtle 
border-bottom and reduce padding. Mobile: hamburger menu.
```

### Hero Section

```
Create a 100vh hero section with:
- Background: CSS gradient mesh (radial gradients layered) in dark tones + accent 
  color glow orb (400px, blur 150px, 0.1 opacity)
- Content centered vertically and horizontally
- Overline: 12px uppercase tracking label "New Release"
- Heading: 72px bold, white, tight line-height 1.05, letter-spacing -0.03em
- Subtitle: 22px, rgba(255,255,255,0.6), max-width 550px, centered
- CTA: Two buttons side by side — primary (solid accent with box-shadow glow) 
  and secondary (ghost with border)
- Scroll indicator at bottom: "SCROLL" text + animated vertical line

All content fades in on load with 0.5s staggered animation.
```

### Feature Card (Glassmorphism)

```
Create a glassmorphism feature card:
- Background: rgba(255,255,255,0.03)
- Border: 1px solid rgba(255,255,255,0.08)
- Border-radius: 16px
- Padding: 32px
- Backdrop-filter: blur(20px)
- Content: icon (64px, gradient background circle), heading (24px bold), 
  description (16px, muted opacity)
- Hover: border-color rgba(255,255,255,0.15), transform translateY(-4px), 
  box-shadow 0 20px 60px rgba(0,0,0,0.4)
- Transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1)
```

### Bento Grid

```
Create a bento grid layout (4 columns, variable height rows):
- Display: grid, grid-template-columns: repeat(4, 1fr), gap: 16px
- Items span multiple columns/rows using grid-column/grid-row
- Each item is a glassmorphism card (see card spec above)
- Mix of content types: text, images, charts, stats, testimonials
- Large item (2x2): Main feature showcase
- Tall item (1x2): Stats counter
- Wide item (2x1): Quote/testimonial
- Small items (1x1): Feature highlights with icons
```

### Testimonial Carousel

```
Create an infinite horizontal scroll testimonial section:
- Track display: flex, animation: scroll 30s linear infinite
- Each testimonial: 400px wide card, glassmorphism style
- Content: quote text (italic, 18px), author name, role, company, star rating (★★★★★)
- Hover pauses the scroll animation
- Gradient masks on left/right edges for smooth fade
```

---

## Prompts de Estilo Cinematográfico <a name="cinematic"></a>

### Dark Premium

```
Dark cinematic design:
- Background: #0a0a0b (near-black with subtle blue undertone)
- Text primary: #ffffff (pure white for headings)
- Text secondary: rgba(255,255,255,0.65) (body text)
- Text muted: rgba(255,255,255,0.40) (labels, metadata)
- Surface: rgba(255,255,255,0.03-0.08) (cards, panels)
- Border: rgba(255,255,255,0.06-0.12) (subtle dividers)
- Accent: single vibrant color (choose ONE per project)
- Glow: box-shadow 0 0 40px rgba(accent, 0.2) on CTA elements
- Typography: Bold, large, tight tracking for headings
```

### Accent Color Palette (elegir UNO)

```
ENERGY:    #ff6b35 (coral orange) — startups, fitness, food
TECH:      #00d4ff (electric cyan) — SaaS, fintech, developer tools
CREATIVE:  #a855f7 (neon purple) — agencies, AI, creative tools
PREMIUM:   #ffd700 (gold) — luxury, consulting, high-end
NATURE:    #10b981 (emerald) — wellness, sustainability, health
FEMININE:  #f472b6 (pink) — beauty, fashion, lifestyle
CORPORATE: #1c69d4 (BMW blue) — enterprise, B2B, serious
```

---

## Prompts de Refinamiento <a name="refinamiento"></a>

### Iteración de Diseño

```
Take the current design and make these improvements:
1. Increase all heading sizes by 20% for more impact
2. Add more breathing room (padding) between sections
3. Strengthen the accent glow effects (increase blur and spread)
4. Add micro-interactions: button scale on hover, card lift on hover
5. Improve mobile responsiveness: ensure all text is readable on 375px
6. Add loading animation: fade-in with stagger on page load
7. Enhance glassmorphism: increase blur to 30px on cards
8. Add custom scrollbar styling
9. Ensure all interactive elements have visible focus states
10. Optimize: lazy load all images, use CSS containment
```

### Conversión de Diseño

```
Convert this Figma/Sketch/wireframe description into HTML:

[PASTE DESIGN DESCRIPTION OR UPLOAD IMAGE]

Extracts:
- Color palette (map to CSS custom properties)
- Typography scale (map to heading/body text sizes)
- Spacing system (map to CSS spacing variables)
- Component library (buttons, cards, nav, etc.)
- Layout grid (map to CSS Grid/Flexbox)
- Animation spec (map to CSS transitions/animations)

Output: Complete HTML/CSS/JS implementation.
```

---

## Anti-Prompts (qué evitar) <a name="anti-prompts"></a>

### ❌ NO hacer esto

```
EVITE estas palabras/frases en sus prompts:
- "Make it pop" — demasiado vago, no genera acción específica
- "Modern design" — ambiguo, especifique qué significa moderno
- "Beautiful" — subjetivo, describa características específicas
- "Like Stripe/Linear/Apple" — no copie, inspírese y cree algo único
- "Responsive" — SIEMPRE incluya mobile-first, no es opcional
- "With animations" — especifique QUÉ animaciones y DÓNDE
- "Dark mode" — especifique colores exactos (#0a0a0b no "dark")
- "Clean" — especifique whitespace values (padding, margin, gap)
- "Professional" — especifique la industria y el tono
```

### ✅ SÍ hacer esto

```
USE estas palabras/frases para mejores resultados:
- Hex colors exactos: "background #0a0a0b, accent #ff6b35"
- Font sizes exactos: "heading 72px bold, body 16px regular"
- Spacing exacto: "padding 32px, gap 16px, section margin 120px"
- Animation specs: "fade-in 0.8s cubic-bezier(0.16, 1, 0.3, 1)"
- Layout exacto: "grid 4 columns, first item spans 2 columns"
- Naming específico: "glassmorphism card, bento grid, pill CTA"
- Interaction details: "hover: translateY(-4px), box-shadow glow"
```

### Prompts Específicos > Prompts Vagos

```
❌ VAGO:    "Make a nice landing page for my app"
✅ ESPECÍFICO: "Create a 100vh hero section with dark gradient background 
   (#0a0a0b to #1a1025), 72px bold white heading 'AI Writing Assistant', 
   18px subtitle in rgba(255,255,255,0.6), primary CTA button with #ff6b35 
   background and box-shadow: 0 0 40px rgba(257,107,53,0.3), 2 rem padding 
   top/bottom. Single HTML file."

❌ VAGO:    "Add some animations"
✅ ESPECÍFICO: "Add IntersectionObserver-based scroll reveal: elements start 
   with opacity:0 and transform:translateY(40px), transition to opacity:1 
   and transform:translateY(0) with 0.8s cubic-bezier easing. Stagger delay 
   of 0.1s between siblings."

❌ VAGO:    "Make it look premium"
✅ ESPECÍFICO: "Use glassmorphism: rgba(255,255,255,0.05) backdrop-filter 
   blur(20px), 1px solid rgba(255,255,255,0.08) border, 16px 
   border-radius. Typography: Space Grotesk 72px 700 weight for hero, 
   Inter 16px 400 for body. Generous 120px section padding."
```
