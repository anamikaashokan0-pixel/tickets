from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from django.conf import settings

class Response(BaseModel):
    response:str=Field(
        description="Professional response send to the customer"
    )

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def evaluate_response(ticket):

    prompt = f"""
    You are a professional customer support assistant.

Create a helpful and professional response for the following support ticket.

Ticket title:
{ticket.title}

Ticket description:
{ticket.description}

Category:
{ticket.category}

Priority:
{ticket.priority}

Status:
{ticket.status}

Evaluation and response rules:

1. Clearly understand the customer's problem before generating the response.
2. Acknowledge the customer's issue politely.
3. Provide a helpful and relevant response based only on the information available
   in the ticket.
4. Do not claim that the issue has been fixed unless the ticket information
   confirms that it has been fixed.
5. Do not invent technical details, actions, or resolutions that are not supported
   by the ticket.
6. If additional information is required, politely ask the customer for it.
7. Consider the ticket priority when writing the response.
8. Keep the response concise, professional and customer-friendly.
9. Do not use unnecessary technical terminology.
10. Return only the requested structured output.
"""


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Response,
        ),
    )

    result = response.parsed

    return result