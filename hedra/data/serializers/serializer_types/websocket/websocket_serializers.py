from hedra.core.engines.types.websocket.action import WebsocketAction
from hedra.core.engines.types.common.types import RequestTypes
from hedra.data.serializers.serializer_types.common.base_serializer import BaseSerializer
from typing import List, Dict, Union, Any


class WebsocketSerializer(BaseSerializer):

    def __init__(self) -> None:
        super().__init__()

    def serialize_action(
        self,
        action: WebsocketAction
    ) -> Dict[str, Union[str, List[str]]]:
        
        serialized_action = super().serialize_action()
        return {
            **serialized_action,
            'type': RequestTypes.HTTP,
            'url': {
                'full': action.url.full,
                'ip_addr': action.url.ip_addr,
                'socket_config': action.url.socket_config,
                'has_ip_addr': action.url.has_ip_addr
            },
            'method': action.method,
            'headers': action._headers,
            'header_items': action._header_items,
            'encoded_headers': action.encoded_headers,
            'data': action.data,
            'encoded_data': action.encoded_data,
            'is_stream': action.is_stream,
            'is_setup': action.is_setup,
            'action_args': action.action_args,
        }
    
    def deserialize_action(
        self,
        action: Dict[str, Any]
    ) -> WebsocketAction:
        
        url_config = action.get('url', {})
        metadata = action.get('metadata', {})
        
        websocket_action = WebsocketAction(
            name=action.get('name'),
            url=url_config.get('full'),
            headers=action.get('headers'),
            data=action.get('data'),
            user=metadata.get('user'),
            tags=metadata.get('tags', [])
        )

        websocket_action.url.ip_addr = url_config.get('ip_addr')
        websocket_action.url.socket_config = url_config.get('socket_config')
        websocket_action.url.has_ip_addr = url_config.get('has_ip_addr')

        websocket_action.setup()

        return websocket_action
    