#!/usr/bin/env python3
"""
nanobanana_generate.py — Generador de imagenes con Nano Banana (Gemini Image API)

Uso:
    export STITCH_API_KEY="your-key"
    python nanobanana_generate.py "Dark cinematic hero background" -o hero.png
    python nanobanana_generate.py --batch assets.json
"""

import requests, json, sys, argparse, os, base64, time

# Leer API key de variable de entorno
NANOBANANA_API_KEY = os.environ.get("STITCH_API_KEY", "")
MODEL = "gemini-2.0-flash-exp-image-generation"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def generate_image(prompt, api_key=None, aspect_ratio="16:9", image_size="1K"):
    """Genera una imagen usando Nano Banana (Gemini Image Generation)."""
    key = api_key or NANOBANANA_API_KEY
    if not key:
        raise ValueError("STITCH_API_KEY not set. Run: export STITCH_API_KEY='your-key'")
    
    full_prompt = f"Generate an image: {prompt}\n\nTechnical: aspect ratio {aspect_ratio}, quality high, web-ready, premium professional style."
    
    response = requests.post(
        f"{ENDPOINT}?key={key}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {
                "temperature": 0.9, "topP": 0.95,
                "responseModalities": ["TEXT", "IMAGE"],
                "imageConfig": {"aspectRatio": aspect_ratio, "imageSize": image_size}
            }
        },
        timeout=120
    )
    response.raise_for_status()
    return response.json()


def save_image_from_response(data, output_path):
    """Extrae y guarda la imagen de la respuesta."""
    candidates = data.get("candidates", [])
    if not candidates:
        raise ValueError(f"No candidates: {json.dumps(data, indent=2)[:500]}")
    
    for part in candidates[0]["content"]["parts"]:
        if "inlineData" in part:
            image_data = part["inlineData"]["data"]
            mime_type = part["inlineData"]["mimeType"]
            image_bytes = base64.b64decode(image_data)
            
            ext = ".png" if "png" in mime_type else ".jpg"
            if not output_path.endswith((".png", ".jpg", ".jpeg", ".webp")):
                output_path += ext
            
            d = os.path.dirname(output_path)
            if d:
                os.makedirs(d, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            return output_path
    
    raise ValueError("No image data found in response")


def generate_asset_batch(asset_list, output_dir="assets", api_key=None):
    """Genera un batch de assets."""
    results = {}
    os.makedirs(output_dir, exist_ok=True)
    
    for i, asset in enumerate(asset_list):
        prompt = asset["prompt"]
        output = os.path.join(output_dir, asset.get("output", f"asset_{i+1}.png"))
        ratio = asset.get("aspect_ratio", "16:9")
        
        print(f"Generating asset {i+1}/{len(asset_list)}: {output}...")
        try:
            data = generate_image(prompt, api_key, ratio)
            saved = save_image_from_response(data, output)
            results[saved] = "Success"
            print(f"  Saved: {saved}")
        except Exception as e:
            results[output] = f"Error: {e}"
            print(f"  Error: {e}")
        
        if i < len(asset_list) - 1:
            time.sleep(2)
    
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nano Banana - Image Generation for Web Design")
    parser.add_argument("prompt", nargs="?", help="Image generation prompt")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--aspect-ratio", default="16:9", help="Aspect ratio")
    parser.add_argument("--size", default="1K", help="Image size")
    parser.add_argument("--variations", "-n", type=int, default=1)
    parser.add_argument("--batch", help="JSON file with asset list")
    parser.add_argument("--api-key", help="Override STITCH_API_KEY env var")
    parser.add_argument("--interactive", action="store_true")
    
    args = parser.parse_args()
    api_key = args.api_key or NANOBANANA_API_KEY
    
    try:
        if args.batch:
            with open(args.batch, "r") as f:
                asset_list = json.load(f)
            results = generate_asset_batch(asset_list, api_key=api_key)
            print("\nBatch Results:")
            for path, status in results.items():
                print(f"  {status} {path}")
        elif args.interactive:
            print("Nano Banana - Interactive Mode (type 'quit' to exit)")
            while True:
                prompt = input("Prompt: ").strip()
                if prompt.lower() in ("quit", "q"):
                    break
                output = input("Output (or Enter for auto): ").strip()
                if not output:
                    output = f"assets/nanobanana_{int(time.time())}.png"
                ratio = input("Aspect ratio (16:9, 1:1, 9:16) [16:9]: ").strip() or "16:9"
                print("Generating...")
                try:
                    data = generate_image(prompt, api_key, ratio)
                    saved = save_image_from_response(data, output)
                    print(f"Saved: {saved}\n")
                except Exception as e:
                    print(f"Error: {e}\n")
        elif args.prompt:
            for i in range(args.variations):
                output = args.output
                if args.variations > 1 and output:
                    base, ext = os.path.splitext(output)
                    output = f"{base}_{i+1}{ext}"
                print(f"Generating ({i+1}/{args.variations})...")
                data = generate_image(args.prompt, api_key, args.aspect_ratio)
                saved = save_image_from_response(data, output or "output.png")
                print(f"Saved: {saved}")
                if i < args.variations - 1:
                    time.sleep(2)
        else:
            parser.print_help()
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e}", file=sys.stderr)
        if e.response is not None:
            print(f"Response: {e.response.text[:500]}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
