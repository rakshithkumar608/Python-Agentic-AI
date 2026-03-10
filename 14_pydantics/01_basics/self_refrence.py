from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None 
    
Comment.model_rebuild()

replies = None
comment = Comment(
    id= 1,
    content="first comment",
    replies=[
        Comment(
            id= 2,
            content="reply to first comment",
            replies=[
                Comment(
                    id= 3,
                    content="reply to reply",
                    replies=[
                        Comment(
                            id= 4,
                            content="reply to reply to reply"
                        )
                    ]
                )
            ]
        )
    ]
)

print(comment)