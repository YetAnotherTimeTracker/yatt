"""
Created by anthony on 05.11.17
service_utils

only generics should be here
"""
from config.db_config import db_session


def find_all(entity_class):
    all_entities = db_session.query(entity_class)
    return all_entities


def find_one_by_id(id_value, entity_class):
    """ assuming id is unique, get entity of entity_class by it """
    id_int = None
    try:
        id_int = int(id_value)

    except ValueError as e:
        err_cause = 'Provided value is not valid id'
        raise ValueError(err_cause)

    entity_by_id = db_session.query(entity_class) \
        .filter_by(id=id_int) \
        .first()
    # here can be none if nothing found!
    return entity_by_id


def save(entity):
    """ insert entity into db """
    db_session.add(entity)
    db_session.commit()
    return entity


def flush(entity):
    """ prepare entity for insertion (fill id attribute but do _not_ insert) """
    db_session.add(entity)
    db_session.flush()
    return entity


class JsonSerializable:
    """
    Subclasses of this class are guaranteed to be able to be converted to JSON format.
    All subclasses of this class must override to_json.
    """

    def to_json(self):
        """
        Returns a JSON string representation of this class.
        This function must be overridden by subclasses.
        :return: a JSON formatted string.
        """
        raise NotImplementedError


class Dictionaryable:
    """
    Subclasses of this class are guaranteed to be able to be converted to dictionary.
    All subclasses of this class must override to_dic.
    """

    def to_dic(self):
        """
        Returns a JSON string representation of this class.
        This function must be overridden by subclasses.
        :return: a JSON formatted string.
        """
        raise NotImplementedError


class JsonDeserializable:
    """
    Subclasses of this class are guaranteed to be able to be created from a json-style dict or json formatted string.
    All subclasses of this class must override de_json.
    """

    @classmethod
    def de_json(cls, json_type):
        """
        Returns an instance of this class from the given json dict or string.
        This function must be overridden by subclasses.
        :return: an instance of this class created from the given json dict or string.
        """
        raise NotImplementedError

    @staticmethod
    def check_json(json_type):
        """
        Checks whether json_type is a dict or a string. If it is already a dict, it is returned as-is.
        If it is not, it is converted to a dict by means of json.loads(json_type)
        :param json_type:
        :return:
        """
        try:
            str_types = (str, unicode)
        except NameError:
            str_types = (str,)

        if type(json_type) == dict:
            return json_type
        elif type(json_type) in str_types:
            return json.loads(json_type)
        else:
            raise ValueError("json_type should be a json dict or string.")

    def __str__(self):
        d = {}
        for x, y in six.iteritems(self.__dict__):
            if hasattr(y, '__dict__'):
                d[x] = y.__dict__
            else:
                d[x] = y

        return six.text_type(d)


class Update(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type):
        obj = cls.check_json(json_type)
        update_id = obj['update_id']
        message = None
        edited_message = None
        channel_post = None
        edited_channel_post = None
        inline_query = None
        chosen_inline_result = None
        callback_query = None
        shipping_query = None
        pre_checkout_query = None
        if 'message' in obj:
            message = Message.de_json(obj['message'])
        if 'edited_message' in obj:
            edited_message = Message.de_json(obj['edited_message'])
        if 'channel_post' in obj:
            channel_post = Message.de_json(obj['channel_post'])
        if 'edited_channel_post' in obj:
            edited_channel_post = Message.de_json(obj['edited_channel_post'])
        if 'inline_query' in obj:
            inline_query = InlineQuery.de_json(obj['inline_query'])
        if 'chosen_inline_result' in obj:
            chosen_inline_result = ChosenInlineResult.de_json(obj['chosen_inline_result'])
        if 'callback_query' in obj:
            callback_query = CallbackQuery.de_json(obj['callback_query'])
        if 'shipping_query' in obj:
            shipping_query = ShippingQuery.de_json(obj['shipping_query'])
        if 'pre_checkout_query' in obj:
            pre_checkout_query = PreCheckoutQuery.de_json(obj['pre_checkout_query'])
        return cls(update_id, message, edited_message, channel_post, edited_channel_post, inline_query,
                   chosen_inline_result, callback_query, shipping_query, pre_checkout_query)

    def __init__(self, update_id, message, edited_message, channel_post, edited_channel_post, inline_query,
                 chosen_inline_result, callback_query, shipping_query, pre_checkout_query):
        self.update_id = update_id
        self.edited_message = edited_message
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query


class WebhookInfo(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        url = obj['url']
        has_custom_certificate = obj['has_custom_certificate']
        pending_update_count = obj['pending_update_count']
        last_error_date = None
        last_error_message = None
        max_connections = None
        allowed_updates = None
        if 'last_error_message' in obj:
            last_error_date = obj['last_error_date']
        if 'last_error_message' in obj:
            last_error_message = obj['last_error_message']
        if 'max_connections' in obj:
            max_connections = obj['max_connections']
        if 'allowed_updates' in obj:
            allowed_updates = obj['allowed_updates']
        return cls(url, has_custom_certificate, pending_update_count, last_error_date, last_error_message,
                   max_connections, allowed_updates)

    def __init__(self, url, has_custom_certificate, pending_update_count, last_error_date, last_error_message,
                 max_connections, allowed_updates):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates


class User(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        id = obj['id']
        is_bot = obj['is_bot']
        first_name = obj['first_name']
        last_name = obj.get('last_name')
        username = obj.get('username')
        language_code = obj.get('language_code')
        return cls(id, is_bot, first_name, last_name, username, language_code)

    def __init__(self, id, is_bot, first_name, last_name=None, username=None, language_code=None):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username
        self.last_name = last_name
        self.language_code = language_code# -*- coding: utf-8 -*-

try:
    import ujson as json
except ImportError:
    import json

import six

from telebot import util


class JsonSerializable:
    """
    Subclasses of this class are guaranteed to be able to be converted to JSON format.
    All subclasses of this class must override to_json.
    """

    def to_json(self):
        """
        Returns a JSON string representation of this class.
        This function must be overridden by subclasses.
        :return: a JSON formatted string.
        """
        raise NotImplementedError


class Dictionaryable:
    """
    Subclasses of this class are guaranteed to be able to be converted to dictionary.
    All subclasses of this class must override to_dic.
    """

    def to_dic(self):
        """
        Returns a JSON string representation of this class.
        This function must be overridden by subclasses.
        :return: a JSON formatted string.
        """
        raise NotImplementedError


class JsonDeserializable:
    """
    Subclasses of this class are guaranteed to be able to be created from a json-style dict or json formatted string.
    All subclasses of this class must override de_json.
    """

    @classmethod
    def de_json(cls, json_type):
        """
        Returns an instance of this class from the given json dict or string.
        This function must be overridden by subclasses.
        :return: an instance of this class created from the given json dict or string.
        """
        raise NotImplementedError

    @staticmethod
    def check_json(json_type):
        """
        Checks whether json_type is a dict or a string. If it is already a dict, it is returned as-is.
        If it is not, it is converted to a dict by means of json.loads(json_type)
        :param json_type:
        :return:
        """
        try:
            str_types = (str, unicode)
        except NameError:
            str_types = (str,)

        if type(json_type) == dict:
            return json_type
        elif type(json_type) in str_types:
            return json.loads(json_type)
        else:
            raise ValueError("json_type should be a json dict or string.")

    def __str__(self):
        d = {}
        for x, y in six.iteritems(self.__dict__):
            if hasattr(y, '__dict__'):
                d[x] = y.__dict__
            else:
                d[x] = y

        return six.text_type(d)


class Update(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type):
        obj = cls.check_json(json_type)
        update_id = obj['update_id']
        message = None
        edited_message = None
        channel_post = None
        edited_channel_post = None
        inline_query = None
        chosen_inline_result = None
        callback_query = None
        shipping_query = None
        pre_checkout_query = None
        if 'message' in obj:
            message = Message.de_json(obj['message'])
        if 'edited_message' in obj:
            edited_message = Message.de_json(obj['edited_message'])
        if 'channel_post' in obj:
            channel_post = Message.de_json(obj['channel_post'])
        if 'edited_channel_post' in obj:
            edited_channel_post = Message.de_json(obj['edited_channel_post'])
        if 'inline_query' in obj:
            inline_query = InlineQuery.de_json(obj['inline_query'])
        if 'chosen_inline_result' in obj:
            chosen_inline_result = ChosenInlineResult.de_json(obj['chosen_inline_result'])
        if 'callback_query' in obj:
            callback_query = CallbackQuery.de_json(obj['callback_query'])
        if 'shipping_query' in obj:
            shipping_query = ShippingQuery.de_json(obj['shipping_query'])
        if 'pre_checkout_query' in obj:
            pre_checkout_query = PreCheckoutQuery.de_json(obj['pre_checkout_query'])
        return cls(update_id, message, edited_message, channel_post, edited_channel_post, inline_query,
                   chosen_inline_result, callback_query, shipping_query, pre_checkout_query)

    def __init__(self, update_id, message, edited_message, channel_post, edited_channel_post, inline_query,
                 chosen_inline_result, callback_query, shipping_query, pre_checkout_query):
        self.update_id = update_id
        self.edited_message = edited_message
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query


class WebhookInfo(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        url = obj['url']
        has_custom_certificate = obj['has_custom_certificate']
        pending_update_count = obj['pending_update_count']
        last_error_date = None
        last_error_message = None
        max_connections = None
        allowed_updates = None
        if 'last_error_message' in obj:
            last_error_date = obj['last_error_date']
        if 'last_error_message' in obj:
            last_error_message = obj['last_error_message']
        if 'max_connections' in obj:
            max_connections = obj['max_connections']
        if 'allowed_updates' in obj:
            allowed_updates = obj['allowed_updates']
        return cls(url, has_custom_certificate, pending_update_count, last_error_date, last_error_message,
                   max_connections, allowed_updates)

    def __init__(self, url, has_custom_certificate, pending_update_count, last_error_date, last_error_message,
                 max_connections, allowed_updates):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates


class User(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        id = obj['id']
        is_bot = obj['is_bot']
        first_name = obj['first_name']
        last_name = obj.get('last_name')
        username = obj.get('username')
        language_code = obj.get('language_code')
        return cls(id, is_bot, first_name, last_name, username, language_code)

    def __init__(self, id, is_bot, first_name, last_name=None, username=None, language_code=None):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username
        self.last_name = last_name
        self.language_code = language_code
