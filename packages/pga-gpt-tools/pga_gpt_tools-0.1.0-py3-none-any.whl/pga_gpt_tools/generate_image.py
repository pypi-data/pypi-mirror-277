from pydantic import Field
from typing import Literal
from instructor import OpenAISchema
from openai import OpenAI
import json
import os

class GenerateImage(OpenAISchema):
    """
    Use this tool to generate images using OpenAI DALL-E 3 model with a prompt. If you receive an error response, perhaps try again using different parameters.

    Note: when DALL-E generates an image, it will typically return a revised prompt that it actually used to generate the image. This is useful if you want to see the actual prompt that was used to generate the image. The revised prompt is included in the response as "prompt".
    """
    prompt: str = Field(description="The prompt / description used to generate the image.")
    size: Literal["1024x1024", "1024x1792", "1792x1024"] = Field(description="The dimensions of the image to generate.", default="1792x1024")
    quality: Literal["standard", "hd"] = Field(description="The quality of the image to generate.", default="standard")


    def run(self):
        try:
            api_key = os.environ['OPENAI_API_KEY']
            openai = OpenAI(api_key=api_key)
            response = openai.images.generate(
                model="dall-e-3",
                size=self.size,
                quality=self.quality,
                prompt=self.prompt
            )
            response = {
                "image_url": response.data[0].url,
                "prompt": response.data[0].revised_prompt
            }
            return json.dumps(response)
        except Exception as e:
            return str(e)
