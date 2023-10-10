const http = require('http');
const os = require('os');

const server = http.createServer((req, res) => {
    // Get the hostname
    const hostname = os.hostname();

    // Get the IP address
    const networkInterfaces = os.networkInterfaces();
    let ip = 'N/A';
    for (const name of Object.keys(networkInterfaces)) {
        for (const net of networkInterfaces[name]) {
            if (net.family === 'IPv4' && !net.internal) {
                ip = net.address;
                break;
            }
        }
    }

    // Get the server uptime
    let uptime = os.uptime(); // in seconds
    const days = Math.floor(uptime / (24 * 60 * 60));
    uptime %= (24 * 60 * 60);
    const hours = Math.floor(uptime / (60 * 60));
    uptime %= (60 * 60);
    const minutes = Math.floor(uptime / 60);
    const seconds = uptime % 60;

    // Get total and free memory in MB
    const totalMemoryMB = (os.totalmem() / (1024 * 1024)).toFixed(2);
    const freeMemoryMB = (os.freemem() / (1024 * 1024)).toFixed(2);

    // Get the number of CPUs
    const cpuCount = os.cpus().length;

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(`Hostname: ${hostname}\nIP Address: ${ip}\nUptime: ${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds.toFixed(0)} Seconds\nTotal Memory: ${totalMemoryMB} MB\nFree Memory: ${freeMemoryMB} MB\nNumber of CPUs: ${cpuCount}`);
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
