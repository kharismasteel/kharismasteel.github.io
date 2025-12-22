# CSS Color Reference Guide

## Updated Color Palette (December 2025)

### Primary Colors
- **Primary Blue**: `#3b82f6` (Bright, Eye-catching blue)
  - Used for: Buttons, active links, primary CTAs, pagination active state, hover effects
  - Previous: `#6366f1` (Pale indigo)
  
- **Secondary Orange**: `#f97316` (Vibrant, warm orange)
  - Used for: Accent elements, secondary buttons, highlights
  - New addition for better visual contrast

- **Accent Cyan**: `#06b6d4` (Cool cyan)
  - Used for: Additional accent elements, special highlights
  - New addition for visual diversity

### Neutral Colors
- **Dark Text**: `#0f172a` (Very dark slate)
- **Light Background**: `#f8fafc` (Off-white)
- **Gray Text**: `#475569` / `#64748b` (Medium gray)
- **Light Gray**: `#e2e8f0` (Light gray for borders)

## Components Updated

### Buttons
- `.btn-primary`: Now `#3b82f6` with darker hover state `#1e40af`
- Enhanced shadows: `0 10px 30px -5px rgba(59, 130, 246, 0.4)`
- Transform on hover: `translateY(-2px)` for lift effect

### Product Cards
- Border: 2px solid `#3b82f6`
- Hover shadow: `0 15px 40px -10px rgba(59, 130, 246, 0.25)`
- Hover transform: `translateY(-4px)` for lift effect

### Pagination
- Active page: `#3b82f6` with shadow and 2px border
- Hover state: `#3b82f6` with transform effect

### Share Links
- Hover background: `#3b82f6` with enhanced shadow
- Transform on hover: `translateY(-2px)`

### Navigation
- Glass-morphism effect with blue tints
- Hero gradient: Blue-to-orange blend with new colors

### Promo Banner
- Background: Linear gradient with new color scheme
- Primary: `#3b82f6` → Secondary: `#f97316`

## Usage in Templates

### CSS Variables (Root)
```css
:root {
  --primary-color: #3b82f6;
  --secondary-color: #f97316;
  --accent-color: #06b6d4;
}
```

### In Tailwind Classes
- `bg-blue-500` → Maps to `#3b82f6`
- `hover:bg-blue-700` → Maps to `#1e40af`
- `text-blue-600` → Maps to `#2563eb`

## Visual Impact

✅ **Bolder**: Colors are more saturated and eye-catching
✅ **Professional**: High contrast with improved readability
✅ **Modern**: Vibrant but not overwhelming
✅ **Consistent**: Applied across all interactive elements

## Build Info

- Last updated: December 22, 2025
- Jekyll build: ✅ Successful
- All components: ✅ Updated
- Site output: `/workspaces/kharismasteel.github.io/_site/`

## Future Modifications

To change colors globally:
1. Update `:root` CSS variables in `css/override.css`
2. Find and replace `#3b82f6` with new color throughout file
3. Run `jekyll build` to verify
4. Test site in browser at `http://127.0.0.1:4000/`
