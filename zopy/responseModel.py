#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

class ZohoError(Schema):
	
	message = fields.String()
	code = fields.Integer()

class ZohoResponse(Schema):

	uri = fields.String()
	error = fields.Nested(ZohoError,default={})
	result = fields.Dict()