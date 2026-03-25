from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    highway: str = Field(description="Federal highway, e.g. 'BR-116'")
    km_marker: float = Field(description="Kilometer marker on the highway")
    state: str = Field(description="Brazilian state abbreviation, e.g. 'MG'")
    municipality: str = Field(description="City name")
    accident_cause: str = Field(description="Reported cause, e.g. 'Falta de atenção'")
    accident_type: str = Field(description="Type of accident, e.g. 'Colisão traseira'")
    day_of_week: str = Field(description="Day of week, e.g. 'Segunda'")
    hour: int = Field(ge=0, le=23, description="Hour of day (0-23)")
    vehicles_involved: int = Field(ge=1, default=1, description="Number of vehicles")
    deaths: int | None = Field(default=None, description="Number of deaths at the scene")
    serious_injuries: int | None = Field(default=None, description="Number of serious injuries")
    minor_injuries: int | None = Field(default=None, description="Number of minor injuries")
    uninjured: int | None = Field(default=None, description="Number of uninjured people")


class PredictResponse(BaseModel):
    is_fatal: bool = Field(description="Whether the accident is predicted to be fatal")
    fatality_probability: float = Field(ge=0, le=1, description="Probability of fatality (0-1)")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    sources: list[str]
    tools_used: list[str]
