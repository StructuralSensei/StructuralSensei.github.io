#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate individual app landing pages from apps.json
Run: python generate_apps.py
"""

import json
import os
from pathlib import Path

def generate_app_page(app):
    """Generate HTML for a single app landing page"""

    app_id = app['id']
    name = app['name']
    tagline = app['tagline']
    description = app['description']
    price = app['price']
    gumroad = app['gumroad']
    features = app.get('features', [])
    faq = app.get('faq', [])
    category = app.get('category', 'tools')
    demo_gif = app.get('demo_gif', '')  # Optional demo GIF

    # Generate demo GIF HTML
    if demo_gif:
        demo_gif_html = f'<img src="{demo_gif}" alt="{name} demo" class="w-full h-full object-cover">'
    else:
        demo_gif_html = f"""<div class="text-center text-gray-400 p-12">
                <p class="text-lg font-semibold mb-2">Demo video coming soon</p>
                <p class="text-sm">Use ScreenToGif to create a GIF, then add the path to apps.json</p>
                <p class="text-xs mt-4 text-gray-500">Expected dimensions: 1200x675 (or any 16:9 ratio)</p>
            </div>"""

    # Generate features HTML
    features_html = ""
    for i, feature in enumerate(features, 1):
        features_html += f"""
        <div class="flex gap-3">
          <div class="icon-tile flex-shrink-0 w-6 h-6 flex items-center justify-center text-white text-sm font-bold">
            {i}
          </div>
          <p class="text-gray-300">{feature}</p>
        </div>
        """

    # Generate FAQ HTML
    faq_html = ""
    for qa in faq:
        faq_html += f"""
        <div class="border-b border-gray-700 pb-4">
          <h3 class="text-lg font-semibold text-white mb-2">{qa['q']}</h3>
          <p class="text-gray-400">{qa['a']}</p>
        </div>
        """

    # Price display
    if price > 0:
        price_display = f"${price:.2f}"
        cta_text = f"Get {name} — ${price:.2f}"
    else:
        price_display = "Free"
        cta_text = f"Get {name} — Free"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#050505">
    <title>{name} — {tagline} | Structural Sensei</title>
    <meta name="description" content="{description}">
    <meta property="og:title" content="{name}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://structuralsensei.cc/{app_id}/">
    <meta property="og:image" content="https://structuralsensei.cc/assets/logo.png">
    <link rel="icon" type="image/png" href="/assets/logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="/assets/tailwind-brand.js"></script>
    <link rel="stylesheet" href="/assets/brand.css">
</head>
<body class="antialiased">
    <!-- Navigation -->
    <nav class="sticky top-0 z-40 bg-gray-950/80 backdrop-blur border-b border-gray-900">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <a href="/" class="brand-lockup">
                <img src="/assets/logo.png" alt="Structural Sensei logo">
                <span class="brand-name">Structural <em>Sensei</em></span>
            </a>
            <a href="/#apps" class="text-gray-400 hover:text-white transition">Back to Apps</a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative py-16 sm:py-24 overflow-hidden">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="inline-block mb-4">
                <span class="inline-block px-3 py-1 bg-blue-500/20 text-blue-300 rounded-full text-sm font-medium">
                    {category.title()}
                </span>
            </div>

            <h1 class="text-4xl sm:text-5xl font-bold text-white mb-4 leading-tight">
                {name}
            </h1>
            <p class="text-xl text-gray-400 mb-8">
                {tagline}
            </p>
            <p class="text-gray-300 max-w-2xl mx-auto mb-10 text-lg">
                {description}
            </p>

            <!-- Price & CTA -->
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-8">
                <a href="{gumroad}" target="_blank" class="gradient-accent text-white font-semibold py-3 px-8 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition duration-300 inline-block">
                    {cta_text}
                </a>
                <a href="{gumroad}" target="_blank" class="text-blue-400 hover:text-blue-300 font-medium transition">
                    View on Gumroad
                </a>
            </div>
        </div>
    </section>

    <!-- Demo GIF Section -->
    <section class="py-16 bg-gray-900/50 border-y border-gray-900">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-white mb-8 text-center">
                See It in Action
            </h2>
            <div class="bg-gray-800 rounded-xl overflow-hidden border border-gray-700 aspect-video flex items-center justify-center">
                {demo_gif_html}
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="py-16 bg-gray-900/50 border-y border-gray-900">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-white mb-12 text-center">
                What's Included
            </h2>
            <div class="grid sm:grid-cols-2 gap-8">
                {features_html}
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-white mb-12 text-center">
                Questions?
            </h2>
            <div class="space-y-6 max-w-3xl mx-auto">
                {faq_html}
            </div>
        </div>
    </section>

    <!-- CTA Footer -->
    <section class="py-16 bg-gray-900/50 border-t border-gray-900">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-2xl sm:text-3xl font-bold text-white mb-6">
                Ready to get {name}?
            </h2>
            <p class="text-gray-400 mb-8 max-w-2xl mx-auto">
                Download now and unlock a more efficient workflow.
            </p>
            <a href="{gumroad}" target="_blank" class="gradient-accent text-white font-semibold py-3 px-8 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition duration-300 inline-block">
                {cta_text}
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-gray-900 bg-gray-950 py-8">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col sm:flex-row justify-between items-center gap-4">
                <p class="text-gray-500 text-sm">© 2026 Structural Sensei. All rights reserved.</p>
                <div class="flex gap-6 text-sm text-gray-500">
                    <a href="/privacy.html" class="hover:text-gray-300 transition">Privacy</a>
                    <a href="https://www.structuralsensei.cc" class="hover:text-gray-300 transition">Main Site</a>
                    <a href="https://www.youtube.com" class="hover:text-gray-300 transition">YouTube</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    return html

def main():
    # Read apps.json
    with open('apps.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create apps directory if it doesn't exist
    Path('apps').mkdir(exist_ok=True)

    # Generate a page for each app
    for app in data['apps']:
        app_id = app['id']
        app_dir = Path(f'apps/{app_id}')
        app_dir.mkdir(exist_ok=True)

        html = generate_app_page(app)

        with open(app_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"Generated: apps/{app_id}/index.html")

    print(f"\nSuccessfully generated {len(data['apps'])} app pages!")

if __name__ == '__main__':
    main()
