#!/usr/bin/env python3
"""
stitch_generate.py — Stitch by Google: Generador de diseno web con Gemini API

Uso:
    export STITCH_API_KEY="your-key"
    python stitch_generate.py "Landing page for AI startup" -o output.html
    python stitch_generate.py --variations 3 "Fintech landing page"
"""

import requests, json, sys, argparse, os, time

# Leer API key de variable de entorno
STITCH_API_KEY = os.environ.get("STITCH_API_KEY", "")
MODEL = "gemini-2.0-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

STITCH_SYSTEM_PROMPT = (
    "You are Stitch by Google, an expert web design AI that creates premium cinematic websites.\n\n"
    "MANDATORY DESIGN RULES:\n"
    "1. DARK MODE ALWAYS - Background: #0a0a0b, Text: #ffffff primary, rgba(255,255,255,0.65) secondary\n"
    "2. TYPOGRAPHY - Display: Space Grotesk 72px bold hero, Body: Inter 16px regular\n"
    "3. HERO 100vh minimum, centered content, CTA buttons with accent glow\n"
    "4. GLASSMORPHISM - rgba(255,255,255,0.05) backdrop-filter blur(20px), 1px solid rgba(255,255,255,0.08)\n"
    "5. SINGLE ACCENT COLOR with glow effect (box-shadow: 0 0 40px rgba(accent, 0.2))\n"
    "6. BENTO GRID layouts for features (CSS Grid, asymmetric)\n"
    "7. SCROLL ANIMATIONS via IntersectionObserver (opacity 0->1, translateY 40px->0)\n"
    "8. NAV fixed, glassmorphism pill style\n"
    "9. BUTTONS: 4px border-radius, accent glow on primary, ghost style secondary\n"
    "10. CARDS: glassmorphism, hover: translateY(-4px) + border brighten\n"
    "11. SECTIONS: 120px vertical padding minimum\n"
    "12. SINGLE HTML FILE - ALL CSS in <style>, ALL JS in <script>\n"
    "13. NO Bootstrap, NO Tailwind CDN, NO external CSS frameworks\n"
    "14. CSS custom properties (:root) for ALL tokens\n"
    "15. Responsive: mobile-first, custom scrollbar (6px, accent colored)\n\n"
    "OUTPUT: Return ONLY the complete HTML code. Start with <!DOCTYPE html>.\n"
    "No explanations, no markdown code blocks. Pure HTML."
)


def generate_design(prompt, api_key=None, model=MODEL, temperature=0.85):
    """Genera diseno web completo usando Stitch (Gemini API)."""
    key = api_key or STITCH_API_KEY
    if not key:
        raise ValueError("STITCH_API_KEY not set. Run: export STITCH_API_KEY='your-key'")
    
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    full_prompt = STITCH_SYSTEM_PROMPT + "\n\n---\n\nDesign request: " + prompt + "\n\nGenerate the complete HTML now. Output ONLY HTML code."
    
    response = requests.post(
        f"{endpoint}?key={key}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {"temperature": temperature, "maxOutputTokens": 8192, "topP": 0.95}
        },
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    
    if "candidates" not in data or not data["candidates"]:
        raise ValueError(f"No candidates: {json.dumps(data, indent=2)[:500]}")
    
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    text = text.strip()
    for prefix in ["```html", "```"]:
        if text.startswith(prefix):
            text = text[len(prefix):]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def refine_design(html, instructions, api_key=None):
    """Refina un diseno existente."""
    key = api_key or STITCH_API_KEY
    if not key:
        raise ValueError("STITCH_API_KEY not set.")
    
    prompt = ("Refine this HTML/CSS/JS website design with these instructions: " + instructions +
              "\n\nCurrent HTML:\n" + html + "\n\nApply the changes and return the complete refined HTML. Output ONLY HTML code.")
    
    response = requests.post(
        f"{ENDPOINT}?key={key}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": STITCH_SYSTEM_PROMPT + "\n\n" + prompt}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 8192}
        },
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    text = text.strip()
    for prefix in ["```html", "```"]:
        if text.startswith(prefix):
            text = text[len(prefix):]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def generate_variations(prompt, count=3, api_key=None):
    """Genera multiples variaciones de diseno."""
    variations = []
    accents = ["#ff6b35", "#00d4ff", "#a855f7", "#10b981", "#ffd700"]
    for i in range(count):
        accent = accents[i % len(accents)]
        v_prompt = prompt + f"\n\nVariation {i+1}: Use {accent} as accent. Make distinctly different layout."
        try:
            html = generate_design(v_prompt, api_key)
            variations.append({"accent": accent, "html": html, "index": i+1})
            print(f"  Variation {i+1} generated (accent: {accent})")
        except Exception as e:
            variations.append({"accent": accent, "html": None, "index": i+1, "error": str(e)})
            print(f"  Variation {i+1} failed: {e}")
        if i < count - 1:
            time.sleep(3)
    return variations


def save_html(html, output_path):
    d = os.path.dirname(output_path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stitch by Google - Cinematic Web Design Generator")
    parser.add_argument("prompt", nargs="?", default="Create a premium dark cinematic landing page")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--refine", help="Refine existing HTML file")
    parser.add_argument("--instructions", default="Improve the design")
    parser.add_argument("--variations", "-n", type=int, default=1)
    parser.add_argument("--temperature", type=float, default=0.85)
    parser.add_argument("--api-key", help="Override STITCH_API_KEY env var")
    parser.add_argument("--interactive", action="store_true")
    
    args = parser.parse_args()
    api_key = args.api_key or STITCH_API_KEY
    
    try:
        if args.interactive:
            print("Stitch by Google - Interactive Mode (type 'quit' to exit)")
            while True:
                prompt = input("Prompt: ").strip()
                if prompt.lower() in ("quit", "q"):
                    break
                output = input("Output (or Enter for auto): ").strip()
                if not output:
                    output = f"output/stitch_{int(time.time())}.html"
                html = generate_design(prompt, api_key)
                save_html(html, output)
                print(f"Saved: {output}\n")
        elif args.refine:
            with open(args.refine, "r") as f:
                html = f.read()
            result = refine_design(html, args.instructions, api_key)
            output = args.output or args.refine.replace(".html", "_refined.html")
            save_html(result, output)
            print(f"Refined design saved: {output}")
        elif args.variations > 1:
            print(f"Generating {args.variations} variations...")
            variations = generate_variations(args.prompt, args.variations, api_key)
            for v in variations:
                if v["html"]:
                    path = (args.output or "output/design.html").replace(".html", f"_v{v['index']}.html")
                    save_html(v["html"], path)
                    print(f"  Saved: {path}")
        else:
            html = generate_design(args.prompt, api_key, temperature=args.temperature)
            if args.output:
                save_html(html, args.output)
                print(f"Design saved: {args.output}")
            else:
                print(html)
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e}", file=sys.stderr)
        if e.response is not None:
            print(f"Response: {e.response.text[:500]}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
