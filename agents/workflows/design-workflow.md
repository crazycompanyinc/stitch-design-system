# 🤖 WORKFLOWS DE AGENTES DE DISEÑO

> Procesos paso a paso para agentes de diseño web

## 1. Workflow Principal: Diseño Cinemático Completo

```
FASE 1: PREPARACIÓN
├── 1.1 Recopilar requirements del cliente
├── 1.2 Seleccionar paleta de colores (1 acento)
├── 1.3 Definir estructura de secciones (8-12 secciones)
└── 1.4 Crear DESIGN.md inicial

FASE 2: GENERACIÓN CON STITCH
├── 2.1 Generar diseño base con stitch_generate.py
├── 2.2 Generar 3 variaciones con diferentes acentos
├── 2.3 Evaluar y seleccionar la mejor variación
└── 2.4 Usar como HTML base

FASE 3: ASSETS CON NANOBANANA
├── 3.1 Generar hero background
├── 3.2 Generar feature icons/illustrations
├── 3.3 Generar product mockups (si aplica)
└── 3.4 Generar textures/patterns

FASE 4: COMPOSICIÓN
├── 4.1 Integrar assets de NanoBanana en HTML de Stitch
├── 4.2 Ajustar CSS para incorporar imágenes de fondo
├── 4.3 Optimizar carga (lazy loading, formatos)
└── 4.4 Verificar responsive con assets reales

FASE 5: ANIMACIÓN E INTERACCIÓN
├── 5.1 Implementar scroll-driven animations
├── 5.2 Agregar hover effects
├── 5.3 Implementar page transitions
├── 5.3 Agregar parallax effects
└── 5.4 Implementar cursor effects (opcional)

FASE 6: REFINAMIENTO
├── 6.1 Iterar con Stitch para mejorar secciones específicas
├── 6.2 Optimizar performance (CSS containment, will-change)
├── 6.3 Verificar accesibilidad (contraste, focus states)
└── 6.4 Cross-browser testing
```

## 2. Workflow: Stitch Prompt Engineering

```
INPUT: Descripción del producto/servicio

PASO 1: CONTEXTUALIZAR
- ¿Qué tipo de página? (landing, dashboard, portfolio, e-commerce)
- ¿Qué industria? (tech, fintech, salud, creativo)
- ¿Qué tono? (premium, playful, corporate, artistic)

PASO 2: CONSTRUIR PROMPT
Usar template maestro:
"[CONTEXTO] + [ESTILO] + [ESTRUCTURA] + [COMPONENTES] + [COLOR] + [RESTRICCIONES]"

PASO 3: GENERAR
- Enviar prompt a stitch_generate.py
- Timeout: 60s, max tokens: 8192
- Guardar output como draft

PASO 4: EVALUAR
Checklist de evaluación:
☐ ¿Background oscuro (#0a0a0b)?
☐ ¿Hero 100vh con impacto visual?
☐ ¿Tipografía grande y bold?
☐ ¿Acento de color con glow?
☐ ¿Scroll animations?
☐ ¿Glassmorphism aplicado correctamente?
☐ ¿Sin frameworks externos?
☐ ¿Responsive?

PASO 5: ITERAR
- Si falla algún check → ajustar prompt y regenerar
- Generar mínimo 3 variaciones
- Seleccionar la mejor como base
```

## 3. Workflow: NanoBanana Asset Pipeline

```
INPUT: Lista de assets necesarios para el diseño

PASO 1: LISTAR ASSETS
- Hero background (1920x1080, 16:9)
- Feature icons (48x48, SVG-style)
- Product mockups (various sizes)
- Section backgrounds (1920x400)
- Textures/patterns (100x100 tileable)

PASO 2: GENERAR CADA ASSET
Para cada asset:
1. Construir prompt específico (ver prompts/nanobanana/)
2. Llamar nanobanana_generate.py
3. Guardar en assets/
4. Verificar calidad (resolución, estilo consistente)
5. Si no cumple → ajustar prompt y regenerar

PASO 3: POST-PROCESO
- Convertir a formatos web (WebP para fotos, SVG para iconos)
- Optimizar tamaño (compressión sin pérdida visible)
- Generar versiones @2x para retina

PASO 4: INTEGRAR EN HTML
- Reemplazar placeholders con URLs de assets
- Añadir lazy loading para below-fold
- Añadir alt text para accesibilidad
```

## 4. Workflow: Iteración y Refinamiento

```
INPUT: Diseño HTML generado por Stitch

PASO 1: REVISIÓN INICIAL
Verificar en browser (browser_vision):
- ¿Se ve bien en desktop (1440px)?
- ¿Se ve bien en tablet (768px)?
- ¿Se ve bien en mobile (375px)?
- ¿Las animaciones funcionan?
- ¿El scroll es suave?

PASO 2: LISTAR MEJORAS
Crear lista de issues encontrados:
- [ ] Heading muy pequeño en sección X
- [ ] Color de acento inconsistente
- [ ] Animación no trigger en sección Y
- [ ] Padding insuficiente en mobile
- [ ] etc.

PASO 3: REFINAR CON STITCH
Para cada issue:
1. Crear prompt de refinamiento específico
2. Ejecutar stitch_generate.py con el refinamiento
3. Integrar el cambio en el HTML
4. Verificar que no rompió nada más

PASO 4: HAND-CODE POLISH
Cambios que Stitch no puede hacer bien:
- Ajustar valores CSS específicos (1-2px fixes)
- Añadir custom scrollbar styling
- Implementar complex hover states
- Fix cross-browser issues
- Optimizar performance

PASO 5: FINAL QA
- Test en Chrome, Firefox, Safari
- Test responsive (3 breakpoints)
- Test rendimiento (Lighthouse)
- Test accesibilidad (axe/WAVE)
- Test links y CTAs funcionales
```

## 5. Workflow: Deploy

```
INPUT: HTML/CSS/JS final + assets

Para Vercel:
1. Crear proyecto en Vercel
2. Conectar repo de GitHub
3. Configurar build settings: static site
4. Push to main → auto deploy
5. Verificar en URL de preview

Para GitHub Pages:
1. Crear repo con index.html en root
2. Settings → Pages → Source: main branch
3. Esperar 2-3 min
4. Verificar en username.github.io/repo

Para Cloudflare Pages:
1. Conectar repo
2. Build settings: No build command (static)
3. Output directory: /
4. Deploy
```
