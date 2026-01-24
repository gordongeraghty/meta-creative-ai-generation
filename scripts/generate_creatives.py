#!/usr/bin/env python3
"""
AI-powered creative generation for Meta ads.
"""

import os
import sys
import argparse
import json
from typing import List, Dict
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class CreativeGenerator:
    def __init__(self, account_id: str, gemini_api_key: str = None):
        self.account_id = account_id
        self.gemini_api_key = gemini_api_key or os.getenv('GEMINI_API_KEY')
        
        if self.gemini_api_key:
            genai.configure(api_key=self.gemini_api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
    
    def generate_copy(self, product: str, audience: str, hook_type: str = 'urgency') -> str:
        """
        Generate ad copy using Gemini.
        """
        if not self.model:
            return f"Check out {product} today!"
        
        prompt = f"""
        Generate a compelling {hook_type} hook for a Meta ad.
        Product: {product}
        Target Audience: {audience}
        
        Requirements:
        - Max 125 characters
        - Include call-to-action
        - Create urgency or curiosity
        - Be specific and benefit-focused
        
        Return ONLY the ad copy, no explanation.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"ERROR: {str(e)}")
            return None
    
    def generate_variations(self, product: str, audience: str, count: int = 10, 
                           formats: List[str] = None) -> List[Dict]:
        """
        Generate multiple creative variations.
        """
        if formats is None:
            formats = ['single_image', 'carousel']
        
        hook_types = ['urgency', 'curiosity', 'emotion', 'benefit', 'social_proof']
        creatives = []
        
        for i in range(count):
            hook_type = hook_types[i % len(hook_types)]
            
            creative = {
                'variation_id': f"v_{i+1}",
                'product': product,
                'audience': audience,
                'hook_type': hook_type,
                'format': formats[i % len(formats)],
                'copy': self.generate_copy(product, audience, hook_type),
                'status': 'generated'
            }
            
            creatives.append(creative)
        
        return creatives

def main():
    parser = argparse.ArgumentParser(description='Generate Meta ad creatives with AI')
    parser.add_argument('--account-id', required=True, help='Meta Ad Account ID')
    parser.add_argument('--product', required=True, help='Product or service name')
    parser.add_argument('--audience', required=True, help='Target audience description')
    parser.add_argument('--count', type=int, default=10, help='Number of variations')
    parser.add_argument('--format', default='single_image,carousel', help='Ad formats')
    parser.add_argument('--output', default='generated_creatives.json', help='Output file')
    
    args = parser.parse_args()
    
    print(f"\n🎨 Generating {args.count} creative variations")
    print("="*60)
    
    generator = CreativeGenerator(args.account_id)
    formats = args.format.split(',')
    
    creatives = generator.generate_variations(
        product=args.product,
        audience=args.audience,
        count=args.count,
        formats=formats
    )
    
    # Save to JSON
    with open(args.output, 'w') as f:
        json.dump(creatives, f, indent=2)
    
    print(f"\n✅ Generated {len(creatives)} creatives")
    print(f"📁 Saved to: {args.output}")
    
    # Print summary
    for creative in creatives[:3]:
        print(f"\n  {creative['variation_id']}: {creative['copy']}")
    
    if len(creatives) > 3:
        print(f"\n  ... and {len(creatives) - 3} more variations")

if __name__ == '__main__':
    main()
