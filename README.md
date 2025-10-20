# Poker Tournament Clock

A simple poker tournament clock that displays a full-screen countdown timer with visual indicators and automatic round transitions.
https://oraweb.github.io/poker-clock/

## Features

- **Large Countdown Display**: Centered, responsive timer showing hours:minutes:seconds that scales to fit any screen
- **Full-Screen Support**: Optimized for all devices - desktops, laptops, tablets, and phones
- **Responsive Design**: Timer, rounds table, and all UI elements automatically adapt to screen size
- **Multiple Configurations**: Support for multiple tournament configurations with different structures
- **Configurable Rounds**: Define tournament rounds in `config-*.yml` files with custom names, durations, and break indicators
- **Multi-Platform Control**: 
  - **Desktop/Laptop**: Press **SPACEBAR** to start/pause the timer, **ENTER** to manually advance to the next round
  - **Mobile/Tablet**: Tap on-screen buttons to Start/Pause or advance to the next round
  - **Collapsible Rounds Table**: Toggle button on mobile/tablet to show/hide rounds table for more screen space
- **Auto-Progression**: Automatically advances to the next round when timer reaches zero
- **Visual Warnings**: 
  - Orange pulsing at 2-minute warning
  - Red flashing during final 10 seconds
- **Break Indicator**: Different background color for break rounds
- **Touch-Friendly**: Large, easily tappable buttons on mobile devices with visual feedback
- **GitHub Pages**: Automatically deployed via GitHub Actions

## Quick Start

### Local Usage

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate the HTML page:
   ```bash
   python generate_clock.py
   ```

3. Open `index.html` in your web browser

### GitHub Pages Deployment

The poker clock automatically deploys to GitHub Pages when:
- You push to the main branch
- You manually trigger the workflow via workflow_dispatch

To enable GitHub Pages:
1. Go to your repository Settings
2. Navigate to Pages
3. Under "Build and deployment", select "GitHub Actions" as the source

## Configuration

The poker clock supports multiple tournament configurations. Create configuration files following the pattern `config-*.yml` (e.g., `config-tourney.yml`, `config-league.yml`). The system will automatically detect up to 10 configuration files and generate separate clock pages for each.

### Creating Configuration Files

Edit or create `config-*.yml` files to customize your tournament structure:

```yaml
rounds:
  - number: 1
    name: "Round 1"
    duration: 20  # minutes
    is_break: false
  
  - number: 2
    name: "Break"
    duration: 5  # minutes
    is_break: true
```

### Configuration Options

- `number`: Round number (for display)
- `name`: Round name (displayed prominently)
- `duration`: Round length in minutes
- `is_break`: `true` for breaks (changes background color), `false` for regular rounds

### Example Configurations

The repository includes example configurations:
- **config-tourney.yml**: Standard tournament with longer rounds (20 minutes)
- **config-league.yml**: League play with shorter rounds (15 minutes)

## Usage

1. Open the poker clock page (index.html)
2. Select your desired tournament configuration (Tourney, League, etc.)
3. **Desktop/Laptop**: Press **SPACEBAR** to start the timer, **SPACEBAR** again to pause, **ENTER** to manually advance to the next round
4. **Mobile/Tablet**: Tap the **▶ Start** button to start, **⏸ Pause** to pause, **⏭ Next Round** to advance
5. **Mobile/Tablet**: Use the **Show/Hide Rounds** button in the top-right corner to toggle the rounds table
6. Timer automatically advances to the next round when it reaches zero

## Device-Specific Features

### Desktop & Laptop
- Full keyboard control with SPACEBAR and ENTER keys
- Rounds table always visible on the left side
- Large timer display optimized for external monitors/projectors
- Instructions show keyboard shortcuts

### Tablet
- Touch-friendly control buttons below the timer
- Collapsible rounds table to maximize screen space
- Responsive timer that scales to tablet screen size
- Instructions show tap controls

### Mobile Phones
- Large, easily tappable control buttons
- Collapsible rounds table accessible via toggle button
- Timer automatically sized to fit phone screen (tested on iPhone 15 and similar devices)
- Optimized layout with rounds table at top when visible
- Instructions show tap controls

## Visual States

- **Normal**: Blue gradient background, white timer
- **Warning** (< 2 minutes): Orange pulsing timer
- **Final Countdown** (< 10 seconds): Red flashing timer
- **Break**: Red/pink gradient background

## Technical Details

- Pure HTML, CSS, and JavaScript (no external dependencies for the clock itself)
- Python script generates self-contained HTML files
- Fully responsive design with CSS media queries and viewport-based sizing
- Works on any screen size from mobile phones (375px) to large displays (1920px+)
- Touch-optimized controls with proper tap targets (minimum 44x44px)
- Adaptive UI that detects device type and shows appropriate controls
- No audio (visual indicators only)

## License

MIT License
