const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

let serverData = {};

app.post('/update', (req, res) => {
  const { serverIp, incomingTraffic } = req.body;
  serverData[serverIp] = { incomingTraffic, timestamp: Date.now() };
  res.sendStatus(200);
});

app.get('/servers', (req, res) => {
  res.json(serverData);
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
