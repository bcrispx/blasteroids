# 🚀 Blasteroids

A fun, retro-style arcade game inspired by the classic Asteroids. Blast your way through increasingly challenging levels while avoiding asteroid collisions!

## 🎮 Game Features

- Classic arcade-style gameplay
- Increasing difficulty with each level
- Dynamic sound effects and background beats
- Score tracking and lives system
- Authentic retro feel with modern touches

## 🎵 Sound Effects
- Shooting lasers
- Asteroid explosions (large and small)
- Thrust engine sounds
- Level-up celebration
- Game over sound
- Background heartbeat that speeds up with each level

## 🛠️ Installation Guide

### Step 1: Get Python
1. Download Python from [python.org](https://python.org)
2. During installation, make sure to check "Add Python to PATH"
3. To verify installation, open Command Prompt and type:
   ```
   python --version
   ```

### Step 2: Get the Game
Choose one of these methods:

#### Option A: Download ZIP (Easiest)
1. Click the green "Code" button above
2. Select "Download ZIP"
3. Extract the ZIP file to your preferred location

#### Option B: Clone with Git
```bash
git clone https://github.com/bcrispx/blasteroids.git
cd blasteroids
```

### Step 3: Set Up the Game
1. Open Command Prompt
2. Navigate to the game folder:
   ```bash
   cd path/to/blasteroids
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 How to Play

1. Start the game:
   ```bash
   python main.py
   ```

2. Controls:
   - `↑` (Up Arrow): Thrust forward
   - `←` `→` (Left/Right Arrows): Rotate ship
   - `Space`: Fire lasers
   - `Esc`: Quit game

3. Game Rules:
   - Destroy asteroids to score points
   - Large asteroids split into smaller ones
   - Avoid colliding with asteroids
   - You start with 3 lives
   - Clear all asteroids to advance to next level
   - Each level increases difficulty

4. When Game Over:
   - Press `Space` to play again
   - Press `Esc` to quit

## 🔧 Troubleshooting

### Common Issues:

1. **"Python not found" error**
   - Make sure Python is installed and added to PATH
   - Try using `python3` instead of `python`

2. **"Module not found" error**
   - Make sure you're in the virtual environment (you should see `(venv)` in your prompt)
   - Try running `pip install -r requirements.txt` again

3. **No sound playing**
   - Check if your system volume is on
   - Make sure no other programs are using your sound device
   - Try restarting the game

4. **Game running slowly**
   - Close other running applications
   - Make sure your graphics drivers are up to date
   - Check if your computer meets the minimum requirements

### Still Having Issues?
Open an issue on GitHub with:
- Your operating system
- Python version (`python --version`)
- Error message (if any)
- What you were doing when the issue occurred

## 🌟 Contributing

Want to contribute? Great!
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
