import express from "express";
import { getMyProfile, login, logout, nice, register } from "../controllers/user.js";
import { isAuthenticated } from "../middlewares/auth.js";
import Notemaking from "../Fornotemaking.js";
import Grammerly from "../Forgrammerly.js";
import Extract from "../ForExtracting.js";
import multer from "multer";
import Solve from "../ForSolving.js";

const router = express.Router();

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, '/tmp/uploads');
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});
  
  const upload = multer({ storage: storage });

router.post("/upload",upload.single('image'),Extract)
router.post("/solve",upload.single('imagesolve'),Solve)
router.post("/note",Notemaking)
router.post("/gram",Grammerly)
router.post("/new", register);
router.post("/login", login);


router.get("/nice",nice);
router.get("/logout",isAuthenticated, logout);
router.get("/me", isAuthenticated, getMyProfile);

export default router;
