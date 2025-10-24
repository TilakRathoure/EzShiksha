import express from "express";
import { getMyProfile, login, logout, nice, register } from "../controllers/user.js";
import { isAuthenticated } from "../middlewares/auth.js";
import Notemaking from "../childprocesses/Fornotemaking.js";
import Grammerly from "../childprocesses/Forgrammerly.js";
import Extract from "../childprocesses/ForExtracting.js";
import multer from "multer";
import Solve from "../childprocesses/ForSolving.js";
import Summarizer from "../childprocesses/forsummarizer.js";

const router = express.Router();

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './uploads');
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});
  
  const upload = multer({ storage: storage });

router.post("/upload",upload.single('image'),Extract)
router.post("/solve",upload.single('imagesolve'),Solve)
router.post("/note",Notemaking)
router.post("/summarize",Summarizer)
router.post("/gram",Grammerly)
router.post("/new", register);
router.post("/login", login);


router.get("/nice",nice);
router.get("/logout",isAuthenticated, logout);
router.get("/me", isAuthenticated, getMyProfile);

export default router;
