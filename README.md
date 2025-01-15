# Python War Card Game

A classic two-player card game implemented in Python. Players compete to win all the cards in a deck through a series of battles, where higher-ranked cards win.

## Features
- **Full Deck Implementation** – 52 cards with four suits and values from 1 to King.
- **Dynamic Gameplay** – Players draw cards, compare values, and collect cards from the table.
- **Interactive Play** – Users press Enter to proceed through each round.
- **Custom Classes** – Separate classes for `Card`, `Deck`, `Hand`, and `War` ensure modularity.
- **Win/Loss Tracking** – Automatically determines the winner when one player has all the cards.

## How to Play
1. Run the game in your terminal.
2. Press Enter to draw cards for both players in each round.
3. The player with the higher card wins the round and collects all the cards on the table.
4. If two cards have the same color, their numbers are compared.
5. The game ends when one player has all the cards.

## Installation
### Prerequisites
- Python 3.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-War-Card-Game.git
   cd Python-War-Card-Game
   ```
2. Run the game:
   ```bash
   python war.py
   ```

## File Structure
```
📂 Python-War-Card-Game
├── 📄 card.py       # Card class
├── 📄 deck.py       # Deck class
├── 📄 hand.py       # Hand class
├── 📄 war.py        # Game logic
├── 📄 test.py       # Unit tests
└── 📂 assets        # Any additional assets (if needed)
```

## Code Overview
- **`Card` Class**: Represents an individual card with a number and suit.
- **`Deck` Class**: Creates and shuffles a deck of cards.
- **`Hand` Class**: Manages a player's collection of cards.
- **`War` Class**: Implements the gameplay logic.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is open-source and available under the MIT License.

---
♠️ ♥️ ♣️ ♦️ *Enjoy the game and may the best player win!*

