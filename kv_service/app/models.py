from pydantic import BaseModel, Field

class KeyValueModel(BaseModel):
    """A very simple model to serve as the basis for the key value storage."""
    
    value: str | None = Field(None, title='The value to store.', max_length=1000)
