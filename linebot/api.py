"""linebot.api module."""
import json
from .__about__ import __version__
from .exceptions import LineBotApiError
from .http_client import HttpClient, RequestsHttpClient
from .models import (
    Error, Profile, MemberIds, Content, RichMenuResponse, MessageQuotaResponse,
    MessageQuotaConsumptionResponse, IssueLinkTokenResponse, IssueChannelTokenResponse,
    MessageDeliveryBroadcastResponse, MessageDeliveryMulticastResponse,
    MessageDeliveryPushResponse, MessageDeliveryReplyResponse,
    InsightMessageDeliveryResponse, InsightFollowersResponse, InsightDemographicResponse,
    InsightMessageEventResponse, BroadcastResponse, NarrowcastResponse,
    MessageProgressNarrowcastResponse, BotInfo, GetWebhookResponse, TestWebhookResponse,
    AudienceGroup, ClickAudienceGroup, ImpAudienceGroup, GetAuthorityLevel, Audience,
    CreateAudienceGroup
)
from .models.responses import Group, UserIds, RichMenuAliasResponse, RichMenuAliasListResponse
class LineBotApi(object):

    DEFAULT_API_ENDPOINT = 'https://api.line.me'
    DEFAULT_API_DATA_ENDPOINT = 'https://api-data.line.me'

    def __init__(self, channel_access_token,
                 endpoint=DEFAULT_API_ENDPOINT, data_endpoint=DEFAULT_API_DATA_ENDPOINT,
                 timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient):
        self.data_endpoint = data_endpoint
        self.endpoint = endpoint
        self.headers = {
            'Authorization': 'Bearer ' + channel_access_token,
            'User-Agent': 'line-bot-sdk-python/' + __version__
        }
        if http_client:
            self.http_client = http_client(timeout=timeout)
        else:
            self.http_client = RequestsHttpClient(timeout=timeout)

    def reply_message(self, reply_token, messages, notification_disabled=False, timeout=None):
        if not isinstance(messages, (list, tuple)):
            messages = [messages]
        data = {
            'replyToken': reply_token,
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }
        self._post('/v2/bot/message/reply', data=json.dumps(data), timeout=timeout)

    def push_message(self, to, messages,retry_key=None, notification_disabled=False, timeout=None):
        if not isinstance(messages, (list, tuple)):
            messages = [messages]
        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key
        data = {
            'to': to,
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }
        self._post('/v2/bot/message/push', data=json.dumps(data), timeout=timeout)

    def multicast(self, to, messages, retry_key=None, notification_disabled=False, timeout=None):
        if not isinstance(messages, (list, tuple)):
            messages = [messages]
        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key
        data = {
            'to': to,
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }        
        self._post('/v2/bot/message/multicast', data=json.dumps(data), timeout=timeout)

    def broadcast(self, messages, retry_key=None, notification_disabled=False, timeout=None):
        if not isinstance(messages, (list, tuple)):
            messages = [messages]
        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key
        data = {
            'messages': [message.as_json_dict() for message in messages],
            'notificationDisabled': notification_disabled,
        }
        response = self._post('/v2/bot/message/broadcast', data=json.dumps(data), timeout=timeout)
        return BroadcastResponse(request_id=response.headers.get('X-Line-Request-Id'))

    def narrowcast(
            self, messages,
            retry_key=None, recipient=None, filter=None, limit=None,
            notification_disabled=False, timeout=None):
        if not isinstance(messages, (list, tuple)):
            messages = [messages]
        if retry_key:
            self.headers['X-Line-Retry-Key'] = retry_key
        data = {
            'messages': [message.as_json_dict() for message in messages],
            'recipient': recipient.as_json_dict(),
            'filter': filter.as_json_dict(),
            'limit': limit.as_json_dict(),
            'notificationDisabled': notification_disabled,
        }

        response = self._post('/v2/bot/message/narrowcast', data=json.dumps(data), timeout=timeout)
        return NarrowcastResponse(request_id=response.headers.get('X-Line-Request-Id'))

    def get_progress_status_narrowcast(self, request_id, timeout=None):
        """Get progress status of narrowcast messages sent.

        https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status

        Gets the number of messages sent with the /bot/message/progress/narrowcast endpoint.

        :param str request_id: request ID of narrowcast.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageDeliveryBroadcastResponse`
        """
        response = self._get(
            '/v2/bot/message/progress/narrowcast?requestId={request_id}'.format(
                request_id=request_id),
            timeout=timeout
        )

        return MessageProgressNarrowcastResponse.new_from_json_dict(response.json)

    def get_message_delivery_broadcast(self, date, timeout=None):
        response = self._get(
            '/v2/bot/message/delivery/broadcast?date={date}'.format(date=date),
            timeout=timeout
        )
        return MessageDeliveryBroadcastResponse.new_from_json_dict(response.json)

    def get_message_delivery_reply(self, date, timeout=None):
        response = self._get(
            '/v2/bot/message/delivery/reply?date={date}'.format(date=date),
            timeout=timeout
        )

        return MessageDeliveryReplyResponse.new_from_json_dict(response.json)

    def get_message_delivery_push(self, date, timeout=None):
        response = self._get(
            '/v2/bot/message/delivery/push?date={date}'.format(date=date),
            timeout=timeout
        )

        return MessageDeliveryPushResponse.new_from_json_dict(response.json)

    def get_message_delivery_multicast(self, date, timeout=None):
        response = self._get(
            '/v2/bot/message/delivery/multicast?date={date}'.format(date=date),
            timeout=timeout
        )
        return MessageDeliveryMulticastResponse.new_from_json_dict(response.json)

    def get_profile(self, user_id, timeout=None):
        response = self._get(
            '/v2/bot/profile/{user_id}'.format(user_id=user_id),
            timeout=timeout
        )
        return Profile.new_from_json_dict(response.json)

    def get_group_summary(self, group_id, timeout=None):
        response = self._get(
            '/v2/bot/group/{group_id}/summary'.format(group_id=group_id),
            timeout=timeout
        )
        return Group.new_from_json_dict(response.json)

    def get_group_members_count(self, group_id, timeout=None):
        response = self._get(
            '/v2/bot/group/{group_id}/members/count'.format(group_id=group_id),
            timeout=timeout
        )
        return response.json.get('count')

    def get_room_members_count(self, room_id, timeout=None):
        response = self._get(
            '/v2/bot/room/{room_id}/members/count'.format(room_id=room_id),
            timeout=timeout
        )
        return response.json.get('count')

    def get_group_member_profile(self, group_id, user_id, timeout=None):
        response = self._get(
            '/v2/bot/group/{group_id}/member/{user_id}'.format(group_id=group_id, user_id=user_id),
            timeout=timeout
        )
        return Profile.new_from_json_dict(response.json)

    def get_room_member_profile(self, room_id, user_id, timeout=None):
        response = self._get(
            '/v2/bot/room/{room_id}/member/{user_id}'.format(room_id=room_id, user_id=user_id),
            timeout=timeout
        )
        return Profile.new_from_json_dict(response.json)

    def get_group_member_ids(self, group_id, start=None, timeout=None):
        params = None if start is None else {'start': start}
        response = self._get(
            '/v2/bot/group/{group_id}/members/ids'.format(group_id=group_id),
            params=params,
            timeout=timeout
        )
        return MemberIds.new_from_json_dict(response.json)





    def get_room_member_ids(self, room_id, start=None, timeout=None):
        params = None if start is None else {'start': start}
        response = self._get(
            '/v2/bot/room/{room_id}/members/ids'.format(room_id=room_id),
            params=params,
            timeout=timeout
        )
        return MemberIds.new_from_json_dict(response.json)

    def get_message_content(self, message_id, timeout=None):
        response = self._get(
            '/v2/bot/message/{message_id}/content'.format(message_id=message_id),
            endpoint=self.data_endpoint, stream=True, timeout=timeout
        )
        return Content(response)

    def leave_group(self, group_id, timeout=None):
        self._post(
            '/v2/bot/group/{group_id}/leave'.format(group_id=group_id),
            timeout=timeout
        )

    def leave_room(self, room_id, timeout=None):
        self._post(
            '/v2/bot/room/{room_id}/leave'.format(room_id=room_id),
            timeout=timeout
        )

    def get_rich_menu(self, rich_menu_id, timeout=None):
        response = self._get(
            '/v2/bot/richmenu/{rich_menu_id}'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

        return RichMenuResponse.new_from_json_dict(response.json)

    def get_rich_menu_alias(self, rich_menu_alias_id=None, timeout=None):
        response = self._get(
            '/v2/bot/richmenu/alias/{rich_menu_id}'.format(rich_menu_id=rich_menu_alias_id),
            timeout=timeout
        )
        return RichMenuAliasResponse.new_from_json_dict(response.json)

    def get_rich_menu_alias_list(self, timeout=None):
        response = self._get(
            '/v2/bot/richmenu/alias/list',
            timeout=timeout
        )
        return RichMenuAliasListResponse.new_from_json_dict(response.json)

    def create_rich_menu(self, rich_menu, timeout=None):
        response = self._post(
            '/v2/bot/richmenu', data=rich_menu.as_json_string(), timeout=timeout
        )
        return response.json.get('richMenuId')

    def create_rich_menu_alias(self, rich_menu_alias, timeout=None):
        self._post(
            '/v2/bot/richmenu/alias', data=rich_menu_alias.as_json_string(), timeout=timeout
        )

    def update_rich_menu_alias(self, rich_menu_alias_id, rich_menu_alias, timeout=None):
        self._post(
            '/v2/bot/richmenu/alias/{rich_menu_id}'.format(rich_menu_id=rich_menu_alias_id),
            data=rich_menu_alias.as_json_string(),
            timeout=timeout
        )

    def delete_rich_menu(self, rich_menu_id, timeout=None):
        self._delete(
            '/v2/bot/richmenu/{rich_menu_id}'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

    def delete_rich_menu_alias(self, rich_menu_alias_id, timeout=None):
        self._delete(
            '/v2/bot/richmenu/alias/{rich_menu_alias_id}'.format(
                rich_menu_alias_id=rich_menu_alias_id),
            timeout=timeout
        )

    def get_rich_menu_id_of_user(self, user_id, timeout=None):
        response = self._get(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )
        return response.json.get('richMenuId')

    def link_rich_menu_to_user(self, user_id, rich_menu_id, timeout=None):
        self._post(
            '/v2/bot/user/{user_id}/richmenu/{rich_menu_id}'.format(
                user_id=user_id,
                rich_menu_id=rich_menu_id
            ),
            timeout=timeout
        )

    def link_rich_menu_to_users(self, user_ids, rich_menu_id, timeout=None):
        self._post(
            '/v2/bot/richmenu/bulk/link',
            data=json.dumps({
                'userIds': user_ids,
                'richMenuId': rich_menu_id,
            }),
            timeout=timeout
        )

    def unlink_rich_menu_from_user(self, user_id, timeout=None):
        self._delete(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )

    def unlink_rich_menu_from_users(self, user_ids, timeout=None):
        self._post(
            '/v2/bot/richmenu/bulk/unlink',
            data=json.dumps({
                'userIds': user_ids,
            }),
            timeout=timeout
        )

    def get_rich_menu_image(self, rich_menu_id, timeout=None):
        response = self._get(
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            endpoint=self.data_endpoint, timeout=timeout
        )
        return Content(response)

    def set_rich_menu_image(self, rich_menu_id, content_type, content, timeout=None):
        self._post(
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            endpoint=self.data_endpoint,
            data=content,
            headers={'Content-Type': content_type},
            timeout=timeout
        )

    def get_rich_menu_list(self, timeout=None):
        response = self._get(
            '/v2/bot/richmenu/list',
            timeout=timeout
        )
        result = []
        for richmenu in response.json['richmenus']:
            result.append(RichMenuResponse.new_from_json_dict(richmenu))
        return result

    def set_default_rich_menu(self, rich_menu_id, timeout=None):
        self._post(
            '/v2/bot/user/all/richmenu/{rich_menu_id}'.format(
                rich_menu_id=rich_menu_id,
            ),
            timeout=timeout
        )

    def get_default_rich_menu(self, timeout=None):
        response = self._get(
            '/v2/bot/user/all/richmenu',
            timeout=timeout
        )
        return response.json.get('richMenuId')

    def cancel_default_rich_menu(self, timeout=None):
        self._delete(
            '/v2/bot/user/all/richmenu',
            timeout=timeout
        )

    def get_message_quota(self, timeout=None):
        response = self._get(
            '/v2/bot/message/quota',
            timeout=timeout
        )

        return MessageQuotaResponse.new_from_json_dict(response.json)

    def get_message_quota_consumption(self, timeout=None):
        response = self._get(
            '/v2/bot/message/quota/consumption',
            timeout=timeout
        )
        return MessageQuotaConsumptionResponse.new_from_json_dict(response.json)

    def issue_link_token(self, user_id, timeout=None):
        response = self._post(
            '/v2/bot/user/{user_id}/linkToken'.format(
                user_id=user_id
            ),
            timeout=timeout
        )

        return IssueLinkTokenResponse.new_from_json_dict(response.json)

    def issue_channel_token(self, client_id, client_secret, grant_type='client_credentials', timeout=None):
        response = self._post(
            '/v2/oauth/accessToken',
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': grant_type,
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=timeout
        )
        return IssueChannelTokenResponse.new_from_json_dict(response.json)

    def revoke_channel_token(self, access_token, timeout=None):
        self._post(
            '/v2/oauth/revoke',
            data={'access_token': access_token},
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            timeout=timeout
        )

    def get_insight_message_delivery(self, date, timeout=None):
        response = self._get(
            '/v2/bot/insight/message/delivery?date={date}'.format(date=date),
            timeout=timeout
        )
        return InsightMessageDeliveryResponse.new_from_json_dict(response.json)

    def get_insight_followers(self, date, timeout=None):
        response = self._get(
            '/v2/bot/insight/followers?date={date}'.format(date=date),
            timeout=timeout
        )
        return InsightFollowersResponse.new_from_json_dict(response.json)

    def get_insight_demographic(self, timeout=None):
        response = self._get(
            '/v2/bot/insight/demographic',
            timeout=timeout
        )
        return InsightDemographicResponse.new_from_json_dict(response.json)

    def get_insight_message_event(self, request_id, timeout=None):
        response = self._get(
            '/v2/bot/insight/message/event?requestId={request_id}'.format(request_id=request_id),
            timeout=timeout
        )
        return InsightMessageEventResponse.new_from_json_dict(response.json)

    def get_bot_info(self, timeout=None):
        response = self._get(
            '/v2/bot/info',
            timeout=timeout
        )
        return BotInfo.new_from_json_dict(response.json)

    def create_audience_group(self, audience_group_name, audiences=[], is_ifa=False, timeout=None):
        if audiences:
            audiences = [Audience.new_from_json_dict(audience) for audience in audiences]
        response = self._post(
            '/v2/bot/audienceGroup/upload',
            data=json.dumps({
                "description": audience_group_name,
                "isIfaAudience": is_ifa,
                "audiences": [audience.as_json_dict() for audience in audiences],
            }),
            timeout=timeout
        )
        return CreateAudienceGroup.new_from_json_dict(response.json)

    def get_audience_group(self, audience_group_id, timeout=None):
        response = self._get(
            '/v2/bot/audienceGroup/{audience_group_id}'.format(
                audience_group_id=audience_group_id),
            timeout=timeout
        )
        return AudienceGroup.new_from_json_dict(response.json)

    def get_audience_group_list(self, page=1, description=None, status=None, size=20, include_external_public_group=None, create_route=None, timeout=None):
        params = {}
        if page:
            params["page"] = page
        if description:
            params["description"] = description
        if status:
            params["status"] = status
        if size:
            params["size"] = size
        if include_external_public_group:
            params["includesExternalPublicGroup"] = include_external_public_group
        if create_route:
            params["createRoute"] = create_route
        response = self._get(
            '/v2/bot/audienceGroup/list?',
            params=params,
            timeout=timeout
        )
        result = []
        for audience_group in response.json.get('audienceGroups', []):
            result.append(AudienceGroup.new_from_json_dict(audience_group))
        if response.json.get('hasNextPage', False):
            result += self.get_audience_group_list(page + 1, description, status, size, include_external_public_group, create_route, timeout)
        return result

    def delete_audience_group(self, audience_group_id, timeout=None):
        self._delete(
            '/v2/bot/audienceGroup/{}'.format(audience_group_id),
            timeout=timeout
        )

    def rename_audience_group(self, audience_group_id, description, timeout=None):
        self._put(
            '/v2/bot/audienceGroup/{audience_group_id}/updateDescription'.format(
                audience_group_id=audience_group_id),
            data=json.dumps({
                "description": description,
            }),
            timeout=timeout
        )
        return ''

    def add_audiences_to_audience_group(self, audience_group_id, audiences, upload_description=None, timeout=None):
        if audiences:
            audiences = [Audience.new_from_json_dict(audience) for audience in audiences]
        response = self._put(
            '/v2/bot/audienceGroup/upload',
            data=json.dumps({
                "audienceGroupId": audience_group_id,
                "audiences": [audience.as_json_dict() for audience in audiences],
                "uploadDescription": upload_description,
            }),
            timeout=timeout
        )
        return response.json

    def get_audience_group_authority_level(self, timeout=None):
        response = self._get(
            '/v2/bot/audienceGroup/authorityLevel',
            timeout=timeout
        )
        return GetAuthorityLevel.new_from_json_dict(response.json)

    def change_audience_group_authority_level(self, authority_level='PUBLIC', timeout=None):
        self._put(
            '/v2/bot/audienceGroup/authorityLevel',
            data=json.dumps({
                "authorityLevel": authority_level,
            }),
            timeout=timeout
        )
        return ''

    def create_click_audience_group(self, description, request_id, click_url=None, timeout=None):
        response = self._post(
            '/v2/bot/audienceGroup/click',
            data=json.dumps({
                "description": description,
                "requestId": request_id,
                "clickUrl": click_url,
            }),
            timeout=timeout
        )
        return ClickAudienceGroup.new_from_json_dict(response.json)

    def create_imp_audience_group(self, description, request_id, timeout=None):
        response = self._post(
            '/v2/bot/audienceGroup/imp',
            data=json.dumps({
                "description": description,
                "requestId": request_id,
            }),
            timeout=timeout
        )
        return ImpAudienceGroup.new_from_json_dict(response.json)

    def set_webhook_endpoint(self, webhook_endpoint, timeout=None):
        data = {
            'endpoint': webhook_endpoint
        }
        response = self._put(
            '/v2/bot/channel/webhook/endpoint',
            data=json.dumps(data),
            timeout=timeout,
        )
        return response.json

    def get_webhook_endpoint(self, timeout=None):
        response = self._get(
            '/v2/bot/channel/webhook/endpoint',
            timeout=timeout,
        )
        return GetWebhookResponse.new_from_json_dict(response.json)

    def test_webhook_endpoint(self, webhook_endpoint=None, timeout=None):
        data = {}
        if webhook_endpoint is not None:
            data['endpoint'] = webhook_endpoint
        response = self._post(
            '/v2/bot/channel/webhook/test',
            data=json.dumps(data),
            timeout=timeout,
        )
        return TestWebhookResponse.new_from_json_dict(response.json)

    def get_followers_ids(self, limit=300, start=None, timeout=None):
        params = {'limit': limit} if start is None else {'limit': limit, 'start': start}
        response = self._get(
            '/v2/bot/followers/ids',
            params=params,
            timeout=timeout
        )
        return UserIds.new_from_json_dict(response.json)

    def _get(self, path, endpoint=None, params=None, headers=None, stream=False, timeout=None):
        url = (endpoint or self.endpoint) + path
        if headers is None:
            headers = {}
        headers.update(self.headers)
        response = self.http_client.get(url, headers=headers, params=params, stream=stream, timeout=timeout)
        self.__check_error(response)
        return response

    def _post(self, path, endpoint=None, data=None, headers=None, timeout=None):
        url = (endpoint or self.endpoint) + path
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)
        response = self.http_client.post(
            url, headers=headers, data=data, timeout=timeout
        )
        self.__check_error(response)
        return response

    def _delete(self, path, endpoint=None, data=None, headers=None, timeout=None):
        url = (endpoint or self.endpoint) + path
        if headers is None:
            headers = {}
        headers.update(self.headers)
        response = self.http_client.delete(
            url, headers=headers, data=data, timeout=timeout
        )
        self.__check_error(response)
        return response

    def _put(self, path, endpoint=None, data=None, headers=None, timeout=None):
        url = (endpoint or self.endpoint) + path
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)
        response = self.http_client.put(
            url, headers=headers, data=data, timeout=timeout
        )
        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            raise LineBotApiError(
                status_code=response.status_code,
                headers=dict(response.headers.items()),
                request_id=response.headers.get('X-Line-Request-Id'),
                accepted_request_id=response.headers.get('X-Line-Accepted-Request-Id'),
                error=Error.new_from_json_dict(response.json)
            )