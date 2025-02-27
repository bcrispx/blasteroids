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

## 📥 Installation Options

### Option 1: Download Standalone Executable (Easiest)
1. Go to the [Releases](https://github.com/bcrispx/blasteroids/releases) page
2. Download the latest `Blasteroids.exe`
3. Double-click to play!

No installation or Python required - just download and play!

### Option 2: Install from Source

#### Step 1: Get Python
1. Download Python from [python.org](https://python.org)
2. During installation, make sure to check "Add Python to PATH"
3. To verify installation, open Command Prompt and type:
   ```
   python --version
   ```

#### Step 2: Get the Game
Choose one of these methods:

##### Method A: Download ZIP
1. Click the green "Code" button above
2. Select "Download ZIP"
3. Extract the ZIP file to your preferred location

##### Method B: Clone with Git
```bash
git clone https://github.com/bcrispx/blasteroids.git
cd blasteroids
```

#### Step 3: Set Up the Game
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

### Controls:
- `↑` (Up Arrow): Thrust forward
- `←` `→` (Left/Right Arrows): Rotate ship
- `Space`: Fire lasers
- `Esc`: Quit game

### Game Rules:
- Destroy asteroids to score points
- Large asteroids split into smaller ones
- Avoid colliding with asteroids
- You start with 3 lives
- Clear all asteroids to advance to next level
- Each level increases difficulty

### When Game Over:
- Press `Space` to play again
- Press `Esc` to quit

## 🔧 Troubleshooting

### For Standalone Executable:
1. **"Windows protected your PC" message**
   - Click "More info"
   - Click "Run anyway"
   - This appears because the executable is not signed with a certificate

2. **Game won't start**
   - Make sure you extracted all files from the ZIP
   - Try running as administrator
   - Check your antivirus isn't blocking it

3. **No sound**
   - Check if your system volume is on
   - Make sure no other programs are using your sound device
   - Try restarting the game

### For Python Version:
1. **"Python not found" error**
   - Make sure Python is installed and added to PATH
   - Try using `python3` instead of `python`

2. **"Module not found" error**
   - Make sure you're in the virtual environment (you should see `(venv)` in your prompt)
   - Try running `pip install -r requirements.txt` again

3. **Game running slowly**
   - Close other running applications
   - Make sure your graphics drivers are up to date
   - Check if your computer meets the minimum requirements

### Still Having Issues?
Open an issue on GitHub with:
- Your operating system
- Version you're using (executable or Python)
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
