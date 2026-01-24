# Meta Creative AI Generation

AI-powered automation for generating Meta ad creatives at scale.

## 🎨 Features

- **AI Creative Generation** - Generate ad creatives using Gemini Enterprise/DALL-E 3
- **Bulk Ad Creation** - Create hundreds of ad variations
- **Multi-platform Publishing** - Publish to Facebook, Instagram, WhatsApp
- **Creative Testing Automation** - A/B test variations automatically
- **Performance Tracking** - Track which creatives perform best
- **Copy Optimization** - AI-generated copy for different audiences

## 🚀 Quick Start

```bash
pip install -r requirements.txt
export GEMINI_API_KEY=your_key
python generate_creatives.py --account-id YOUR_ACCOUNT_ID --count 50
```

## 📚 Documentation

### Generate Creatives

```python
from scripts.generate_creatives import CreativeGenerator

generator = CreativeGenerator(account_id='YOUR_ACCOUNT_ID')
creatives = generator.generate_variations(
    product='Summer Collection',
    audience='Women 25-40',
    count=50,
    format=['carousel', 'single_image', 'video']
)
```

### Create Ads

```python
from scripts.create_ads import AdCreator

creator = AdCreator(account_id='YOUR_ACCOUNT_ID')
creator.bulk_create_ads(
    campaign_id='CAMPAIGN_ID',
    creatives=creatives,
    targeting={'age_min': 25, 'age_max': 40}
)
```

## 🔧 Configuration

Create `.env` file:

```env
FACEBOOK_ACCESS_TOKEN=your_token
GEMINI_API_KEY=your_gemini_key
DOWNLOAD_URL=your_download_url
IMAGE_STORAGE_PATH=./images
```

## 📊 Usage Examples

### Example 1: Generate 100 Product Ads

```bash
python scripts/generate_creatives.py \
  --account-id 12345 \
  --product "iPhone 15" \
  --count 100 \
  --format single_image,carousel
```

### Example 2: A/B Test Creatives

```bash
python scripts/ab_test_creatives.py \
  --campaign-id 67890 \
  --variants 5 \
  --test-duration 7
```

## 🌐 Supported Formats

- Single Image Ads
- Carousel Ads
- Video Ads
- Collection Ads
- Slideshow Ads

## 🎯 Integration

- **n8n Pro**: Schedule daily creative generation
- **Zapier Max**: Automate ad publishing workflow
- **Gemini Enterprise**: AI copy and image generation
- **Google Sheets**: Track creative performance

## 📝 License

MIT
