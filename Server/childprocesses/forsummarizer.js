import { spawn } from "child_process";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const Grammerly = (req, res) => {
    if (!req.body.name) {
        return res.status(400).json({ error: "No input text provided" });
    }

    const inputText = req.body.name;
    const scriptPath = path.join(__dirname, "..", "python", "summarizer.py");

    console.log("scriptPath:", scriptPath);
    console.log("inputText:", inputText);

    let responseData = '';

    const childPython = spawn('python', [scriptPath, inputText]);

    childPython.stdout.on('data', (data) => {
        responseData += data.toString();
    });

    childPython.stderr.on('data', (data) => {
        console.error(`Python stderr: ${data.toString()}`);
    });

    childPython.on('close', (code) => {
        console.log(`Child process exited with code ${code}`);

        if (code === 1) {
            return res.status(500).json({ error: "Python script error" });
        }

        res.json({ trying: responseData });
    });
};

export default Grammerly;
