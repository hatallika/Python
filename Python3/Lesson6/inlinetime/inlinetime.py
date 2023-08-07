import datetime
from dataclasses import dataclass
from typing import Dict, Optional, Union
from aiogram import types
from aiogram.utils.callback_data import CallbackData, CallbackDataFilter

from .exceptions import (
    NotInitedException,
    WrongCallbackException
)


@dataclass
class InlineTimeData():
    min_time: datetime.time
    max_time: datetime.time
    current_time: datetime.time
    minute_step: int
    hour_step: int


class Time:
    _cb_prefix = 'inline_time'
    BASE_CALLBACK = CallbackData(_cb_prefix, 'action', 'data')
    CALLBACK_WRONG_CHOICE = BASE_CALLBACK.new(action='wrong_choice', data='_')
    CALLBACK_HOUR_DECREASE = BASE_CALLBACK.new(action='dec', data='hour')
    CALLBACK_HOUR_INCREASE = BASE_CALLBACK.new(action='inc', data='hour')
    CALLBACK_MINUTE_DECREASE = BASE_CALLBACK.new(action='dec', data='min')
    CALLBACK_MINUTE_INCREASE = BASE_CALLBACK.new(action='dec', data='min')
    CALLBACK_SUCCESS = BASE_CALLBACK.new(action='success', data='_')

    def __init__(self):
        self.data = {}

    def _get_user_info(self, chat_id: int):
        return self.data.get(chat_id, None)

    def _set_user_info(self, chat_id: int, data: Optional[InlineTimeData] = None):
        self.data[chat_id] = data

    def filter(self, **full_config):
        return Time.BASE_CALLBACK.filter(**full_config)

    def init(self,
             base_time: datetime.time,
             min_time: datetime.time,
             max_time: datetime.time,
             chat_id: Optional[int] = None,
             minute_step: int = 15,
             hour_step: int = 1):
        if chat_id is None:
            chat_id = types.User.get_current().id
        self._set_user_info(chat_id, InlineTimeData(min_time, max_time, base_time, minute_step, hour_step))

    def is_init(self, chat_id: Optional[int] = None) -> bool:
        if chat_id is None:
            chat_id = types.User.get_current().id
        return self._get_user_info(chat_id) is not None

    def reset(self, chat_id: Optional[int] = None):
        if chat_id is None:
            chat_id = types.User.get_current().id
        self._set_user_info(chat_id, None)

    def get_keyboard(self, chat_id: Optional[int] = None) -> types.InlineKeyboardMarkup:
        pass
