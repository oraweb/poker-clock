# Poker Tournament Clock

A simple, elegant poker tournament clock that displays a full-screen countdown timer with visual indicators and automatic round transitions.

![Poker Clock Screenshot](https://github.com/user-attachments/assets/9142957d-4d1a-4769-b2cf-c9cfdc69b59f)

## Features

- **Large Countdown Display**: Centered, very large timer showing hours:minutes:seconds
- **Full-Screen Support**: Optimized for any device with a large screen
- **Configurable Rounds**: Define tournament rounds in `config.yml` with custom names, durations, and break indicators
- **Keyboard Control**: Press spacebar to start/pause the timer
- **Auto-Progression**: Automatically advances to the next round when timer reaches zero
- **Visual Warnings**: 
  - Orange pulsing at 2-minute warning
  - Red flashing during final 10 seconds
- **Break Indicator**: Different background color for break rounds
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

Edit `config.yml` to customize your tournament structure:

```yaml
rounds:
  - number: 1
    name: "Round 1"
    duration: 1200  # 20 minutes in seconds
    is_break: false
  
  - number: 2
    name: "Break"
    duration: 300  # 5 minutes in seconds
    is_break: true
```

### Configuration Options

- `number`: Round number (for display)
- `name`: Round name (displayed prominently)
- `duration`: Round length in seconds
- `is_break`: `true` for breaks (changes background color), `false` for regular rounds

## Usage

1. Open the poker clock page
2. Press **SPACEBAR** to start the timer
3. Press **SPACEBAR** again to pause
4. Timer automatically advances to the next round when it reaches zero

## Visual States

- **Normal**: Blue gradient background, white timer
- **Warning** (< 2 minutes): Orange pulsing timer
- **Final Countdown** (< 10 seconds): Red flashing timer
- **Break**: Red/pink gradient background

## Screenshots

| Paused State | Running | 2-Minute Warning | Break Time |
|--------------|---------|------------------|------------|
| ![Paused](https://github.com/user-attachments/assets/9142957d-4d1a-4769-b2cf-c9cfdc69b59f) | ![Running](https://github.com/user-attachments/assets/a30dd18f-5186-4c93-a06f-62e74cdc07ed) | ![Warning](https://github.com/user-attachments/assets/cc97f12b-fbd8-43f2-8177-0afef58f56e0) | ![Break](https://github.com/user-attachments/assets/7ec09cbc-955f-4973-9b47-346fc5426273) |

## Technical Details

- Pure HTML, CSS, and JavaScript (no external dependencies for the clock itself)
- Python script generates a single self-contained HTML file
- Responsive design works on any screen size
- No audio (visual indicators only)

## License

MIT License
