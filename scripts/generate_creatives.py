#!/usr/bin/env python3
"""
Generate ad creatives using Google Gemini API.

Usage:
    python scripts/generate_creatives.py --brand "Nike" --product "Running Shoes" --tone "energetic" --count 3
"""

import argparse
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def generate_creatives(brand, product, tone, count=3):
    """
    Generate creative ad copy using Gemini API.
    
    Args:
        brand (str): Brand name
        product (str): Product description
        tone (str): Tone of voice (energetic, professional, casual, luxury)
        count (int): Number of creatives to generate
    """
    try:
        print(f"\nGenerating {count} creative variations for {brand} {product}...")
        print(f"{"="*80}")
        print(f"NOTE: Using template data. Connect Gemini API for AI-generated creatives.")
        print(f"{"="*80}\n")
        
        creatives = []
        tones_descriptions = {
            'energetic': 'fast-paced, exciting, action-oriented',
            'professional': 'formal, authoritative, trustworthy',
            'casual': 'friendly, conversational, approachable',
            'luxury': 'premium, exclusive, high-end',
        }
        
        tone_desc = tones_descriptions.get(tone, tone)
        
        for i in range(count):
            creative = {
                'id': f"creative_{i+1}",
                'headline': f"{brand} {product} - Transform Your Performance #Variant{i+1}",
                'description': f"Experience premium {product.lower()} designed for champions. Limited time offer. Shop now and save 20%.",
                'cta': "Shop Now",
                'tone': tone,
                'character_count_headline': len(f"{brand} {product} - Transform Your Performance #Variant{i+1}"),
            }
            creatives.append(creative)
            
            print(f"Creative {i+1}:")
            print(f"  Headline: {creative['headline']}")
            print(f"  Description: {creative['description']}")
            print(f"  CTA: {creative['cta']}")
            print(f"  Tone: {tone_desc}")
            print('-' * 80)
        
        return creatives
    
    except Exception as e:
        print(f'Error generating creatives: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate ad creatives using AI')
    parser.add_argument('--brand', required=True, help='Brand name')
    parser.add_argument('--product', required=True, help='Product description')
    parser.add_argument('--tone', default='energetic', help='Tone of voice (energetic, professional, casual, luxury)')
    parser.add_argument('--count', type=int, default=3, help='Number of creatives to generate')
    args = parser.parse_args()
    
    generate_creatives(args.brand, args.product, args.tone, args.count)
