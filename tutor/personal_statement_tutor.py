import os
import openai
from dotenv import load_dotenv
import json
from typing import Dict, Any, List
import asyncio

load_dotenv()

class PersonalStatementTutor:
    def __init__(self):
        self.model = "gpt-4"
        self.system_prompt = """You are a helpful university personal statement tutor. Your role is to:
1. Provide specific, actionable feedback on personal statements
2. Help students structure their statements effectively
3. Suggest improvements for clarity, impact, and relevance
4. Maintain a supportive and encouraging tone
5. Focus on personal statement best practices for university applications

When responding:
- Be specific and provide examples
- Break down complex suggestions into manageable steps
- Always explain the reasoning behind your feedback
- Maintain a positive and constructive approach
"""

    @classmethod
    def create(cls) -> "PersonalStatementTutor":
        return cls()

    def get_response(self, prompt: str) -> str:
        try:
            # Create a chat completion with system prompt and user message
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try again later."

    async def analyze_statement(self, statement: str) -> Dict[str, Any]:
        """Analyze a personal statement and provide structured feedback."""
        try:
            response = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=[
                    {"role": "system", "content": """Analyze this personal statement and provide structured feedback. Return JSON with:
                    - Overall strength (1-5)
                    - Strengths
                    - Areas for improvement
                    - Specific suggestions
                    - Structure assessment
                    - Personal impact assessment"""},
                    {"role": "user", "content": statement}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            feedback = response.choices[0].message.content
            return json.loads(feedback)
            
        except Exception as e:
            return {"error": str(e)}

    async def suggest_improvements(self, statement: str) -> List[str]:
        """Provide specific suggestions for improving a personal statement."""
        try:
            response = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=[
                    {"role": "system", "content": """Provide specific, actionable suggestions to improve this personal statement. 
                    Focus on:
                    - Clarity of expression
                    - Structure and organization
                    - Impact and engagement
                    - Personalization
                    - Relevance to university applications
                    Format response as a list of bullet points."""},
                    {"role": "user", "content": statement}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            return response.choices[0].message.content.split('\n')
            
        except Exception as e:
            return [f"Error: {str(e)}"]