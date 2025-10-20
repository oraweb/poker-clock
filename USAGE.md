# Poker Clock Usage Guide

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate the clock:**
   ```bash
   python generate_clock.py
   ```

3. **Open in browser:**
   - Double-click `index.html`, or
   - Open with your preferred browser

## Using the Clock

### Controls

- **SPACEBAR** - Start/Pause the timer
- **Refresh Page** - Reset to first round

### Visual Indicators

The clock provides visual feedback based on time remaining:

| Time Remaining | Visual State |
|---------------|--------------|
| > 2 minutes | Normal white text on blue background |
| ≤ 2 minutes | Orange pulsing timer |
| ≤ 10 seconds | Red flashing timer |
| Break rounds | Red/pink background gradient |

## Customizing Tournament Structure

Edit `config.yml` to customize your tournament:

```yaml
rounds:
  - number: 1
    name: "Round 1"
    duration: 20  # minutes
    is_break: false
```

### Configuration Fields

- **number**: Round number (displayed in small text above round name)
- **name**: Round name (displayed prominently)
- **duration**: Round length in **minutes**
  - Example: 20 = 20 minutes
  - Example: 15 = 15 minutes
  - Example: 5 = 5 minutes
- **is_break**: Set to `true` for break rounds, `false` for regular rounds

### Example Tournament Structures

#### Short Tournament (4 rounds)
```yaml
rounds:
  - number: 1
    name: "Round 1"
    duration: 15  # minutes
    is_break: false
  
  - number: 2
    name: "Round 2"
    duration: 15
    is_break: false
  
  - number: 3
    name: "Break"
    duration: 3  # minutes
    is_break: true
  
  - number: 4
    name: "Final Round"
    duration: 20  # minutes
    is_break: false
```

#### Long Tournament with Multiple Breaks
```yaml
rounds:
  - number: 1
    name: "Round 1 - 25/50"
    duration: 30  # minutes
    is_break: false
  
  - number: 2
    name: "Round 2 - 50/100"
    duration: 30
    is_break: false
  
  - number: 3
    name: "Break"
    duration: 10  # minutes
    is_break: true
  
  - number: 4
    name: "Round 3 - 100/200"
    duration: 30
    is_break: false
  
  - number: 5
    name: "Round 4 - 200/400"
    duration: 30
    is_break: false
  
  - number: 6
    name: "Dinner Break"
    duration: 30  # minutes
    is_break: true
  
  - number: 7
    name: "Round 5 - 400/800"
    duration: 30
    is_break: false
  
  - number: 8
    name: "Final Round"
    duration: 30
    is_break: false
```

## Regenerating After Changes

After editing `config.yml`, regenerate the HTML:

```bash
python generate_clock.py
```

This creates a new `index.html` with your updated configuration.

## Full-Screen Mode

For the best experience:

1. Open `index.html` in your browser
2. Press **F11** (Windows/Linux) or **Control+Command+F** (Mac) for full-screen mode
3. Press **SPACEBAR** to start the tournament

## Tips

- **Test your configuration** - Run through a quick test with short durations (e.g., 10 seconds per round) to ensure everything works as expected
- **Display on second monitor** - Open the clock on a second monitor or TV visible to all players
- **Prepare in advance** - Generate the HTML before your tournament starts
- **Keep a backup** - Save different configurations for different tournament types

## Troubleshooting

### Python script fails

**Error:** `FileNotFoundError: Configuration file 'config.yml' not found`
- **Solution:** Make sure you're running the script from the directory containing `config.yml`

**Error:** `Invalid YAML in configuration file`
- **Solution:** Check your YAML syntax. Ensure proper indentation (use spaces, not tabs)

### Timer not working

- **Check:** Make sure JavaScript is enabled in your browser
- **Try:** Refresh the page (F5 or Ctrl+R)
- **Verify:** You're opening the latest generated `index.html`

### Spacebar not working

- **Check:** Click on the page first to ensure it has focus
- **Try:** Click anywhere on the clock display, then press spacebar

## GitHub Pages Deployment

Once merged to the main branch and workflow is run:

1. Your clock will be accessible at: `https://<username>.github.io/<repo-name>/`
2. You can bookmark this URL for quick access
3. Works on any device with a modern web browser (phone, tablet, computer)

### Updating the Live Version

1. Edit `config.yml` in the repository
2. Commit and push changes to main branch
3. GitHub Actions will automatically regenerate and deploy
4. Or manually trigger the workflow from the Actions tab

## Advanced Customization

If you want to customize the appearance (colors, fonts, sizes), you can modify `generate_clock.py`:

- Look for the `<style>` section in the `generate_html()` function
- Modify CSS properties as desired
- Regenerate the HTML

Example customizations:
- Change timer font size: Modify `.timer { font-size: 12rem; }`
- Change colors: Modify `background: linear-gradient(...)` 
- Change warning times: Modify the JavaScript conditions for `warning` and `final-countdown` classes
