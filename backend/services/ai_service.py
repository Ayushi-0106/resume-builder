import os
from openai import OpenAI
from typing import List, Dict, Any

class AIService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None
            print("Warning: OPENAI_API_KEY not found. AI features will be limited.")
    
    def get_suggestions(self, content_type: str, content: str, context: str = "") -> List[str]:
        """
        Get AI suggestions for resume content improvements
        
        Args:
            content_type: Type of content (summary, experience, skills, etc.)
            content: Current content to improve
            context: Additional context (job title, industry, etc.)
        
        Returns:
            List of suggested improvements
        """
        if not self.client:
            return self._get_fallback_suggestions(content_type, content)
        
        try:
            prompt = self._build_prompt(content_type, content, context)
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional resume writing expert. Provide specific, actionable suggestions to improve resume content."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            suggestions = response.choices[0].message.content.strip().split('\n')
            # Filter out empty lines and clean up
            suggestions = [s.strip() for s in suggestions if s.strip() and not s.startswith('-')]
            
            return suggestions[:5]  # Limit to 5 suggestions
            
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return self._get_fallback_suggestions(content_type, content)
    
    def _build_prompt(self, content_type: str, content: str, context: str) -> str:
        """Build a specific prompt for the AI based on content type"""
        
        base_prompt = f"Please provide 3-5 specific suggestions to improve this {content_type} for a resume:"
        
        if content_type == "summary":
            prompt = f"{base_prompt}\n\nCurrent summary: {content}\n\nFocus on making it more compelling, specific, and achievement-oriented. Include quantifiable results if possible."
        
        elif content_type == "experience":
            prompt = f"{base_prompt}\n\nCurrent experience description: {content}\n\nFocus on using action verbs, quantifying achievements, and highlighting impact. Make it more results-driven."
        
        elif content_type == "skills":
            prompt = f"{base_prompt}\n\nCurrent skills: {content}\n\nSuggest how to better organize, prioritize, or describe these skills. Consider industry relevance and skill levels."
        
        elif content_type == "projects":
            prompt = f"{base_prompt}\n\nCurrent project description: {content}\n\nFocus on highlighting your role, technologies used, challenges overcome, and measurable outcomes."
        
        elif content_type == "education":
            prompt = f"{base_prompt}\n\nCurrent education section: {content}\n\nSuggest how to better highlight relevant coursework, achievements, or activities."
        
        else:
            prompt = f"{base_prompt}\n\nContent: {content}"
        
        if context:
            prompt += f"\n\nContext: This is for a {context} position."
        
        prompt += "\n\nProvide specific, actionable suggestions that can be directly implemented."
        
        return prompt
    
    def _get_fallback_suggestions(self, content_type: str, content: str) -> List[str]:
        """Fallback suggestions when OpenAI API is not available"""
        
        fallback_suggestions = {
            "summary": [
                "Use action verbs to start each sentence",
                "Include quantifiable achievements and metrics",
                "Focus on your unique value proposition",
                "Keep it concise (2-3 sentences maximum)",
                "Tailor it to the specific job you're applying for"
            ],
            "experience": [
                "Start each bullet point with a strong action verb",
                "Quantify your achievements with numbers and percentages",
                "Focus on impact and results, not just responsibilities",
                "Use industry-specific keywords and terminology",
                "Highlight leadership and collaboration skills"
            ],
            "skills": [
                "Group skills by category (Technical, Soft Skills, Tools)",
                "Prioritize skills most relevant to the target position",
                "Include proficiency levels where appropriate",
                "Add emerging technologies and trending skills",
                "Remove outdated or irrelevant skills"
            ],
            "projects": [
                "Describe your specific role and contributions",
                "Highlight technologies and tools used",
                "Include challenges overcome and solutions implemented",
                "Quantify project impact and outcomes",
                "Link to live demos or GitHub repositories if available"
            ],
            "education": [
                "Include relevant coursework related to the position",
                "Highlight academic achievements and honors",
                "Add relevant extracurricular activities or clubs",
                "Include certifications and continuing education",
                "Show progression and growth in your field"
            ]
        }
        
        return fallback_suggestions.get(content_type, [
            "Review for clarity and conciseness",
            "Ensure consistency in formatting and style",
            "Check for spelling and grammar errors",
            "Make content more specific and actionable",
            "Align with the job requirements"
        ])
    
    def improve_text(self, text: str, improvement_type: str) -> str:
        """
        Get an improved version of specific text
        
        Args:
            text: Text to improve
            improvement_type: Type of improvement (professional, concise, impactful)
        
        Returns:
            Improved text
        """
        if not self.client:
            return text
        
        try:
            prompts = {
                "professional": f"Rewrite this text in a more professional tone suitable for a resume: {text}",
                "concise": f"Make this text more concise while keeping all important information: {text}",
                "impactful": f"Rewrite this text to be more impactful and achievement-focused: {text}"
            }
            
            prompt = prompts.get(improvement_type, f"Improve this text: {text}")
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer. Improve the given text while maintaining accuracy and relevance."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.5
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return text
