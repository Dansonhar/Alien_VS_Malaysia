# 🎨 Asset Guide - Aliens vs Malaysians

## Overview
This folder contains PNG assets that can be easily swapped with your custom graphics.

## Asset Files

| File | Size | Description |
|------|------|-------------|
| `alien_normal.png` | 512x512 | Normal green alien character |
| `alien_helmet.png` | 512x512 | Alien wearing a protective helmet |
| `alien_hit.png` | 512x512 | Alien being hit (spiral eyes, shocked) |
| `durian.png` | 512x512 | Spiky durian fruit projectile |
| `malaysian_male.png` | 512x512 | Male helper in baju melayu + songkok |
| `malaysian_female.png` | 512x512 | Female helper in baju kurung + tudung |

## How to Swap Assets

1. **Prepare your images** - Make them ~512x512 pixels with transparent background (PNG)
2. **Replace the file** - Simply overwrite the existing file with your custom image
3. **Keep the same filename** - The games reference assets by filename

## Asset Paths in Code

The games load assets from this config:
```javascript
const ASSETS = {
    alienNormal: '../assets/alien_normal.png',
    alienHelmet: '../assets/alien_helmet.png',
    alienHit: '../assets/alien_hit.png',
    durian: '../assets/durian.png',
    malaysianMale: '../assets/malaysian_male.png',
    malaysianFemale: '../assets/malaysian_female.png'
};
```

## Fallback Behavior

If an asset fails to load, the game will automatically use canvas-drawn graphics as a fallback.

## Adding More Assets

To add new asset varieties:
1. Add the new PNG to this folder
2. Add the path to the `ASSETS` config in the game file
3. Reference it in your drawing code

---
*Swap these with your own custom characters!* 🎮
