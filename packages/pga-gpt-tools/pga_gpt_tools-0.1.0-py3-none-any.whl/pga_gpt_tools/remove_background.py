from pydantic import Field
from instructor import OpenAISchema
import json
import os
import fal_client

class RemoveBackground(OpenAISchema):
    """
    Remove the background of an image. Returns the URL of the new image in PNG format.
    """
    image_url: str = Field(description="The URL of the image to remove the background from")

    def run(self):
        FAL_KEY = os.environ['FALAI_API_KEY']
        os.environ['FAL_KEY'] = FAL_KEY
        try:
            handler = fal_client.submit(
                "fal-ai/birefnet",
                arguments={"image_url": self.image_url}
            )

            result = handler.get()["image"]
            return json.dumps(result)
        except Exception as e:
            return str(e)