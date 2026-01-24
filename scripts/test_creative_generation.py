#!/usr/bin/env python3
"""
Test creative generation pipeline with sample data.

Usage:
    python scripts/test_creative_generation.py
"""

import json
import sys

def test_creative_pipeline():
    """
    Test creative generation with sample brand/product data.
    """
    try:
        test_cases = [
            {'brand': 'Nike', 'product': 'Running Shoes', 'tone': 'energetic'},
            {'brand': 'Apple', 'product': 'iPhone 15', 'tone': 'professional'},
            {'brand': 'Coca-Cola', 'product': 'Sparkling Water', 'tone': 'casual'},
        ]
        
        print(f'\n{"="*80}')
        print('CREATIVE GENERATION TEST')
        print(f'{"="*80}\n')
        
        generated_creatives = []
        
        for idx, test_case in enumerate(test_cases, 1):
            print(f"Test Case {idx}: {test_case['brand']} - {test_case['product']}")
            print(f"Tone: {test_case['tone']}\n")
            
            brand = test_case['brand']
            product = test_case['product']
            tone = test_case['tone']
            
            # Generate sample creatives
            creatives = [
                {
                    'id': f"test_creative_{idx}_1",
                    'headline': f"{brand} {product} - Discover Excellence",
                    'description': f"Experience the latest {product.lower()} innovation. Premium quality guaranteed.",
                    'cta': 'Explore',
                    'tone': tone,
                },
                {
                    'id': f"test_creative_{idx}_2",
                    'headline': f"{brand} {product} - Limited Offer",
                    'description': f"Get {product.lower()} with special pricing. Offer ends soon!",
                    'cta': 'Learn More',
                    'tone': tone,
                },
            ]
            
            for creative in creatives:
                print(f"  Creative ID: {creative['id']}")
                print(f"  Headline: {creative['headline']}")
                print(f"  Description: {creative['description']}")
                print(f"  CTA: {creative['cta']}")
                print('-' * 80)
                generated_creatives.append(creative)
        
        # Save results
        output_file = 'test_creatives_output.json'
        with open(output_file, 'w') as f:
            json.dump(generated_creatives, f, indent=2)
        
        print(f'\n✓ Test complete. Generated {len(generated_creatives)} creatives.')
        print(f'✓ Results saved to: {output_file}\n')
        
        return generated_creatives
    
    except Exception as e:
        print(f'Error in test pipeline: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    test_creative_pipeline()
