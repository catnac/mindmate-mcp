from pydantic import BaseModel, Field

class GetMotivationalQuoteInput(BaseModel):
    emotion: str = Field(..., description="User emotion, e.g. 'stressed', 'tired', 'anxious'")

class GetMotivationalQuoteOutput(BaseModel):
    quote: str


class SuggestMindfulnessActivityInput(BaseModel):
    emotion: str = Field(..., description="User emotion, e.g. 'stressed', 'tired', 'anxious'")

class SuggestMindfulnessActivityOutput(BaseModel):
    tip: str


class DailyReflectionPromptOutput(BaseModel):
    prompt: str
