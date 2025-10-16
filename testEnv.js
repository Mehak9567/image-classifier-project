import dotenv from "dotenv";
dotenv.config();

console.log("https://api-inference.huggingface.co/models/google/vit-base-patch16-224", process.env.HUGGING_FACE_API_URL);
console.log("hf_pvXQNMbTQlFAOfufJTrvFqWUWoyKTOVvpjs", process.env.HUGGING_FACE_API_KEY ? "Loaded ✅" : "Not Found ❌");
