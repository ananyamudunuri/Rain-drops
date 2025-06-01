# Rain-drops Simulation 🌧️

This is a fun rain simulation built in Python using Pygame and Pymunk. You control a bucket or a person to catch falling rain drops, with realistic bounce and sound effects.

## 🎨 Features

Adjustable rain speed via a slider

Realistic gravity and bouncing using Pymunk physics

Background music of rain sounds

Beautiful background visuals

Interactive control (move left/right to catch rain)

Splash effect when raindrops hit the object

## 🚀 Getting Started

1. Clone the repo

<pre>git clone https://github.com/ananyamudunuri/Rain-drops.git
cd Rain-drops </pre>

2. Set up the virtual environment

<pre>python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate </pre>

3. Install the dependencies

<pre>pip install -r requirements.txt </pre>

4. Run the simulation

<pre>python main.py</pre>

## 📁 Project Structure
<pre>rain_sim/
├── assets/                # Images, background, music
├── main.py                # Main execution file
├── config.py              # Constants and settings
├── rain/
│   ├── drop.py            # Drop logic
│   ├── bucket.py          # Bucket object (currently used)
│   └── person.py          # Optional person object
├── utils/
│   ├── draw.py            # Rendering logic
│   └── slider.py          # Custom rain-speed slider
└── requirements.txt       # Python dependencies 
  </pre>

## 🎧 Credits

Background music: royalty-free rain audio

Built with: Pygame + Pymunk

## 🚀 Future Ideas

Animate bucket filling with water

Splash particles

Score counter

Mobile-friendly controls

## Made with ❤️ by Ananya Mudunuri

