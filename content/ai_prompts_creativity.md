Title: AI Prompts - Creativity
Date: 2025-11-01
Category: AI
Slug: ai_prompts_creativity
Summary: Prompts for creative writing, brainstorming, and ideation

### LinkedIn Profile Picture (Image Generation)

**Prompt 1** - Classic professional headshot:

```text
Create a professional portrait of the person in the uploaded image
for a LinkedIn profile photo.

The person should have a subtle smile, conveying a professional and
confident demeanor. The person should be dressed in a black business suit,
with sharp, realistic features and an authentic touch.

The background should be gray, with a well-lit environment.
The image must be extremely detailed, rendered in 4K 360 HD resolution.
```

**Prompt 2** - Natural look with outfit change:

```text
Create a professional LinkedIn profile photo of the person in the
uploaded image.

Keep the original facial details and natural skin texture to avoid
an AI-generated look.

Change the outfit to a well-fitted dark business blazer over a light shirt,
suitable for a corporate environment.

Use a clean, neutral background (light gray or soft blue) with soft,
natural studio lighting.

Make the person face the camera with a relaxed, confident posture and
a slight, professional smile.

Crop the image as a head-and-shoulders portrait, centered, high-resolution
and photorealistic.
```

**Prompt 3** - Studio quality with technical specifications:

```text
A professional, high-resolution profile photo, maintaining the exact
facial structure, identity, and key features of the person in the input image.

The subject is framed from the chest up, with ample headroom and negative
space above their head, ensuring the top of their head is not cropped.

The person looks directly at the camera, and the subject's body is also
directly facing the camera.

They are styled for a professional photo studio shoot, wearing a smart
casual blazer.

The background is a solid '#141414' neutral studio.

Shot from a high angle with bright and airy soft, diffused studio lighting,
gently illuminating the face and creating a subtle catchlight in the eyes,
conveying a sense of clarity.

Captured on an 85mm f/1.8 lens with a shallow depth of field, exquisite
focus on the eyes, and beautiful, soft bokeh.

Observe crisp detail on the fabric texture of the blazer, individual
strands of hair, and natural, realistic skin texture.

The atmosphere exudes confidence, professionalism, and approachability.

Clean and bright cinematic color grading with subtle warmth and balanced
tones, ensuring a polished and contemporary feel.
```

---

### Lo-Fi 2010s Phone Selfie (Image Generation)

Structured prompt for generating authentic-looking casual 2010s phone selfies:

```json
{
  "scene": "casual 2010s phone selfie; unintentional snapshot",
  "subject": {
    "type": "adult woman (idol vibe)",
    "age_range": "20s",
    "hair": "straight or simple ponytail",
    "makeup": "glossy lips, eyeliner highlight",
    "jewelry": "small hoops, thin chain, bracelets"
  },
  "wardrobe": {
    "top": "basic tee or camisole",
    "bottom": "denim shorts or mini skirt",
    "footwear": "sneakers or ankle boots",
    "notes": "everyday outfit, not styled"
  },
  "pose": {
    "angle": "mirror selfie FULL BODY",
    "body": "standing, weight on one hip",
    "hands": "phone in one hand; other relaxed or in pocket",
    "framing": "HEAD-TO-SHOES, feet visible, not cropped"
  },
  "camera": {
    "device": "iPhone 4/5 era",
    "flash": "on (harsh LED) with mirror glare",
    "orientation": "vertical",
    "aspect_ratio": "4:3",
    "distance": "2-3 m from mirror to capture full body",
    "focus": "soft; slight hand-shake blur"
  },
  "look": {
    "texture": "grainy digital noise; mild JPEG artifacts",
    "sharpness": "low; soft focus",
    "color": "cool indoor white balance; blown highlights from flash",
    "effects": "subtle vignette; cheap filter vibe"
  },
  "background": {
    "environment": "bedroom or bathroom; clutter allowed; visible floor",
    "props": "framed mirror; phone visible"
  },
  "style": {
    "genre": "lo-fi Y2K/2010s snapshot",
    "authenticity": "imperfect candid moment"
  },
  "ban": [
    "studio lighting",
    "DSLR/bokeh look",
    "cinematic grading",
    "spotless staged room",
    "logos/brand text",
    "nsfw",
    "cropped feet"
  ],
  "output": {
    "count": 1,
    "size": "1200x1600",
    "safety": "strict"
  },
  "variants": [
    {
      "name": "timer_fullbody",
      "angle": "rear camera on dresser, timer; subject centered, both hands visible"
    }
  ]
}
```
