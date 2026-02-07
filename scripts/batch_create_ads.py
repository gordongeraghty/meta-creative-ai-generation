#!/usr/bin/env python3
"""
Create multiple ads in Meta from generated creatives.

Usage:
    python scripts/batch_create_ads.py --account-id ACT_1234567890 --adset-id 123456789 --creatives creatives.json
"""

import argparse
import json
import os
import sys
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adset import AdSet

load_dotenv()

def batch_create_ads(account_id, adset_id, creatives_file):
    """
    Create multiple ads from generated creatives.
    
    Args:
        account_id (str): Meta Business Account ID
        adset_id (str): Ad Set ID where ads will be created
        creatives_file (str): Path to JSON file with creative definitions
    """
    try:
        access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        if not access_token:
            raise ValueError('FACEBOOK_ACCESS_TOKEN not found in .env')
        
        with open(creatives_file, 'r') as f:
            creatives = json.load(f)
        
        if not isinstance(creatives, list):
            raise ValueError('creatives_file must contain a JSON array')
        
        FacebookAdsApi.init(access_token=access_token)
        
        created_ads = []
        errors = []
        
        print(f'\nCreating {len(creatives)} ads in AdSet {adset_id}...\n')
        print(f'{"="*80}')
        
        for idx, creative in enumerate(creatives, 1):
            try:
                # Note: This requires adcreative object and additional setup
                # Simplified example - implement full Ad creation in production
                
                ad_data = {
                    'name': f"{creative.get('headline', 'Ad')}_{idx}",
                    'adset_id': adset_id,
                    'status': 'PAUSED',
                }
                
                print(f"Creating Ad {idx}: {ad_data['name']}")
                print(f"  Headline: {creative.get('headline', 'N/A')}")
                print(f"  Description: {creative.get('description', 'N/A')}")
                print(f"  CTA: {creative.get('cta', 'N/A')}")
                
                # TODO: Uncomment below to create real ads via Meta API
                # ad = Ad(adset_id).create(ad_data)
                # created_ads.append(ad)

                created_ads.append(ad_data)
                print(f"  [DRY RUN] Ad prepared but NOT created in Meta (API call not yet active)\n")
            
            except Exception as e:
                error_msg = f"✗ Failed to create ad {idx}: {str(e)}"
                errors.append(error_msg)
                print(error_msg, file=sys.stderr)
        
        print(f'{"="*80}')
        print(f'Summary: {len(created_ads)} ads prepared (dry run), {len(errors)} errors\n')
        
        if errors:
            sys.exit(1)
        
        return created_ads
    
    except FileNotFoundError:
        print(f'Error: Creatives file not found: {creatives_file}', file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f'Error parsing JSON: {e}', file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f'Configuration Error: {e}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'Error creating ads: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch create ads from creatives')
    parser.add_argument('--account-id', required=True, help='Meta Business Account ID')
    parser.add_argument('--adset-id', required=True, help='Ad Set ID for ad creation')
    parser.add_argument('--creatives', required=True, help='Path to creatives JSON file')
    args = parser.parse_args()
    
    batch_create_ads(args.account_id, args.adset_id, args.creatives)
