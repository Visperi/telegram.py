"""
MIT License

Copyright (c) 2022 Niko Mätäsaho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from typing_extensions import TYPE_CHECKING
from .types.poll import (
    PollOption as PollOptionPayload,
    PollAnswer as PollAnswerPayload,
    Poll as PollPayload
)


if TYPE_CHECKING:
    from .message import MessageEntity


class PollOption:

    __slots__ = (
        "text",
        "voter_count"
    )

    def __init__(self, payload: PollOptionPayload):
        self.text = payload["text"]
        self.voter_count = payload["voter_count"]


class PollAnswer:

    __slots__ = (
        "poll_id",
        "user",
        "option_ids"
    )

    def __init__(self, payload: PollAnswerPayload):
        self.poll_id = payload["poll_id"]
        self.user = payload["user"]
        self.option_ids = payload["option_ids"]


class Poll:

    __slots__ = (
        "id",
        "question",
        "options",
        "total_voter_count",
        "is_closed",
        "is_anonymous",
        "type",
        "allows_multiple_answers",
        "correct_option_id",
        "explanation",
        "explanation_entities",
        "open_period",
        "close_date"
    )

    def __init__(self, payload: PollPayload):
        self._update(payload)

    def _update(self, payload: PollPayload):
        self.id = payload["id"]
        self.question = payload["question"]
        self.options = [PollOption(o) for o in payload["options"]]
        self.total_voter_count = payload["total_voter_count"]
        self.is_closed = payload["is_closed"]
        self.is_anonymous = payload["is_anonymous"]
        self.type = payload["type"]
        self.allows_multiple_answers = payload["allows_multiple_answers"]
        self.correct_option_id = payload.get("correct_option_id", -1)
        self.explanation = payload.get("explanation")
        self.open_period = payload.get("open_period", -1)
        self.close_date = payload.get("close_date", -1)

        try:
            self.explanation_entities = [MessageEntity(e) for e in payload["explanation_entities"]]
        except KeyError:
            self.explanation_entities = []
