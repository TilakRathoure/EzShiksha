import axios from "axios";

const Grammerly = async (req, res) => {
  if (!req.body.name) {
    return res.status(400).json({ error: "No input text provided" });
  }

  try {
    const response = await axios.post(`${process.env.FASTAPI}/generate-notes`, {
      text: req.body.name,
    });

    res.json({ trying: response.data.notes });
  } catch (error) {
    console.error("Error calling FastAPI:", error.message);
    res.status(500).json({ error: "Failed to generate notes" });
  }
};

export default Grammerly;
