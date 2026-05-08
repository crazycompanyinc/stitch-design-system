# 🎬 Stitch Design System — Cinematic Web Design with AI

> **Guía definitiva para diseño web cinematográfico usando Google Stitch + NanoBanana + Gemini**

## Stack Tecnológico

| Herramienta | Uso | API |
|---|---|---|
| **Google Stitch** | Generación de layouts/UI desde prompts | Gemini API (`gemini-2.0-flash`) |
| **Nano Banana** | Generación de imágenes/animaciones interactivas | Gemini Image API |
| **Gemini 2.0 Flash** | Generación de código HTML/CSS/JS | Gemini API |
| **Imagen 3** | Imágenes estáticas de alta calidad | Gemini API |
| **Veo** | Generación de video para hero sections | Gemini API |

## Proceso de Diseño (5 pasos)

```
1. STITCH → Generar layout base desde prompt
2. NANOBANANA → Crear imágenes/animaciones interactivas
3. GEMINI CODE → Generar HTML/CSS/JS completo
4. REFINE → Iterar y refinar diseño
5. DEPLOY → Publicar en Vercel/GitHub Pages
```

## Estructura del Repo

```
├── prompts/
│   ├── stitch/          # Prompts optimizados para Stitch
│   ├── nanobanana/      # Prompts para imágenes/animaciones
│   └── cinematic/       # Prompts para estilo cinematográfico
├── agents/
│   ├── workflows/       # Workflows de agentes de diseño
│   └── personas/        # Personas/roles para agentes
├── templates/
│   ├── html/            # Templates HTML base
│   └── css/             # Sistemas de diseño CSS
├── scripts/             # Scripts de automatización
├── examples/
│   ├── landing-pages/   # Ejemplos completos
│   └── components/      # Componentes reutilizables
└── docs/                # Documentación extendida
```

## Uso Rápido

```bash
# Generar diseño con Stitch
python scripts/stitch_generate.py "Landing page for AI startup" -o output.html

# Generar imágenes con NanoBanana
python scripts/nanobanana_generate.py "Hero image for fintech app" -o hero.png

# Generar animación interactiva
python scripts/nanobanana_animate.py "Interactive 3D product showcase" -o animation.mp4
```

## Referencias

- [Google Stitch](https://stitch.withgoogle.com)
- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [Nano Banana Model](https://ai.google.dev/gemini-api/docs/models)
