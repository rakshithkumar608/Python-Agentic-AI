from google import genai
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Generate image
response = client.models.generate_images(
    model="imagen-3.0-generate-001",
    prompt="A futuristic AI robot coding in a neon cyberpunk city",
    config={
        "size": "1024x1024"
    }
)

# Extract image bytes
image_bytes = response.generated_images[0].image.image_bytes

# Convert to image
image = Image.open(BytesIO(image_bytes))

# Save image
image.save("ai_robot.png")

print("✅ Image saved as ai_robot.png")