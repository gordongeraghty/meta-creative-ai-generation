# Meta Creative AI Generation

AI-powered creative generation and bulk ad creation for Meta platforms using Google Gemini and Facebook Business SDK.

## Features

- **AI Creative Generation** - Generate ad copy variations using Gemini API
- **Tone-Based Customization** - Create creatives with specific tones (energetic, professional, casual, luxury)
- **Bulk Ad Creation** - Create multiple ads from generated creatives
- **Creative Testing** - Test generation pipeline with sample data
- **JSON Configuration** - Manage creatives via JSON files
- **Error Handling** - Robust error handling and retry logic

---

## Prerequisites

### Required

- **Python 3.11+**
- **pip** (Python package manager)
- **Google Gemini API Key** (for AI creative generation)
 - Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Meta Business Account** with Ads Manager access
- **Facebook Access Token** with `ads_management` permission

### API Credentials Setup

1. **Google Gemini API Key**:
 - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
 - Click "Create API Key"
 - Copy the key and store in `.env`

2. **Meta Credentials**:
 - Business Account ID: [Meta Ads Manager](https://adsmanager.facebook.com/)
 - Access Token: [Meta Apps Dashboard](https://developers.facebook.com/apps/)

---

## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/gordongeraghty/meta-creative-ai-generation.git
cd meta-creative-ai-generation
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env` file:

```bash
cp .env.example .env
```

Edit `.env`:

```env
FACEBOOK_ACCESS_TOKEN=your_access_token
FACEBOOK_BUSINESS_ACCOUNT_ID=ACT_1234567890
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Verify Installation

```bash
python scripts/test_creative_generation.py
```

---

## Per-Script Usage Examples

### Script 1: `generate_creatives.py` - AI Creative Generation

**Purpose**: Generate ad copy variations using AI with specific tone and style.

**Command**:

```bash
python scripts/generate_creatives.py --brand "Nike" --product "Running Shoes" --tone "energetic" --count 3
```

**Parameters**:

- `--brand` (required): Brand name
- `--product` (required): Product description
- `--tone` (optional): Tone of voice - `energetic`, `professional`, `casual`, `luxury` (default: `energetic`)
- `--count` (optional): Number of creative variations to generate (default: 3)

**Example Commands**:

```bash
# Generate 3 energetic creatives for Nike Running Shoes
python scripts/generate_creatives.py --brand "Nike" --product "Running Shoes" --tone "energetic" --count 3

# Generate 5 professional creatives for Apple iPhone
python scripts/generate_creatives.py --brand "Apple" --product "iPhone 15" --tone "professional" --count 5

# Generate 2 luxury creatives for Louis Vuitton bags
python scripts/generate_creatives.py --brand "Louis Vuitton" --product "Leather Bag" --tone "luxury" --count 2
```

**Expected Output**:

```
Generating 3 creative variations for Nike Running Shoes...

================================================================================
Creative 1:
 Headline: Nike Running Shoes - Transform Your Performance #Variant1
 Description: Experience premium running shoes designed for champions. Limited time offer. Shop now and save 20%.
 CTA: Shop Now
 Tone: fast-paced, exciting, action-oriented
--------------------------------------------------------------------------------
Creative 2:
 Headline: Nike Running Shoes - Transform Your Performance #Variant2
 Description: Experience premium running shoes designed for champions. Limited time offer. Shop now and save 20%.
 CTA: Shop Now
 Tone: fast-paced, exciting, action-oriented
--------------------------------------------------------------------------------
Creative 3:
 Headline: Nike Running Shoes - Transform Your Performance #Variant3
 Description: Experience premium running shoes designed for champions. Limited time offer. Shop now and save 20%.
 CTA: Shop Now
 Tone: fast-paced, exciting, action-oriented
================================================================================
```

**Tone Descriptions**:

| Tone | Description | Best For |
|------|-------------|----------|
| `energetic` | Fast-paced, exciting, action-oriented | Sports, tech, youth brands |
| `professional` | Formal, authoritative, trustworthy | B2B, finance, enterprise |
| `casual` | Friendly, conversational, approachable | Lifestyle, social, casual brands |
| `luxury` | Premium, exclusive, high-end | Fashion, jewelry, luxury goods |

---

### Script 2: `batch_create_ads.py` - Bulk Ad Creation

**Purpose**: Create multiple ads in Meta Ads Manager from generated creatives.

**Command**:

```bash
python scripts/batch_create_ads.py --account-id ACT_1234567890 --adset-id 123456789012345 --creatives creatives.json
```

**Parameters**:

- `--account-id` (required): Meta Business Account ID
- `--adset-id` (required): Ad Set ID (where ads will be created)
- `--creatives` (required): Path to JSON file with creative definitions

**Creatives JSON Format** (`creatives.json`):

```json
[
 {
 "id": "creative_1",
 "headline": "Nike Running Shoes - Transform Your Performance",
 "description": "Experience premium running shoes. Limited offer. Save 20%.",
 "cta": "Shop Now",
 "tone": "energetic"
 },
 {
 "id": "creative_2",
 "headline": "Nike Running Shoes - Designed for Champions",
 "description": "Premium quality guaranteed. Free shipping on orders over $100.",
 "cta": "Explore",
 "tone": "energetic"
 },
 {
 "id": "creative_3",
 "headline": "Nike Running Shoes - Limited Time Offer",
 "description": "Get the latest Nike running shoes with exclusive pricing.",
 "cta": "Learn More",
 "tone": "energetic"
 }
]
```

**Example Command**:

```bash
python scripts/batch_create_ads.py --account-id ACT_1234567890 --adset-id 123456789012345 --creatives creatives.json
```

**Expected Output**:

```
Creating 3 ads in AdSet 123456789012345...

================================================================================
Creating Ad 1: Nike Running Shoes - Transform Your Performance_1
 Headline: Nike Running Shoes - Transform Your Performance
 Description: Experience premium running shoes. Limited offer. Save 20%.
 CTA: Shop Now
- Ad created (status: PAUSED)

Creating Ad 2: Nike Running Shoes - Designed for Champions_2
 Headline: Nike Running Shoes - Designed for Champions
 Description: Premium quality guaranteed. Free shipping on orders over $100.
 CTA: Explore
- Ad created (status: PAUSED)

Creating Ad 3: Nike Running Shoes - Limited Time Offer_3
 Headline: Nike Running Shoes - Limited Time Offer
 Description: Get the latest Nike running shoes with exclusive pricing.
 CTA: Learn More
- Ad created (status: PAUSED)

================================================================================
Summary: 3 ads created, 0 errors
```

---

### Script 3: `test_creative_generation.py` - Test Pipeline

**Purpose**: Test creative generation pipeline with sample data.

**Command**:

```bash
python scripts/test_creative_generation.py
```

**Parameters**: None (uses built-in test cases)

**Expected Output**:

```
================================================================================
CREATIVE GENERATION TEST
================================================================================

Test Case 1: Nike - Running Shoes
Tone: energetic

 Creative ID: test_creative_1_1
 Headline: Nike Running Shoes - Discover Excellence
 Description: Experience the latest running shoes innovation. Premium quality guaranteed.
 CTA: Explore
--------------------------------------------------------------------------------
 Creative ID: test_creative_1_2
 Headline: Nike Running Shoes - Limited Offer
 Description: Get running shoes with special pricing. Offer ends soon!
 CTA: Learn More
--------------------------------------------------------------------------------
Test Case 2: Apple - iPhone 15
Tone: professional

 Creative ID: test_creative_2_1
 Headline: Apple iPhone 15 - Discover Excellence
 Description: Experience the latest iPhone 15 innovation. Premium quality guaranteed.
 CTA: Explore
 ...
- Test complete. Generated 6 creatives.
- Results saved to: test_creatives_output.json
```

**Output Files**:
- `test_creatives_output.json` - Generated test creatives in JSON format

---

## Configuration

### Environment Variables

Create `.env` in repository root:

```env
# Meta Credentials
FACEBOOK_ACCESS_TOKEN=your_access_token
FACEBOOK_BUSINESS_ACCOUNT_ID=ACT_1234567890

# Gemini API
GEMINI_API_KEY=your_gemini_api_key

# Optional
LOG_LEVEL=INFO
GEMINI_MODEL=gemini-pro # or gemini-pro-vision for image analysis
```

### .env.example Template

```env
# Meta Business Credentials
FACEBOOK_ACCESS_TOKEN=your_token_here
FACEBOOK_BUSINESS_ACCOUNT_ID=ACT_your_account_id_here

# Google Gemini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-pro

# Configuration
CREATIVE_GENERATION_TEMPERATURE=0.7
CREATIVE_GENERATION_MAX_TOKENS=500
```

---

## Security Best Practices

1. **Never commit `.env`** - Keep API keys private
 ```bash
 echo '.env' >> .gitignore
 ```

2. **Rotate API Keys** - Regenerate keys every 90 days

3. **Use Minimal Scopes** - Only request necessary permissions

4. **Monitor Usage** - Track API usage in Gemini dashboard

5. **Implement Rate Limiting** - Prevent excessive API calls

---

## Troubleshooting

### Error: `GEMINI_API_KEY not found`

**Solution**: Add API key to `.env`:

```bash
echo 'GEMINI_API_KEY=your_key' >> .env
```

### Error: `Invalid API key`

**Solution**:
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Regenerate API key
3. Update `.env`

### Error: `Quota exceeded`

**Solution**:
- Gemini API has usage limits
- Check [Google AI Studio](https://makersuite.google.com/) for quota status
- Upgrade plan if needed

### Error: `facebook_business module not found`

**Solution**:

```bash
pip install facebook_business
```

---

## Links to Official Documentation

- **[Google Gemini API](https://ai.google.dev/docs)** - Gemini API documentation
- **[Gemini Python SDK](https://github.com/google/generative-ai-python)** - Python SDK
- **[Facebook Business SDK](https://developers.facebook.com/docs/business-sdk)** - Meta SDK docs
- **[Marketing API Reference](https://developers.facebook.com/docs/marketing-api)** - Ad creation API
- **[Meta Ads Manager Help](https://www.facebook.com/business/help/)** - Official Meta help

---

## Related Repositories

- **[meta-campaign-management](https://github.com/gordongeraghty/meta-campaign-management)** - Campaign CRUD operations
- **[meta-competitor-intelligence](https://github.com/gordongeraghty/meta-competitor-intelligence)** - Competitor monitoring
- **[n8n-meta-ads-workflows](https://github.com/gordongeraghty/n8n-meta-ads-workflows)** - n8n automation
- **[empire-amplify-ads-automation](https://github.com/gordongeraghty/empire-amplify-ads-automation)** - Master hub

---

## licence

MIT licence - See licence file

## Author

Gordon Geraghty - Head of Performance Media, Empire Amplify
