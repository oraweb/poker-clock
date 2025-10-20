#!/usr/bin/env python3
"""
Poker Clock Generator
Generates a static HTML page with embedded CSS and JavaScript for a poker tournament clock.
"""

import yaml
import json
import os


def load_config(config_file='config.yml'):
    """Load tournament configuration from YAML file."""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def generate_html(config):
    """Generate the complete HTML page with embedded CSS and JavaScript."""
    
    rounds_json = json.dumps(config['rounds'])
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poker Tournament Clock</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }}

        .container {{
            text-align: center;
            width: 90%;
            max-width: 1200px;
        }}

        .round-info {{
            margin-bottom: 30px;
        }}

        .round-number {{
            font-size: 2rem;
            opacity: 0.8;
            margin-bottom: 10px;
        }}

        .round-name {{
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 20px;
        }}

        .timer {{
            font-size: 12rem;
            font-weight: bold;
            font-family: 'Courier New', monospace;
            line-height: 1;
            margin: 40px 0;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
            transition: all 0.3s ease;
        }}

        .timer.warning {{
            color: #ffa500;
            animation: pulse 1s ease-in-out infinite;
        }}

        .timer.final-countdown {{
            color: #ff4444;
            animation: flash 0.5s ease-in-out infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{
                transform: scale(1);
            }}
            50% {{
                transform: scale(1.05);
            }}
        }}

        @keyframes flash {{
            0%, 100% {{
                opacity: 1;
            }}
            50% {{
                opacity: 0.3;
            }}
        }}

        .controls {{
            margin-top: 30px;
            font-size: 1.5rem;
            opacity: 0.7;
        }}

        .status {{
            margin-top: 20px;
            font-size: 2rem;
            font-weight: bold;
        }}

        .status.paused {{
            color: #ffa500;
        }}

        .status.running {{
            color: #00ff00;
        }}

        .next-round {{
            margin-top: 30px;
            font-size: 1.5rem;
            opacity: 0.6;
        }}

        .break-indicator {{
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        }}

        .instructions {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 1.2rem;
            opacity: 0.5;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="round-info">
            <div class="round-number" id="roundNumber">Round 1</div>
            <div class="round-name" id="roundName">Loading...</div>
        </div>
        
        <div class="timer" id="timer">00:00:00</div>
        
        <div class="status paused" id="status">PAUSED</div>
        
        <div class="next-round" id="nextRound"></div>
    </div>
    
    <div class="instructions">
        Press SPACEBAR to Start/Pause
    </div>

    <script>
        // Tournament configuration
        const rounds = {rounds_json};
        
        // State management
        let currentRoundIndex = 0;
        let timeRemaining = 0;
        let isRunning = false;
        let timerInterval = null;

        // DOM elements
        const timerElement = document.getElementById('timer');
        const statusElement = document.getElementById('status');
        const roundNumberElement = document.getElementById('roundNumber');
        const roundNameElement = document.getElementById('roundName');
        const nextRoundElement = document.getElementById('nextRound');

        // Format time as HH:MM:SS
        function formatTime(seconds) {{
            const hours = Math.floor(seconds / 3600);
            const minutes = Math.floor((seconds % 3600) / 60);
            const secs = seconds % 60;
            
            return [hours, minutes, secs]
                .map(v => v.toString().padStart(2, '0'))
                .join(':');
        }}

        // Update the display
        function updateDisplay() {{
            const currentRound = rounds[currentRoundIndex];
            
            // Update round info
            roundNumberElement.textContent = `Round ${{currentRound.number}}`;
            roundNameElement.textContent = currentRound.name;
            
            // Update timer
            timerElement.textContent = formatTime(timeRemaining);
            
            // Update visual indicators based on time remaining
            timerElement.classList.remove('warning', 'final-countdown');
            
            if (timeRemaining <= 10 && timeRemaining > 0) {{
                timerElement.classList.add('final-countdown');
            }} else if (timeRemaining <= 120 && timeRemaining > 10) {{
                timerElement.classList.add('warning');
            }}
            
            // Update body background for breaks
            if (currentRound.is_break) {{
                document.body.style.background = 'linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%)';
            }} else {{
                document.body.style.background = 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)';
            }}
            
            // Show next round info
            if (currentRoundIndex < rounds.length - 1) {{
                const nextRound = rounds[currentRoundIndex + 1];
                nextRoundElement.textContent = `Next: ${{nextRound.name}}`;
            }} else {{
                nextRoundElement.textContent = 'Final Round';
            }}
        }}

        // Start the next round
        function startNextRound() {{
            if (currentRoundIndex < rounds.length - 1) {{
                currentRoundIndex++;
                timeRemaining = rounds[currentRoundIndex].duration;
                updateDisplay();
            }} else {{
                // Tournament finished
                stopTimer();
                statusElement.textContent = 'TOURNAMENT COMPLETE';
                statusElement.className = 'status';
            }}
        }}

        // Timer tick function
        function tick() {{
            if (timeRemaining > 0) {{
                timeRemaining--;
                updateDisplay();
            }} else {{
                // Round finished, start next round
                startNextRound();
            }}
        }}

        // Start the timer
        function startTimer() {{
            if (!isRunning) {{
                isRunning = true;
                statusElement.textContent = 'RUNNING';
                statusElement.className = 'status running';
                timerInterval = setInterval(tick, 1000);
            }}
        }}

        // Stop the timer
        function stopTimer() {{
            if (isRunning) {{
                isRunning = false;
                statusElement.textContent = 'PAUSED';
                statusElement.className = 'status paused';
                clearInterval(timerInterval);
            }}
        }}

        // Toggle timer
        function toggleTimer() {{
            if (isRunning) {{
                stopTimer();
            }} else {{
                startTimer();
            }}
        }}

        // Keyboard event listener
        document.addEventListener('keydown', (event) => {{
            if (event.code === 'Space') {{
                event.preventDefault();
                toggleTimer();
            }}
        }});

        // Initialize the clock
        function init() {{
            currentRoundIndex = 0;
            timeRemaining = rounds[0].duration;
            updateDisplay();
        }}

        // Start the application
        init();
    </script>
</body>
</html>
"""
    
    return html_content


def main():
    """Main function to generate the poker clock HTML."""
    print("Loading configuration from config.yml...")
    config = load_config()
    
    print(f"Generating HTML for {len(config['rounds'])} rounds...")
    html = generate_html(config)
    
    output_file = 'index.html'
    with open(output_file, 'w') as f:
        f.write(html)
    
    print(f"Successfully generated {output_file}")
    print(f"Open {output_file} in a web browser to use the poker clock.")


if __name__ == '__main__':
    main()
