const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static(__dirname)); // Serves HTML, CSS, and JS files

// Load Users Data
const usersFilePath = path.join(__dirname, 'users.json');
const loadUsers = () => JSON.parse(fs.readFileSync(usersFilePath, 'utf8'));

// Sign-Up Endpoint
app.post('/signup', (req, res) => {
    const { fullName, email, password } = req.body;
    const users = loadUsers();

    if (users.some(user => user.email === email)) {
        return res.status(400).json({ message: 'User already exists!' });
    }

    users.push({ fullName, email, password });
    fs.writeFileSync(usersFilePath, JSON.stringify(users, null, 2));

    res.status(200).json({ message: 'Sign-Up successful! Please log in.' });
});

// Login Endpoint
app.post('/login', (req, res) => {
    const { email, password } = req.body;
    const users = loadUsers();

    const user = users.find(user => user.email === email && user.password === password);

    if (!user) {
        return res.status(401).json({ message: 'Invalid email or password' });
    }

    res.status(200).json({ message: 'Login successful!', redirect: '/home.html' });
});

// Start Server
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
