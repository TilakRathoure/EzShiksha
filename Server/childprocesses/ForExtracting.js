import { spawn } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const Solve = (req, res) => {
    if (!req.file || !req.file.path) {
        return res.status(400).json({ error: 'No file uploaded' });
    }

    const imagePath = req.file.path;
    const scriptPath = path.join(__dirname, '..', 'python', 'Extract.py');

    console.log('scriptPath:', scriptPath);
    console.log('imagePath:', imagePath);

    let responseData = '';

    const childPython = spawn('python', [scriptPath, imagePath]);

    childPython.stdout.on('data', (data) => {
        responseData += data.toString();
    });

    childPython.stderr.on('data', (data) => {
        console.error(`Python stderr: ${data.toString()}`);
    });

    childPython.on('close', (code) => {
        console.log(`Child process exited with code ${code}`);
        res.json({ trying: responseData });
    });
};

export default Solve;
