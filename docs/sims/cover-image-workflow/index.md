# Cover Image Generation Workflow

This interactive flowchart shows the decision tree for generating book cover images using the `generate-cover.sh` script. The workflow adapts based on your available resources: OpenAI API billing, ChatGPT Pro subscription, and operating system.

<iframe src="./main.html" width="100%" height="600px" scrolling="no" style="border: none;"></iframe>

[View Fullscreen](./main.html){ .md-button .md-button--primary }

## Overview

The cover image generation script supports three modes of operation:

1. **Full Auto Mode** - Requires OpenAI API with active billing
2. **Local Prompt + Browser Mode** - Requires ChatGPT Pro and macOS
3. **Local Prompt + Manual Mode** - Requires ChatGPT Pro (any OS)

## Decision Points

### HAS_OPENAI_API_KEY

Checks if the `OPENAI_API_KEY` environment variable is set. This is required for any API-based operations.

```bash
export OPENAI_API_KEY='your-key-here'
```

### API Billing Active

Even with a valid API key, your OpenAI account must have active billing enabled. The script tests this by making a simple API call.

- **If billing is active**: Use full auto mode for seamless image generation
- **If billing is not active**: Fall back to ChatGPT Pro workflow

### HAS_CHATGPT_PRO

ChatGPT Pro/Plus subscription ($20/month) allows you to generate images through the ChatGPT interface. This is separate from API billing.

### ON_MACOS

The `--open-browser` flag uses AppleScript to automate browser interaction, which only works on macOS.

## Usage Commands

### Full Auto Mode (API billing required)
```bash
./generate-cover.sh
```

### Local Prompt with Browser Automation (macOS + ChatGPT Pro)
```bash
./generate-cover.sh --open-browser
```

### Local Prompt Only (ChatGPT Pro, any OS)
```bash
./generate-cover.sh --local-prompt
```

## Output

All modes produce a cover image saved to:
```
docs/img/cover.png
```

**Specifications:**
- Size: 1200x630 pixels
- Aspect Ratio: 1.91:1 (Open Graph standard)
- Format: PNG

## Related Resources

- [Image Generation README](https://github.com/dmccreary/ibook-skills/tree/main/src/image-generation)
- [OpenAI Billing Setup](https://platform.openai.com/account/billing)
- [ChatGPT Plus](https://openai.com/chatgpt/pricing)
