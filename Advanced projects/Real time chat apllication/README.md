

# Real-Time Chat Application
# Developed by : Nathishwar
A Python-based real-time chat application using Flask and Flask-SocketIO for instant messaging with WebSocket communication.

![Chat Application Screenshot](https://via.placeholder.com/800x500?text=Chat+App+Screenshot) 
*(You can add a real screenshot later)*

## Features

- Real-time messaging using WebSockets
- User join/leave notifications
- Simple username system
- Clean, responsive interface
- Multiple client support
- Broadcast messages to all connected clients

## Technologies Used

- **Backend**: Python, Flask
- **WebSockets**: Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript
- **Client Library**: Socket.IO

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nathishwar-prog/realtime-chat-app.git
   cd realtime-chat-app
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter a username and start chatting!

## Project Structure

```
realtime-chat-app/
├── app.py                # Main application file
├── templates/
│   └── index.html        # Frontend HTML template
├── static/
│   └── style.css         # CSS styling
└── requirements.txt      # Python dependencies
```

## Configuration

The application uses default configuration. You can modify these in `app.py`:

- Change the secret key: `app.config['SECRET_KEY'] = 'your-secret-key'`
- Modify the port: `socketio.run(app, port=5001)`

## How to Use

1. Open the application in your browser
2. Enter a username in the first input field
3. Type your message in the second input field
4. Press Enter or click the Send button
5. All connected clients will see your messages in real-time

## Future Enhancements

- [ ] User authentication system
- [ ] Private/direct messaging
- [ ] Chat rooms/channels
- [ ] Message history persistence
- [ ] File sharing capability
- [ ] Online users list

## Troubleshooting

**Issue**: Socket connection errors  
**Solution**: Make sure you're using compatible versions of Flask-SocketIO and Socket.IO client

**Issue**: Messages not appearing  
**Solution**: 
1. Check browser console for errors (F12)
2. Verify the Flask server is running
3. Ensure you've entered a username before sending messages

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask and Flask-SocketIO documentation
- Socket.IO library
- Various open-source chat applications for inspiration
```

This README includes:
1. Project overview
2. Features list
3. Technology stack
4. Installation instructions
5. Usage guide
6. Project structure
7. Configuration options
8. Future enhancement ideas
9. Troubleshooting tips
10. Contribution guidelines
11. License information

You can customize it further by:
- Adding real screenshots
- Including a demo link if deployed
- Adding more detailed setup instructions for different environments
- Expanding the troubleshooting section with issues you've encountered

